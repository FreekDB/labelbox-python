from datetime import datetime, timezone
import json
import logging
import os

import requests
import requests.exceptions

from labelbox import query, utils
import labelbox.exceptions
from labelbox.db_objects import Project, Dataset, User, Organization
from labelbox.paginated_collection import PaginatedCollection
from labelbox.schema import DbObject


logger = logging.getLogger(__name__)


_LABELBOX_API_KEY = "LABELBOX_API_KEY"


class Client:
    """ A Labelbox client. Containes info necessary for connecting to
    the server (URL, authentication key). Provides functions for querying
    and creating top-level data objects (Projects, Datasets).
    """

    def __init__(self, api_key=None,
                 endpoint='https://api.labelbox.com/graphql'):
        """ Create and initialize a Labelbox Client.

        Args:
            api_key (str): API key. If None, the key is obtained from
                the "LABELBOX_API_KEY" environment variable.
            endpoint (str): URL of the Labelbox server to connect to.
        """
        if api_key is None:
            if _LABELBOX_API_KEY not in os.environ:
                raise labelbox.exceptions.AuthenticationError(
                    "Labelbox API key not provided")
                api_key = os.environ[_LABELBOX_API_KEY]
        self.api_key = api_key

        logging.info("Initializing Labelbox client at '%s'", endpoint)

        self.endpoint = endpoint
        self.headers = {'Accept': 'application/json',
                        'Content-Type': 'application/json',
                        'Authorization': 'Bearer %s' % api_key}

    def execute(self, query, params=None, timeout=10.0):
        """ Sends a request to the server for the execution of the
        given query. Checks the response for errors and wraps errors
        in appropriate labelbox.exceptions.LabelboxError subtypes.

        Args:
            query (str): the query to execute.
            params (dict): query parameters referenced within the query.
            timeout (float): Max allowed time for query execution,
                in seconds.
        Return:
            dict, parsed JSON response.
        Raises:
            labelbox.exceptions.AuthenticationError: If authentication
                failed.
            labelbox.exceptions.InvalidQueryError: If `query` is not
                syntactically or semantically valid (checked server-side).
            labelbox.exceptions.ApiLimitError: If the server API limit was
                exceeded. Check Labelbox documentation to see API limits.
            labelbox.exceptions.TimeoutError: If response was not received
                in `timeout` seconds.
            labelbox.exceptions.NetworkError: If an unknown error occurred
                most likely due to connection issues.
            labelbox.exceptions.LabelboxError: If an unknown error of any
                kind occurred.
        """
        logger.debug("Query: %s, params: %r", query, params)

        # Convert datetimes to UTC strings.
        def convert_value(value):
            if isinstance(value, datetime):
                value = value.astimezone(timezone.utc)
                value = value.strftime("%Y-%m-%dT%H:%M:%SZ")
            return value

        if params is not None:
            params = {key: convert_value(value) for key, value in params.items()}

        data = json.dumps(
            {'query': query, 'variables': params}).encode('utf-8')

        try:
            response = requests.post(self.endpoint, data=data,
                                        headers=self.headers,
                                        timeout=timeout)
        except requests.exceptions.Timeout as e:
            raise labelbox.exceptions.TimeoutError(str(e))

        except requests.exceptions.RequestException as e:
            logger.error("Unknown error: %s", str(e))
            raise labelbox.exceptions.NetworkError(e)

        except Exception as e:
            logger.error("Unknown error: %s", str(e))
            raise labelbox.exceptions.LabelboxError(str(e))

        try:
            response = response.json()
        except:
            raise labelbox.exceptions.LabelboxError(
                "Failed to parse response as JSON: %s", response.text)

        errors = response.get("errors", [])

        def check_errors(keywords, *path):
            """ Helper that looks for any of the given `keywords` in any of
            current errors on paths (like error[path][component][to][keyword]).
            """
            for error in errors:
                obj = error
                for path_elem in path:
                    obj = obj.get(path_elem, {})
                if obj in keywords:
                    return error
            return None

        # Check for authentication error
        if check_errors(["AUTHENTICATION_ERROR"],
                        "extensions", "exception", "code") is not None:
            raise labelbox.exceptions.AuthenticationError("Invalid API key")

        # Check for query complexity error
        validation_error = check_errors(["GRAPHQL_VALIDATION_FAILED"],
                                        "extensions", "code")
        if validation_error is not None:
            raise labelbox.exceptions.ValidationFailedError(
                validation_error["message"])

        # Check for malformed GraphQL error
        graphql_error = check_errors(["GRAPHQL_PARSE_FAILED"], "extensions", "code")
        if graphql_error is not None:
            raise labelbox.exceptions.InvalidQueryError(
                graphql_error["message"])

        # Check if API limit was exceeded
        response_msg = response.get("message", "")
        if response_msg.startswith("You have exceeded"):
            raise labelbox.exceptions.ApiLimitError(response_msg)

        if len(errors) > 0:
            logging.warning("Unparsed errors on query execution: %r", errors)
            raise labelbox.exceptions.LabelboxError(
                "Unknown error: %s" % str(errors))

        return response

    def upload_data(self, data):
        """ Uploads the given data (bytes) to Labelbox.
        Args:
            data (bytes): the data to upload.
        Return:
            str, the URL of uploaded data.
        Raises:
            labelbox.exceptions.LabelboxError: if upload failes.
        """
        request_data = {
            "operations": json.dumps({
            "variables": {"file": None, "contentLength": len(data), "sign": False},
            "query": """mutation UploadFile($file: Upload!, $contentLength: Int!,
                                            $sign: Boolean) {
                            uploadFile(file: $file, contentLength: $contentLength,
                                       sign: $sign) {url filename} } """,}),
            "map": (None, json.dumps({"1": ["variables.file"]})),
            }
        request = requests.post(
            self.endpoint,
            headers={"authorization": "Bearer %s" % self.api_key},
            data=request_data,
            files={"1": data}
        )

        try:
            file_data = request.json().get("data", None)
        except ValueError: # response is not valid JSON
            raise labelbox.exceptions.LabelboxError(
                "Failed to upload, unknown cause")

        if not file_data or not file_data.get("uploadFile", None):
            raise labelbox.exceptions.LabelboxError(
                "Failed to upload, message: %s" % file_data.get("error", None))

        return file_data["uploadFile"]["url"]

    def get_single(self, db_object_type, uid):
        """ Fetches a single object of the given type, for the given ID.

        Args:
            db_object_type (type): DbObject subclass.
            uid (str): Unique ID of the row.
        Return:
            Object of `db_object_type`.
        Raises:
            labelbox.exceptions.ResourceNotFoundError: If there is no object
                of the given type for the given ID.
            labelbox.exceptions.LabelboxError: Any error raised by
                `Client.execute` can also be raised by this function.
        """
        query_str, params = query.get_single(db_object_type, uid)
        res = self.execute(query_str, params)["data"][
            utils.camel_case(db_object_type.type_name())]
        if res is None:
            raise labelbox.exceptions.ResourceNotFoundError(
                db_object_type, params)
        else:
            return db_object_type(self, res)

    def get_project(self, project_id):
        """ Convenience for `client.get_single(Project, project_id)`. """
        return self.get_single(Project, project_id)

    def get_dataset(self, dataset_id):
        """ Convenience for `client.get_single(Dataset, dataset_id)`. """
        return self.get_single(Dataset, dataset_id)

    def get_user(self):
        """ Gets the current user database object. """
        return self.get_single(User, None)

    def get_organization(self):
        """ Gets the organization DB object of the current user. """
        return self.get_single(Organization, None)

    def get_all(self, db_object_type, where):
        """ Fetches all the objects of the given type the user has access to.

        Args:
            db_object_type (type): DbObject subclass.
            where (Comparison, LogicalOperation or None): The `where` clause
                for filtering.
        Return:
            An iterable of `db_object_type` instances.
        Raises:
            labelbox.exceptions.LabelboxError: Any error raised by
                `Client.execute` can also be raised by this function.
        """
        not_deleted = db_object_type.deleted == False
        where = not_deleted if where is None else where & not_deleted
        query_str, params = query.get_all(db_object_type, where)
        return PaginatedCollection(
            self, query_str, params,
            [utils.camel_case(db_object_type.type_name()) + "s"],
            db_object_type)

    def get_projects(self, where=None):
        """ Fetches all the projects the user has access to.

        Args:
            where (Comparison, LogicalOperation or None): The `where` clause
                for filtering.
        Return:
            An iterable of Projects (typically a PaginatedCollection).
        Raises:
            labelbox.exceptions.LabelboxError: Any error raised by
                `Client.execute` can also be raised by this function.
        """
        return self.get_all(Project, where)

    def get_datasets(self, where=None):
        """ Fetches all the datasets the user has access to.

        Args:
            where (Comparison, LogicalOperation or None): The `where` clause
                for filtering.
        Return:
            An iterable of Datasets (typically a PaginatedCollection).
        Raises:
            labelbox.exceptions.LabelboxError: Any error raised by
                `Client.execute` can also be raised by this function.
        """
        return self.get_all(Dataset, where)

    def _create(self, db_object_type, data):
        """ Creates a object on the server. Attribute values are
            passed as keyword arguments:

        Args:
            db_object_type (type): A DbObjectType subtype.
            data (dict): Keys are attributes or their names (in Python,
                snake-case convention) and values are desired attribute values.
        Return:
            a new object of the given DB object type.
        Raises:
            InvalidAttributeError: in case the DB object type does not contain
                any of the attribute names given in `data`.
        """
        # Convert string attribute names to Field or Relationship objects.
        # Also convert Labelbox object values to their UIDs.
        data = {db_object_type.attribute(attr) if isinstance(attr, str) else attr:
                value.uid if isinstance(value, DbObject) else value
                for attr, value in data.items()}

        query_string, params = query.create(db_object_type, data)
        res = self.execute(query_string, params)
        res = res["data"]["create%s" % db_object_type.type_name()]
        return db_object_type(self, res)

    def create_dataset(self, **kwargs):
        """ Creates a Dataset object on the server. Attribute values are
            passed as keyword arguments:
                >>> dataset = client.create_dataset(name="MyDataset")

        Kwargs:
            Keyword arguments with new Dataset attribute values.
            Keys are attribute names (in Python, snake-case convention) and
            values are desired attribute values.
        Return:
            a new Dataset object.
        Raises:
            InvalidAttributeError: in case the Dataset type does not contain
                any of the field names given in kwargs.
        """
        return self._create(Dataset, kwargs)

    def create_project(self, **kwargs):
        """ Creates a Project object on the server. Attribute values are
            passed as keyword arguments:
                >>> project = client.create_project(name="MyProject")

        Kwargs:
            Keyword arguments with new Project attribute values.
            Keys are attribute names (in Python, snake-case convention) and
            values are desired attribute values.
        Return:
            a new Project object.
        Raises:
            InvalidAttributeError: in case the Project type does not contain
                any of the field names given in kwargs.
        """
        return self._create(Project, kwargs)
