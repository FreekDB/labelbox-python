from labelbox.data.serialization.labelbox_v1.converter import LBV1Converter
import json

payload = {
    'ID':
        'ckr2k3bq8fe2b0y7he4y25udy',
    'DataRow ID':
        'ckr083n0e196n0ydk4uyzapvn',
    'Labeled Data':
        'https://upload.wikimedia.org/wikipedia/commons/thumb/0/08/Kitano_Street_Kobe01s5s4110.jpg/2560px-Kitano_Street_Kobe01s5s4110.jpg',
    'Label': {
        'objects': [{
            'featureId':
                'ckr2k4hvi000a3h69dm0voem2',
            'schemaId':
                'ckr083qt78ie70yar0goy4trr',
            'color':
                '#ff0000',
            'title':
                'bounding_box',
            'value':
                'bounding_box',
            'bbox': {
                'top': 1333,
                'left': 965,
                'height': 186,
                'width': 594
            },
            'instanceURI':
                'https://api.labelbox.com/masks/feature/ckr2k4hvi000a3h69dm0voem2?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOiJja3FjeDFkMDMwNjg0MHk2MWJvd2I1anI1Iiwib3JnYW5pemF0aW9uSWQiOiJja3FjeDFjem4wNjgzMHk2MWdoOXYwMmNzIiwiaWF0IjoxNjI2MzAyNDk5LCJleHAiOjE2Mjg4OTQ0OTl9.bLY1gGt0MRxqG6BRVpmjlAp_a9WhcaZYq4Lnbz_lwxE'
        }, {
            'featureId':
                'ckr2k4lzj000d3h69hvowgptf',
            'schemaId':
                'ckr083qt78ie70yar0goy4trr',
            'color':
                '#ff0000',
            'title':
                'bounding_box',
            'value':
                'bounding_box',
            'bbox': {
                'top': 176,
                'left': 392,
                'height': 315,
                'width': 463
            },
            'instanceURI':
                'https://api.labelbox.com/masks/feature/ckr2k4lzj000d3h69hvowgptf?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOiJja3FjeDFkMDMwNjg0MHk2MWJvd2I1anI1Iiwib3JnYW5pemF0aW9uSWQiOiJja3FjeDFjem4wNjgzMHk2MWdoOXYwMmNzIiwiaWF0IjoxNjI2MzAyNDk5LCJleHAiOjE2Mjg4OTQ0OTl9.bLY1gGt0MRxqG6BRVpmjlAp_a9WhcaZYq4Lnbz_lwxE',
            'classifications': [{
                'featureId': 'ckr2k4onp000g3h692t93rrf1',
                'schemaId': 'ckr083sxf8iej0yardcg05ffq',
                'title': 'has_handbag',
                'value': 'has_handbag',
                'answer': {
                    'featureId': 'ckr2k4onp000f3h69skg29vqq',
                    'schemaId': 'ckr083u8g8ieo0yargphlg4dq',
                    'title': 'True',
                    'value': 'True'
                }
            }, {
                'featureId': 'ckr2k4q3z000i3h693eeexdgs',
                'schemaId': 'ckr2k38anf2z10y9f3my9bm8r',
                'title': 'nested1',
                'value': 'nested1',
                'answer': {
                    'featureId': 'ckr2k4q3z000h3h698n3lp5vf',
                    'schemaId': 'ckr2k38bdf2z30y9f66vmayf3',
                    'title': 'nested_op1',
                    'value': 'nested_op1'
                }
            }, {
                'featureId': 'ckr2k4rlq000k3h69eky8lmhj',
                'schemaId': 'ckr2k38byf2z70y9fhsqg3dhr',
                'title': 'super_nested_1',
                'value': 'super_nested_1',
                'answer': {
                    'featureId': 'ckr2k4rlq000j3h692slt7177',
                    'schemaId': 'ckr2k38cgf2z90y9f220554cl',
                    'title': 'super_nested_op1',
                    'value': 'super_nested_op1'
                }
            }, {
                'featureId': 'ckr2k4sr6000m3h69h9qyc8oa',
                'schemaId': 'ckr2k38d5f2zd0y9fgtfj3i22',
                'title': 'ultra_nested',
                'value': 'ultra_nested',
                'answer': {
                    'featureId': 'ckr2k4sr6000l3h6909bz8bnd',
                    'schemaId': 'ckr2k38dof2zf0y9fccbp7llu',
                    'title': 'ultra_nested_1',
                    'value': 'ultra_nested_1'
                }
            }, {
                'featureId': 'ckr2k4w4c000n3h69fkww7wy1',
                'schemaId': 'ckr2k38ehf2zh0y9f89fv7ce8',
                'title': 'forever_nested',
                'value': 'forever_nested',
                'answer': 'hmmm'
            }]
        }, {
            'featureId':
                'ckr2k50s4000p3h69i0u26pan',
            'schemaId':
                'ckr083qt78ie70yar0goy4trr',
            'color':
                '#ff0000',
            'title':
                'bounding_box',
            'value':
                'bounding_box',
            'bbox': {
                'top': 236,
                'left': 1152,
                'height': 193,
                'width': 415
            },
            'instanceURI':
                'https://api.labelbox.com/masks/feature/ckr2k50s4000p3h69i0u26pan?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOiJja3FjeDFkMDMwNjg0MHk2MWJvd2I1anI1Iiwib3JnYW5pemF0aW9uSWQiOiJja3FjeDFjem4wNjgzMHk2MWdoOXYwMmNzIiwiaWF0IjoxNjI2MzAyNDk5LCJleHAiOjE2Mjg4OTQ0OTl9.bLY1gGt0MRxqG6BRVpmjlAp_a9WhcaZYq4Lnbz_lwxE',
            'classifications': [{
                'featureId': 'ckr2k53i4000s3h69qzgn1n73',
                'schemaId': 'ckr083sxf8iej0yardcg05ffq',
                'title': 'has_handbag',
                'value': 'has_handbag',
                'answer': {
                    'featureId': 'ckr2k53i4000r3h69yo6v3ocf',
                    'schemaId': 'ckr083u8h8ieq0yar9gtddq0k',
                    'title': 'False',
                    'value': 'False'
                }
            }]
        }, {
            'featureId':
                'ckr2k55ty000u3h696xy6o7x0',
            'schemaId':
                'ckr083qt78ie70yar0goy4trr',
            'color':
                '#ff0000',
            'title':
                'bounding_box',
            'value':
                'bounding_box',
            'bbox': {
                'top': 619,
                'left': 749,
                'height': 240,
                'width': 317
            },
            'instanceURI':
                'https://api.labelbox.com/masks/feature/ckr2k55ty000u3h696xy6o7x0?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOiJja3FjeDFkMDMwNjg0MHk2MWJvd2I1anI1Iiwib3JnYW5pemF0aW9uSWQiOiJja3FjeDFjem4wNjgzMHk2MWdoOXYwMmNzIiwiaWF0IjoxNjI2MzAyNDk5LCJleHAiOjE2Mjg4OTQ0OTl9.bLY1gGt0MRxqG6BRVpmjlAp_a9WhcaZYq4Lnbz_lwxE',
            'classifications': [{
                'featureId': 'ckr2k58fs000x3h69umbjow14',
                'schemaId': 'ckr083sxf8iej0yardcg05ffq',
                'title': 'has_handbag',
                'value': 'has_handbag',
                'answer': {
                    'featureId': 'ckr2k59mb000y3h69h89rqurm',
                    'schemaId': 'ckr083u8g8ieo0yargphlg4dq',
                    'title': 'True',
                    'value': 'True'
                }
            }, {
                'featureId': 'ckr2k5bfk00103h69ibq3cpas',
                'schemaId': 'ckr2k38anf2z10y9f3my9bm8r',
                'title': 'nested1',
                'value': 'nested1',
                'answer': {
                    'featureId': 'ckr2k5bfk000z3h69lvv4rolv',
                    'schemaId': 'ckr2k38bef2z50y9feroo2dfm',
                    'title': 'nested_op2',
                    'value': 'nested_op2'
                }
            }]
        }, {
            'featureId':
                'ckr2k459500063h69uiumklz0',
            'schemaId':
                'ckr2k3898f2yq0y9ffrwyghm1',
            'color':
                '#FF34FF',
            'title':
                'segmentation',
            'value':
                'segmentation',
            'instanceURI':
                'https://api.labelbox.com/masks/feature/ckr2k459500063h69uiumklz0?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOiJja3FjeDFkMDMwNjg0MHk2MWJvd2I1anI1Iiwib3JnYW5pemF0aW9uSWQiOiJja3FjeDFjem4wNjgzMHk2MWdoOXYwMmNzIiwiaWF0IjoxNjI2MzAyNDk5LCJleHAiOjE2Mjg4OTQ0OTl9.bLY1gGt0MRxqG6BRVpmjlAp_a9WhcaZYq4Lnbz_lwxE'
        }, {
            'featureId':
                'ckr2k3v6d00043h69s3psq0oy',
            'schemaId':
                'ckr2k3899f2ys0y9feg0zeatk',
            'color':
                '#FF4A46',
            'title':
                'polygon',
            'value':
                'polygon',
            'polygon': [{
                'x': 1450.321,
                'y': 523.608
            }, {
                'x': 1164.034,
                'y': 920.127
            }, {
                'x': 1712.112,
                'y': 868.074
            }, {
                'x': 1428.887,
                'y': 814.49
            }, {
                'x': 1611.07,
                'y': 659.863
            }],
            'instanceURI':
                'https://api.labelbox.com/masks/feature/ckr2k3v6d00043h69s3psq0oy?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOiJja3FjeDFkMDMwNjg0MHk2MWJvd2I1anI1Iiwib3JnYW5pemF0aW9uSWQiOiJja3FjeDFjem4wNjgzMHk2MWdoOXYwMmNzIiwiaWF0IjoxNjI2MzAyNDk5LCJleHAiOjE2Mjg4OTQ0OTl9.bLY1gGt0MRxqG6BRVpmjlAp_a9WhcaZYq4Lnbz_lwxE'
        }, {
            'featureId':
                'ckr2k3zy300053h69wtr5q1c8',
            'schemaId':
                'ckr2k3899f2ys0y9feg0zeatk',
            'color':
                '#FF4A46',
            'title':
                'polygon',
            'value':
                'polygon',
            'polygon': [{
                'x': 1332.438,
                'y': 1244.691
            }, {
                'x': 1803.969,
                'y': 1175.797
            }, {
                'x': 1748.855,
                'y': 1241.629
            }],
            'instanceURI':
                'https://api.labelbox.com/masks/feature/ckr2k3zy300053h69wtr5q1c8?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOiJja3FjeDFkMDMwNjg0MHk2MWJvd2I1anI1Iiwib3JnYW5pemF0aW9uSWQiOiJja3FjeDFjem4wNjgzMHk2MWdoOXYwMmNzIiwiaWF0IjoxNjI2MzAyNDk5LCJleHAiOjE2Mjg4OTQ0OTl9.bLY1gGt0MRxqG6BRVpmjlAp_a9WhcaZYq4Lnbz_lwxE'
        }, {
            'featureId':
                'ckr2k3ti600033h697k4f5q4y',
            'schemaId':
                'ckr2k3899f2yu0y9fh5a98m80',
            'color':
                '#008941',
            'title':
                'point',
            'value':
                'point',
            'point': {
                'x': 660.353,
                'y': 140.867
            },
            'instanceURI':
                'https://api.labelbox.com/masks/feature/ckr2k3ti600033h697k4f5q4y?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOiJja3FjeDFkMDMwNjg0MHk2MWJvd2I1anI1Iiwib3JnYW5pemF0aW9uSWQiOiJja3FjeDFjem4wNjgzMHk2MWdoOXYwMmNzIiwiaWF0IjoxNjI2MzAyNDk5LCJleHAiOjE2Mjg4OTQ0OTl9.bLY1gGt0MRxqG6BRVpmjlAp_a9WhcaZYq4Lnbz_lwxE'
        }, {
            'featureId':
                'ckr2k3h9t00003h69gdr7eb8p',
            'schemaId':
                'ckr2k3899f2yw0y9fb953bdtj',
            'color':
                '#006FA6',
            'title':
                'polyline',
            'value':
                'polyline',
            'line': [{
                'x': 245.467,
                'y': 134.743
            }, {
                'x': 263.838,
                'y': 1289.089
            }, {
                'x': 464.392,
                'y': 131.681
            }, {
                'x': 352.633,
                'y': 297.025
            }, {
                'x': 340.386,
                'y': 678.235
            }, {
                'x': 312.829,
                'y': 812.959
            }],
            'instanceURI':
                'https://api.labelbox.com/masks/feature/ckr2k3h9t00003h69gdr7eb8p?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOiJja3FjeDFkMDMwNjg0MHk2MWJvd2I1anI1Iiwib3JnYW5pemF0aW9uSWQiOiJja3FjeDFjem4wNjgzMHk2MWdoOXYwMmNzIiwiaWF0IjoxNjI2MzAyNDk5LCJleHAiOjE2Mjg4OTQ0OTl9.bLY1gGt0MRxqG6BRVpmjlAp_a9WhcaZYq4Lnbz_lwxE'
        }, {
            'featureId':
                'ckr2k3px700013h69op6o240s',
            'schemaId':
                'ckr2k3899f2yw0y9fb953bdtj',
            'color':
                '#006FA6',
            'title':
                'polyline',
            'value':
                'polyline',
            'line': [{
                'x': 309.767,
                'y': 1544.759
            }, {
                'x': 395.5,
                'y': 1165.081
            }],
            'instanceURI':
                'https://api.labelbox.com/masks/feature/ckr2k3px700013h69op6o240s?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOiJja3FjeDFkMDMwNjg0MHk2MWJvd2I1anI1Iiwib3JnYW5pemF0aW9uSWQiOiJja3FjeDFjem4wNjgzMHk2MWdoOXYwMmNzIiwiaWF0IjoxNjI2MzAyNDk5LCJleHAiOjE2Mjg4OTQ0OTl9.bLY1gGt0MRxqG6BRVpmjlAp_a9WhcaZYq4Lnbz_lwxE'
        }],
        'classifications': []
    },
    'Created By':
        'msokoloff+11@labelbox.com',
    'Project Name':
        'subclass_mal_project',
    'Created At':
        '2021-07-13T21:19:39.000Z',
    'Updated At':
        '2021-07-13T21:19:39.946Z',
    'Seconds to Label':
        150.908,
    'External ID':
        None,
    'Agreement':
        -1,
    'Benchmark Agreement':
        -1,
    'Benchmark ID':
        None,
    'Dataset Name':
        'subclass_mal_dataset',
    'Reviews': [],
    'View Label':
        'https://editor.labelbox.com?project=ckr083gl1dr8j0yag4jo5cnnt&label=ckr2k3bq8fe2b0y7he4y25udy',
    'Has Open Issues':
        0,
    'Skipped':
        False
}

def test_image():
    collection = LBV1Converter.deserialize([payload])
    serialized = next(LBV1Converter.serialize(collection, None))

    assert serialized.keys() == payload.keys()
    for key in serialized:
        if key != 'Label':
            assert serialized[key] == payload[key]
        elif key == 'Label':
            for annotation_a, annotation_b in zip(serialized[key]['objects'],
                                                payload[key]['objects']):
                if not len(annotation_a['classifications']):
                    # We don't add a classification key to the payload if there is no classifications.
                    annotation_a.pop('classifications')
                assert annotation_a == annotation_b
