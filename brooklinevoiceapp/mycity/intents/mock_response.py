import json

mock_home = json.loads('{"x": -7917110.6406735824, "y": 5211147.4714696482}')

mock_features = json.loads("""
   [
        {
            "attributes": {
                "OBJECTID": 437,
                "FACILITYID": null,
                "NAME": "BROOKLINE AVE",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Brookline",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "65",
                "DESCRIPT": "OUTBOUND: KENMORE - BRIGHTON",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7916116.5740525108,
                "y": 5211282.8205066817
            }
        },
        {
            "attributes": {
                "OBJECTID": 438,
                "FACILITYID": null,
                "NAME": "WASHINGTON ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Brookline",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "65",
                "DESCRIPT": "OUTBOUND: KENMORE - BRIGHTON",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7917388.8962022979,
                "y": 5211260.8579029068
            }
        },
        {
            "attributes": {
                "OBJECTID": 439,
                "FACILITYID": null,
                "NAME": "WASHINGTON ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Brookline",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "65",
                "DESCRIPT": "OUTBOUND: KENMORE - BRIGHTON",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7917922.0899542468,
                "y": 5211785.5640802803
            }
        },
        {
            "attributes": {
                "OBJECTID": 440,
                "FACILITYID": null,
                "NAME": "WASHINGTON ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Brookline",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "65",
                "DESCRIPT": "OUTBOUND: KENMORE - BRIGHTON",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7919070.1567182811,
                "y": 5212246.819561962
            }
        },
        {
            "attributes": {
                "OBJECTID": 441,
                "FACILITYID": null,
                "NAME": "WASHINGTON ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Brookline",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "65",
                "DESCRIPT": "OUTBOUND: KENMORE - BRIGHTON",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7918296.9662187658,
                "y": 5211809.2255833801
            }
        },
        {
            "attributes": {
                "OBJECTID": 442,
                "FACILITYID": null,
                "NAME": "WASHINGTON ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Brookline",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "65",
                "DESCRIPT": "OUTBOUND: KENMORE - BRIGHTON",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7918666.5375123555,
                "y": 5211900.8213977618
            }
        },
        {
            "attributes": {
                "OBJECTID": 443,
                "FACILITYID": null,
                "NAME": "WASHINGTON ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Brookline",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "65",
                "DESCRIPT": "INBOUND: BRIGHTON - KENMORE",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7919058.3907241272,
                "y": 5212211.5234905044
            }
        },
        {
            "attributes": {
                "OBJECTID": 444,
                "FACILITYID": null,
                "NAME": "WASHINGTON ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Brookline",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "65",
                "DESCRIPT": "INBOUND: BRIGHTON - KENMORE",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7918813.521635293,
                "y": 5211988.9348047981
            }
        },
        {
            "attributes": {
                "OBJECTID": 445,
                "FACILITYID": null,
                "NAME": "WASHINGTON ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Brookline",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "65",
                "DESCRIPT": "INBOUND: BRIGHTON - KENMORE",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7918594.6766777746,
                "y": 5211841.9807277918
            }
        },
        {
            "attributes": {
                "OBJECTID": 446,
                "FACILITYID": null,
                "NAME": "WASHINGTON ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Brookline",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "65",
                "DESCRIPT": "INBOUND: BRIGHTON - KENMORE",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7917703.2139701443,
                "y": 5211506.4285576921
            }
        },
        {
            "attributes": {
                "OBJECTID": 447,
                "FACILITYID": null,
                "NAME": "WASHINGTON ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Brookline",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "65",
                "DESCRIPT": "INBOUND: BRIGHTON - KENMORE",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7918083.1770421965,
                "y": 5211800.7429413358
            }
        },
        {
            "attributes": {
                "OBJECTID": 448,
                "FACILITYID": null,
                "NAME": "WASHINGTON ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Brookline",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "65",
                "DESCRIPT": "INBOUND: BRIGHTON - KENMORE",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7918351.5810992941,
                "y": 5211794.9866457339
            }
        },
        {
            "attributes": {
                "OBJECTID": 449,
                "FACILITYID": null,
                "NAME": "WASHINGTON ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Brookline",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "65",
                "DESCRIPT": "INBOUND: BRIGHTON - KENMORE",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7917588.5725994026,
                "y": 5211339.1484495867
            }
        },
        {
            "attributes": {
                "OBJECTID": 450,
                "FACILITYID": null,
                "NAME": "WASHINGTON ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Brookline",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "65",
                "DESCRIPT": "INBOUND: BRIGHTON - KENMORE",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7916932.9780555777,
                "y": 5210996.0834494289
            }
        },
        {
            "attributes": {
                "OBJECTID": 451,
                "FACILITYID": null,
                "NAME": "BROOKLINE AVE",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Brookline",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "65",
                "DESCRIPT": "INBOUND: BRIGHTON - KENMORE",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7916412.5757887736,
                "y": 5210854.9738585725
            }
        },
        {
            "attributes": {
                "OBJECTID": 452,
                "FACILITYID": null,
                "NAME": "BROOKLINE AVE",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Brookline",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "65",
                "DESCRIPT": "INBOUND: BRIGHTON - KENMORE",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7916266.897172153,
                "y": 5211041.5307694599
            }
        },
        {
            "attributes": {
                "OBJECTID": 453,
                "FACILITYID": null,
                "NAME": "380 ft East of River Rd",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Brookline",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "65",
                "DESCRIPT": "INBOUND: BRIGHTON - KENMORE",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7916092.2665862469,
                "y": 5211250.9272010839
            }
        },
        {
            "attributes": {
                "OBJECTID": 454,
                "FACILITYID": null,
                "NAME": "WASHINGTON ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Brookline",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "65",
                "DESCRIPT": "INBOUND: BRIGHTON - KENMORE",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7916900.6350542419,
                "y": 5210937.7265734589
            }
        },
        {
            "attributes": {
                "OBJECTID": 455,
                "FACILITYID": null,
                "NAME": "BROOKLINE AVE",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Brookline",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "65",
                "DESCRIPT": "OUTBOUND: KENMORE - BRIGHTON",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7916357.4837671593,
                "y": 5210975.2366243564
            }
        },
        {
            "attributes": {
                "OBJECTID": 456,
                "FACILITYID": null,
                "NAME": "BROOKLINE AVE",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Brookline",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "65",
                "DESCRIPT": "OUTBOUND: KENMORE - BRIGHTON",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7916262.8875933122,
                "y": 5211095.9494195785
            }
        },
        {
            "attributes": {
                "OBJECTID": 457,
                "FACILITYID": null,
                "NAME": "HARVARD ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Brookline",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "66",
                "DESCRIPT": "OUTBOUND: DUDLEY - ALLSTON",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7917156.9742489029,
                "y": 5212325.2698437134
            }
        },
        {
            "attributes": {
                "OBJECTID": 458,
                "FACILITYID": null,
                "NAME": "BABCOCK ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Brookline",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "66",
                "DESCRIPT": "OUTBOUND: DUDLEY - ALLSTON",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7917422.559066412,
                "y": 5212584.7476538299
            }
        },
        {
            "attributes": {
                "OBJECTID": 459,
                "FACILITYID": null,
                "NAME": "HARVARD ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Brookline",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "66",
                "DESCRIPT": "OUTBOUND: DUDLEY - ALLSTON",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7917844.3775026482,
                "y": 5212889.1229320681
            }
        },
        {
            "attributes": {
                "OBJECTID": 460,
                "FACILITYID": null,
                "NAME": "HARVARD ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Brookline",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "66",
                "DESCRIPT": "OUTBOUND: DUDLEY - ALLSTON",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7917945.3950788863,
                "y": 5213036.9377676947
            }
        },
        {
            "attributes": {
                "OBJECTID": 461,
                "FACILITYID": null,
                "NAME": "HARVARD ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Brookline",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "66",
                "DESCRIPT": "OUTBOUND: DUDLEY - ALLSTON",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7918059.5784736369,
                "y": 5213276.9214660916
            }
        },
        {
            "attributes": {
                "OBJECTID": 462,
                "FACILITYID": null,
                "NAME": "HARVARD ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Brookline",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "66",
                "DESCRIPT": "OUTBOUND: DUDLEY - ALLSTON",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7916961.960673376,
                "y": 5211291.1103441529
            }
        },
        {
            "attributes": {
                "OBJECTID": 463,
                "FACILITYID": null,
                "NAME": "HARVARD ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Brookline",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "66",
                "DESCRIPT": "OUTBOUND: DUDLEY - ALLSTON",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7917112.2207282567,
                "y": 5211475.1968937051
            }
        },
        {
            "attributes": {
                "OBJECTID": 464,
                "FACILITYID": null,
                "NAME": "HARVARD ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Brookline",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "66",
                "DESCRIPT": "OUTBOUND: DUDLEY - ALLSTON",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7917195.0602085395,
                "y": 5211644.3215244375
            }
        },
        {
            "attributes": {
                "OBJECTID": 465,
                "FACILITYID": null,
                "NAME": "HARVARD ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Brookline",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "66",
                "DESCRIPT": "OUTBOUND: DUDLEY - ALLSTON",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7917164.4202661496,
                "y": 5211886.9096538899
            }
        },
        {
            "attributes": {
                "OBJECTID": 466,
                "FACILITYID": null,
                "NAME": "HARVARD ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Brookline",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "66",
                "DESCRIPT": "OUTBOUND: DUDLEY - ALLSTON",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7917694.1565356487,
                "y": 5212778.3444362348
            }
        },
        {
            "attributes": {
                "OBJECTID": 467,
                "FACILITYID": null,
                "NAME": "WASHINGTON ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Brookline",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "65",
                "DESCRIPT": "INBOUND: BRIGHTON - KENMORE",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7916778.4799945243,
                "y": 5210712.2558378065
            }
        },
        {
            "attributes": {
                "OBJECTID": 468,
                "FACILITYID": null,
                "NAME": "WASHINGTON ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Brookline",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "66",
                "DESCRIPT": "INBOUND: ALLSTON - DUDLEY",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7916777.1469317377,
                "y": 5210711.9365432048
            }
        },
        {
            "attributes": {
                "OBJECTID": 469,
                "FACILITYID": null,
                "NAME": "WASHINGTON ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Brookline",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "65",
                "DESCRIPT": "INBOUND: BRIGHTON - KENMORE",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7917358.0866269423,
                "y": 5211220.6648570271
            }
        },
        {
            "attributes": {
                "OBJECTID": 470,
                "FACILITYID": null,
                "NAME": "WASHINGTON ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Brookline",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "65",
                "DESCRIPT": "OUTBOUND: KENMORE - BRIGHTON",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7917573.8105988819,
                "y": 5211356.8849814767
            }
        },
        {
            "attributes": {
                "OBJECTID": 471,
                "FACILITYID": null,
                "NAME": "WASHINGTON ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Brookline",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "65",
                "DESCRIPT": "OUTBOUND: KENMORE - BRIGHTON",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7917708.8436840037,
                "y": 5211554.1815390578
            }
        },
        {
            "attributes": {
                "OBJECTID": 472,
                "FACILITYID": null,
                "NAME": "WASHINGTON ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Brookline",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "65",
                "DESCRIPT": "OUTBOUND: KENMORE - BRIGHTON",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7916939.7679861849,
                "y": 5211031.6531504169
            }
        },
        {
            "attributes": {
                "OBJECTID": 473,
                "FACILITYID": null,
                "NAME": "BOYLSTON ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Brookline",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "60",
                "DESCRIPT": "OUTBOUND:KENMORE-CHESTNUT HILL",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7922170.2020038301,
                "y": 5209519.6493102703
            }
        },
        {
            "attributes": {
                "OBJECTID": 474,
                "FACILITYID": null,
                "NAME": "BOYLSTON ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Brookline",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "60",
                "DESCRIPT": "INBOUND:CHESTNUT HILL-KENMORE",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7921025.1751233842,
                "y": 5209835.9012392908
            }
        },
        {
            "attributes": {
                "OBJECTID": 475,
                "FACILITYID": null,
                "NAME": "BOYLSTON ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Brookline",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "60",
                "DESCRIPT": "INBOUND:CHESTNUT HILL-KENMORE",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7917994.3830591049,
                "y": 5210468.7490852559
            }
        },
        {
            "attributes": {
                "OBJECTID": 476,
                "FACILITYID": null,
                "NAME": " ",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Brookline",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "65 ",
                "DESCRIPT": "OUTBOUND: KENMORE - BRIGHTON",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7916602.6126764268,
                "y": 5210836.7513533114
            }
        },
        {
            "attributes": {
                "OBJECTID": 477,
                "FACILITYID": null,
                "NAME": "CHESTNUT HILL AVE",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Brookline",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "51",
                "DESCRIPT": " ",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7920256.914389668,
                "y": 5211296.3687759284
            }
        },
        {
            "attributes": {
                "OBJECTID": 478,
                "FACILITYID": null,
                "NAME": "CHESTNUT HILL AVE",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Brookline",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "51",
                "DESCRIPT": "INBOUND:CLEVLAND CL-FOREST HIL",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7920024.3471633932,
                "y": 5210880.3250879999
            }
        },
        {
            "attributes": {
                "OBJECTID": 479,
                "FACILITYID": null,
                "NAME": "CHESTNUT HILL AVE",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Brookline",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "51",
                "DESCRIPT": "INBOUND:CLEVLAND CL-FOREST HIL",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7919944.2047488503,
                "y": 5210539.5699097579
            }
        },
        {
            "attributes": {
                "OBJECTID": 480,
                "FACILITYID": null,
                "NAME": "GROVE ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Brookline",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "51",
                "DESCRIPT": "INBOUND:CLEVLAND CL-FOREST HIL",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7920437.3143127123,
                "y": 5206653.6612877762
            }
        },
        {
            "attributes": {
                "OBJECTID": 481,
                "FACILITYID": null,
                "NAME": "GROVE ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Brookline",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "51",
                "DESCRIPT": "INBOUND:CLEVLAND CL-FOREST HIL",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7920854.189785894,
                "y": 5206185.5591881201
            }
        },
        {
            "attributes": {
                "OBJECTID": 482,
                "FACILITYID": null,
                "NAME": "GROVE ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Brookline",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "51",
                "DESCRIPT": "INBOUND:CLEVLAND CL-FOREST HIL",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7920970.2206588192,
                "y": 5206047.1999251274
            }
        },
        {
            "attributes": {
                "OBJECTID": 483,
                "FACILITYID": null,
                "NAME": "GROVE ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Brookline",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "51",
                "DESCRIPT": "INBOUND:CLEVLAND CL-FOREST HIL",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7921162.7716419306,
                "y": 5205765.9858286669
            }
        },
        {
            "attributes": {
                "OBJECTID": 484,
                "FACILITYID": null,
                "NAME": "GROVE ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Brookline",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "51",
                "DESCRIPT": "OUTBOUND:FOREST HILL-CLEVELAND",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7921141.5322892983,
                "y": 5205750.0962478062
            }
        },
        {
            "attributes": {
                "OBJECTID": 485,
                "FACILITYID": null,
                "NAME": "GROVE ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Brookline",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "51",
                "DESCRIPT": "OUTBOUND:FOREST HILL-CLEVELAND",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7920951.2364427196,
                "y": 5206029.1452992884
            }
        },
        {
            "attributes": {
                "OBJECTID": 486,
                "FACILITYID": null,
                "NAME": "GROVE ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Brookline",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "51",
                "DESCRIPT": "OUTBOUND:FOREST HILL-CLEVELAND",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7920795.2808806458,
                "y": 5206217.1936507355
            }
        },
        {
            "attributes": {
                "OBJECTID": 487,
                "FACILITYID": null,
                "NAME": "CHESTNUT HILL AVE",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Brookline",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "51",
                "DESCRIPT": "OUTBOUND:FOREST HILL-CLEVELAND",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7919921.2948711114,
                "y": 5210552.6771192923
            }
        },
        {
            "attributes": {
                "OBJECTID": 488,
                "FACILITYID": null,
                "NAME": "CHESTNUT HILL AVE",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Brookline",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "51",
                "DESCRIPT": "OUTBOUND:FOREST HILL-CLEVELAND",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7920009.5403915225,
                "y": 5210906.1247998457
            }
        },
        {
            "attributes": {
                "OBJECTID": 489,
                "FACILITYID": null,
                "NAME": "CYPRESS ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Brookline",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "60",
                "DESCRIPT": "INBOUND:CHESTNUT HILL-KENMORE",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7917728.3349934081,
                "y": 5210435.6675837832
            }
        },
        {
            "attributes": {
                "OBJECTID": 490,
                "FACILITYID": null,
                "NAME": "CYPRESS ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Brookline",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "60",
                "DESCRIPT": "INBOUND:CHESTNUT HILL-KENMORE",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7917482.059360059,
                "y": 5210046.272364825
            }
        },
        {
            "attributes": {
                "OBJECTID": 491,
                "FACILITYID": null,
                "NAME": "HIGH ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Brookline",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "60",
                "DESCRIPT": "INBOUND:CHESTNUT HILL-KENMORE",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7917065.9381137248,
                "y": 5209936.7921426762
            }
        },
        {
            "attributes": {
                "OBJECTID": 492,
                "FACILITYID": null,
                "NAME": "HIGH ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Brookline",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "60",
                "DESCRIPT": "INBOUND:CHESTNUT HILL-KENMORE",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7916947.4473972032,
                "y": 5210211.8519482324
            }
        },
        {
            "attributes": {
                "OBJECTID": 493,
                "FACILITYID": null,
                "NAME": "BOYLSTON ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Brookline",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "60",
                "DESCRIPT": "INBOUND:CHESTNUT HILL-KENMORE",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7916662.0780981136,
                "y": 5210773.5910743512
            }
        },
        {
            "attributes": {
                "OBJECTID": 494,
                "FACILITYID": null,
                "NAME": "HIGH ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Brookline",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "60",
                "DESCRIPT": "OUTBOUND:KENMORE-CHESTNUT HILL",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7916975.5215685787,
                "y": 5210180.8547750721
            }
        },
        {
            "attributes": {
                "OBJECTID": 495,
                "FACILITYID": null,
                "NAME": "HIGH ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Brookline",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "60",
                "DESCRIPT": "OUTBOUND:KENMORE-CHESTNUT HILL",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7917057.2099315422,
                "y": 5209995.4181540292
            }
        },
        {
            "attributes": {
                "OBJECTID": 496,
                "FACILITYID": null,
                "NAME": "CYPRESS ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Brookline",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "60",
                "DESCRIPT": "INBOUND:CHESTNUT HILL-KENMORE",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7917299.1081790496,
                "y": 5209870.4825491132
            }
        },
        {
            "attributes": {
                "OBJECTID": 497,
                "FACILITYID": null,
                "NAME": "CYPRESS ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Brookline",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "60",
                "DESCRIPT": "OUTBOUND:KENMORE-CHESTNUT HILL",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7917252.5790137947,
                "y": 5209860.1133351037
            }
        },
        {
            "attributes": {
                "OBJECTID": 498,
                "FACILITYID": null,
                "NAME": "CYPRESS ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Brookline",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "60",
                "DESCRIPT": "OUTBOUND:KENMORE-CHESTNUT HILL",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7917483.5248498768,
                "y": 5210089.8853280256
            }
        },
        {
            "attributes": {
                "OBJECTID": 499,
                "FACILITYID": null,
                "NAME": "CYPRESS ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Brookline",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "60",
                "DESCRIPT": "OUTBOUND:KENMORE-CHESTNUT HILL",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7917683.7947014263,
                "y": 5210306.495442125
            }
        },
        {
            "attributes": {
                "OBJECTID": 500,
                "FACILITYID": null,
                "NAME": "CYPRESS ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Brookline",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "60",
                "DESCRIPT": "INBOUND:CHESTNUT HILL-KENMORE",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7917702.4327361276,
                "y": 5210296.4148655357
            }
        },
        {
            "attributes": {
                "OBJECTID": 501,
                "FACILITYID": null,
                "NAME": "BOYLSTON ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Brookline",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "60",
                "DESCRIPT": "OUTBOUND:KENMORE-CHESTNUT HILL",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7917983.132082046,
                "y": 5210501.6658141399
            }
        },
        {
            "attributes": {
                "OBJECTID": 502,
                "FACILITYID": null,
                "NAME": "150 ft West of Tully St",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Brookline",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "60",
                "DESCRIPT": " ",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7922380.1643504603,
                "y": 5209376.9805363938
            }
        },
        {
            "attributes": {
                "OBJECTID": 503,
                "FACILITYID": null,
                "NAME": "BOYLSTON ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Brookline",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "60",
                "DESCRIPT": " ",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7922487.7279737284,
                "y": 5209402.9456276717
            }
        },
        {
            "attributes": {
                "OBJECTID": 504,
                "FACILITYID": null,
                "NAME": "BOYLSTON ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Brookline",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "60",
                "DESCRIPT": "OUTBOUND:KENMORE-CHESTNUT HILL",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7922332.9237530008,
                "y": 5209461.1856080433
            }
        },
        {
            "attributes": {
                "OBJECTID": 505,
                "FACILITYID": null,
                "NAME": "BOYLSTON ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Brookline",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "60",
                "DESCRIPT": "INBOUND:CHESTNUT HILL-KENMORE",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7921950.6350193266,
                "y": 5209530.6630706508
            }
        },
        {
            "attributes": {
                "OBJECTID": 506,
                "FACILITYID": null,
                "NAME": "BOYLSTON ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Brookline",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "60",
                "DESCRIPT": "OUTBOUND:KENMORE-CHESTNUT HILL",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7921914.9196495945,
                "y": 5209586.8861131454
            }
        },
        {
            "attributes": {
                "OBJECTID": 507,
                "FACILITYID": null,
                "NAME": "BOYLSTON ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Brookline",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "60",
                "DESCRIPT": "INBOUND:CHESTNUT HILL-KENMORE",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7921442.179380171,
                "y": 5209701.8827735344
            }
        },
        {
            "attributes": {
                "OBJECTID": 508,
                "FACILITYID": null,
                "NAME": "BOYLSTON ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Brookline",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "60",
                "DESCRIPT": "OUTBOUND:KENMORE-CHESTNUT HILL",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7921442.7542354865,
                "y": 5209740.0382322837
            }
        },
        {
            "attributes": {
                "OBJECTID": 509,
                "FACILITYID": null,
                "NAME": "BOYLSTON ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Brookline",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "60",
                "DESCRIPT": "OUTBOUND:KENMORE-CHESTNUT HILL",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7921030.9104730356,
                "y": 5209877.3874715064
            }
        },
        {
            "attributes": {
                "OBJECTID": 510,
                "FACILITYID": null,
                "NAME": "BOYLSTON ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Brookline",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "60",
                "DESCRIPT": "OUTBOUND:KENMORE-CHESTNUT HILL",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7920394.053662085,
                "y": 5210060.7857688321
            }
        },
        {
            "attributes": {
                "OBJECTID": 511,
                "FACILITYID": null,
                "NAME": "BOYLSTON ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Brookline",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "60",
                "DESCRIPT": "INBOUND:CHESTNUT HILL-KENMORE",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7920243.6259864671,
                "y": 5210012.2381974999
            }
        },
        {
            "attributes": {
                "OBJECTID": 512,
                "FACILITYID": null,
                "NAME": "BOYLSTON ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Brookline",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "60",
                "DESCRIPT": "OUTBOUND:KENMORE-CHESTNUT HILL",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7920124.1401324412,
                "y": 5210036.9649965391
            }
        },
        {
            "attributes": {
                "OBJECTID": 513,
                "FACILITYID": null,
                "NAME": "BOYLSTON ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Brookline",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "60",
                "DESCRIPT": "INBOUND:CHESTNUT HILL-KENMORE",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7919845.7091519274,
                "y": 5209985.6110027498
            }
        },
        {
            "attributes": {
                "OBJECTID": 514,
                "FACILITYID": null,
                "NAME": "BOYLSTON ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Brookline",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "60",
                "DESCRIPT": "OUTBOUND:KENMORE-CHESTNUT HILL",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7919862.4610082358,
                "y": 5210017.9078585785
            }
        },
        {
            "attributes": {
                "OBJECTID": 515,
                "FACILITYID": null,
                "NAME": "BOYLSTON ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Brookline",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "51",
                "DESCRIPT": "INBOUND:CLEVLAND CL-FOREST HIL",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7919646.4040721906,
                "y": 5210049.83018272
            }
        },
        {
            "attributes": {
                "OBJECTID": 516,
                "FACILITYID": null,
                "NAME": "BOYLSTON ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Brookline",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "60",
                "DESCRIPT": "INBOUND:CHESTNUT HILL-KENMORE",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7919611.4773162482,
                "y": 5209980.0941537954
            }
        },
        {
            "attributes": {
                "OBJECTID": 517,
                "FACILITYID": null,
                "NAME": "CHESTNUT HILL AVE",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Brookline",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "51",
                "DESCRIPT": "OUTBOUND:FOREST HILL-CLEVELAND",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7919595.0461513894,
                "y": 5210064.2531568604
            }
        },
        {
            "attributes": {
                "OBJECTID": 518,
                "FACILITYID": null,
                "NAME": "LEE ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Brookline",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "51",
                "DESCRIPT": "INBOUND:CLEVLAND CL-FOREST HIL",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7919359.6170334741,
                "y": 5209943.9218442077
            }
        },
        {
            "attributes": {
                "OBJECTID": 519,
                "FACILITYID": null,
                "NAME": "LEE ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Brookline",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "51",
                "DESCRIPT": "OUTBOUND:FOREST HILL-CLEVELAND",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7919323.978154581,
                "y": 5209964.8555953624
            }
        },
        {
            "attributes": {
                "OBJECTID": 520,
                "FACILITYID": null,
                "NAME": "LEE ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Brookline",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "51",
                "DESCRIPT": "OUTBOUND:FOREST HILL-CLEVELAND",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7919068.6734717954,
                "y": 5209385.14466256
            }
        },
        {
            "attributes": {
                "OBJECTID": 521,
                "FACILITYID": null,
                "NAME": "LEE ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Brookline",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "51",
                "DESCRIPT": "OUTBOUND:FOREST HILL-CLEVELAND",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7919343.5682873689,
                "y": 5208777.2436786499
            }
        },
        {
            "attributes": {
                "OBJECTID": 522,
                "FACILITYID": null,
                "NAME": "CLYDE ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Brookline",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "51",
                "DESCRIPT": "OUTBOUND:FOREST HILL-CLEVELAND",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7919495.8999787373,
                "y": 5208204.3653681288
            }
        },
        {
            "attributes": {
                "OBJECTID": 523,
                "FACILITYID": null,
                "NAME": "LEE ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Brookline",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "51",
                "DESCRIPT": "INBOUND:CLEVLAND CL-FOREST HIL",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7919526.453759551,
                "y": 5208202.1941776117
            }
        },
        {
            "attributes": {
                "OBJECTID": 524,
                "FACILITYID": null,
                "NAME": "CLYDE ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Brookline",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "51",
                "DESCRIPT": "INBOUND:CLEVLAND CL-FOREST HIL",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7919554.1948926849,
                "y": 5207728.029515571
            }
        },
        {
            "attributes": {
                "OBJECTID": 525,
                "FACILITYID": null,
                "NAME": "CLYDE ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Brookline",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "51",
                "DESCRIPT": "OUTBOUND:FOREST HILL-CLEVELAND",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7919525.6589396382,
                "y": 5207732.3161829002
            }
        },
        {
            "attributes": {
                "OBJECTID": 526,
                "FACILITYID": null,
                "NAME": "NEWTON ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Brookline",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "51",
                "DESCRIPT": "INBOUND:CLEVLAND CL-FOREST HIL",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7919958.0839179046,
                "y": 5207184.3309692424
            }
        },
        {
            "attributes": {
                "OBJECTID": 527,
                "FACILITYID": null,
                "NAME": "NEWTON ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Brookline",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "51",
                "DESCRIPT": "OUTBOUND:FOREST HILL-CLEVELAND",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7919942.5215746164,
                "y": 5207152.6161572868
            }
        },
        {
            "attributes": {
                "OBJECTID": 528,
                "FACILITYID": null,
                "NAME": "GROVE ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Brookline",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "51",
                "DESCRIPT": "OUTBOUND:FOREST HILL-CLEVELAND",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7920121.9418063965,
                "y": 5206875.9161542933
            }
        },
        {
            "attributes": {
                "OBJECTID": 529,
                "FACILITYID": null,
                "NAME": "GROVE ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Brookline",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "51",
                "DESCRIPT": "OUTBOUND:FOREST HILL-CLEVELAND",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7920571.7606426803,
                "y": 5206459.86224401
            }
        },
        {
            "attributes": {
                "OBJECTID": 530,
                "FACILITYID": null,
                "NAME": "HARVARD ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Brookline",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "66",
                "DESCRIPT": "INBOUND: ALLSTON - DUDLEY",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7916945.8966758912,
                "y": 5211183.1983299386
            }
        },
        {
            "attributes": {
                "OBJECTID": 531,
                "FACILITYID": null,
                "NAME": "HARVARD ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Brookline",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "66",
                "DESCRIPT": "INBOUND: ALLSTON - DUDLEY",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7917092.8831995223,
                "y": 5211415.6154322736
            }
        },
        {
            "attributes": {
                "OBJECTID": 532,
                "FACILITYID": null,
                "NAME": "HARVARD ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Brookline",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "66",
                "DESCRIPT": "INBOUND: ALLSTON - DUDLEY",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7917216.8845310034,
                "y": 5211733.3603057247
            }
        },
        {
            "attributes": {
                "OBJECTID": 533,
                "FACILITYID": null,
                "NAME": "HARVARD ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Brookline",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "66",
                "DESCRIPT": "INBOUND: ALLSTON - DUDLEY",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7917150.3547424665,
                "y": 5212030.7553474912
            }
        },
        {
            "attributes": {
                "OBJECTID": 534,
                "FACILITYID": null,
                "NAME": "HARVARD ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Brookline",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "66",
                "DESCRIPT": "INBOUND: ALLSTON - DUDLEY",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7917231.4954319606,
                "y": 5212400.2545042587
            }
        },
        {
            "attributes": {
                "OBJECTID": 535,
                "FACILITYID": null,
                "NAME": "HARVARD ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Brookline",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "66",
                "DESCRIPT": "INBOUND: ALLSTON - DUDLEY",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7917860.0260020681,
                "y": 5212862.6637585163
            }
        },
        {
            "attributes": {
                "OBJECTID": 536,
                "FACILITYID": null,
                "NAME": "HARVARD ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Brookline",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "66",
                "DESCRIPT": "INBOUND: ALLSTON - DUDLEY",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7917965.6828282485,
                "y": 5213010.2576235449
            }
        },
        {
            "attributes": {
                "OBJECTID": 537,
                "FACILITYID": null,
                "NAME": "HARVARD ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Brookline",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "66",
                "DESCRIPT": "INBOUND: ALLSTON - DUDLEY",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7918117.9388033943,
                "y": 5213332.0348927211
            }
        },
        {
            "attributes": {
                "OBJECTID": 538,
                "FACILITYID": null,
                "NAME": "HARVARD ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Brookline",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "66",
                "DESCRIPT": "INBOUND: ALLSTON - DUDLEY",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7917667.4526496259,
                "y": 5212723.8981186366
            }
        },
        {
            "attributes": {
                "OBJECTID": 539,
                "FACILITYID": null,
                "NAME": "HARVARD ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Brookline",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "66",
                "DESCRIPT": "INBOUND: ALLSTON - DUDLEY",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7917448.0264022183,
                "y": 5212568.9374470068
            }
        },
        {
            "attributes": {
                "OBJECTID": 540,
                "FACILITYID": null,
                "NAME": "CHESTNUT HILL AVE",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Brookline",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "51",
                "DESCRIPT": " ",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7920337.2005492412,
                "y": 5211271.3356689671
            }
        },
        {
            "attributes": {
                "OBJECTID": 541,
                "FACILITYID": null,
                "NAME": "WASHINGTON ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Brookline",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "66",
                "DESCRIPT": " ",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7916684.4525489882,
                "y": 5210833.8216752661
            }
        },
        {
            "attributes": {
                "OBJECTID": 542,
                "FACILITYID": null,
                "NAME": "BOYLSTON ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Boston",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "60",
                "DESCRIPT": " ",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7922487.7226101682,
                "y": 5209402.9268871238
            }
        },
        {
            "attributes": {
                "OBJECTID": 543,
                "FACILITYID": null,
                "NAME": "BOYLSTON ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Boston",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "60",
                "DESCRIPT": "OUTBOUND:KENMORE-CHESTNUT HILL",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7922332.9270123504,
                "y": 5209461.1969750738
            }
        },
        {
            "attributes": {
                "OBJECTID": 544,
                "FACILITYID": null,
                "NAME": "BOYLSTON ST - HPKW",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Boston",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "60",
                "DESCRIPT": " ",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7922853.8543798421,
                "y": 5209240.0161889372
            }
        },
        {
            "attributes": {
                "OBJECTID": 545,
                "FACILITYID": null,
                "NAME": "BOYLSTON ST - HPKW",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Boston",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "60",
                "DESCRIPT": " ",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7922842.4317951435,
                "y": 5209213.1177071743
            }
        },
        {
            "attributes": {
                "OBJECTID": 546,
                "FACILITYID": null,
                "NAME": "WASHINGTON ST/COREY RD",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Boston",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "65",
                "DESCRIPT": " ",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7919295.0067781731,
                "y": 5212406.5403350042
            }
        },
        {
            "attributes": {
                "OBJECTID": 547,
                "FACILITYID": null,
                "NAME": "WASHINGTON ST/COREY RD",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Boston",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "65",
                "DESCRIPT": " ",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7919312.1169718355,
                "y": 5212389.5648709014
            }
        },
        {
            "attributes": {
                "OBJECTID": 548,
                "FACILITYID": null,
                "NAME": "WASHINGTON ST/COMM AVE",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Boston",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "65",
                "DESCRIPT": " ",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7919549.6582832588,
                "y": 5212598.1399871539
            }
        },
        {
            "attributes": {
                "OBJECTID": 549,
                "FACILITYID": null,
                "NAME": "WASHINGTON ST/COMM AVE",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Boston",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "65",
                "DESCRIPT": " ",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7919560.313001289,
                "y": 5212572.9741079025
            }
        },
        {
            "attributes": {
                "OBJECTID": 550,
                "FACILITYID": null,
                "NAME": "WASHINGTON ST/EUSTON RD",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Boston",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "65",
                "DESCRIPT": " ",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7919755.6305133114,
                "y": 5212745.2067951988
            }
        },
        {
            "attributes": {
                "OBJECTID": 551,
                "FACILITYID": null,
                "NAME": "WASHINGTON ST/EUSTON RD",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Boston",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "65",
                "DESCRIPT": " ",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7919770.737049249,
                "y": 5212726.7749824543
            }
        },
        {
            "attributes": {
                "OBJECTID": 552,
                "FACILITYID": null,
                "NAME": "HARVARD AVE/BRIGHTON AVE",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Boston",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "66",
                "DESCRIPT": " ",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7918363.5513850218,
                "y": 5213972.016011077
            }
        },
        {
            "attributes": {
                "OBJECTID": 553,
                "FACILITYID": null,
                "NAME": "HARVARD AVE/BRIGHTON AVE",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Boston",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "66",
                "DESCRIPT": " ",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7918396.7384551549,
                "y": 5213970.7129874369
            }
        },
        {
            "attributes": {
                "OBJECTID": 554,
                "FACILITYID": null,
                "NAME": "HARVARD ST/COMM AVE",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Boston",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "66",
                "DESCRIPT": " ",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7918228.3090801444,
                "y": 5213562.531503669
            }
        },
        {
            "attributes": {
                "OBJECTID": 555,
                "FACILITYID": null,
                "NAME": "HARVARD ST/COMM AVE",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Boston",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "66",
                "DESCRIPT": " ",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7918262.9633698491,
                "y": 5213548.2154309992
            }
        },
        {
            "attributes": {
                "OBJECTID": 556,
                "FACILITYID": null,
                "NAME": "HUNTINGTON AVE/JAMAICA WAY",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Boston",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "66",
                "DESCRIPT": " ",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7916190.4541892046,
                "y": 5210852.9151276955
            }
        },
        {
            "attributes": {
                "OBJECTID": 557,
                "FACILITYID": null,
                "NAME": "HUNTINGTON AVE/JAMAICA WAY",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Boston",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "66",
                "DESCRIPT": " ",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7916182.5253025275,
                "y": 5210813.7268133825
            }
        },
        {
            "attributes": {
                "OBJECTID": 558,
                "FACILITYID": null,
                "NAME": "HUNTINGTON AVE/PARKERHILL AVE",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Boston",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "66",
                "DESCRIPT": " ",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7915898.1650746372,
                "y": 5211000.7494928408
            }
        },
        {
            "attributes": {
                "OBJECTID": 559,
                "FACILITYID": null,
                "NAME": "HUNTINGTON AVE/PARKERHILL AVE",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Boston",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "66",
                "DESCRIPT": " ",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7915868.7194593474,
                "y": 5211042.3497838266
            }
        },
        {
            "attributes": {
                "OBJECTID": 560,
                "FACILITYID": null,
                "NAME": "HUNTINGTON AVE/MISSION ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Boston",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "66",
                "DESCRIPT": " ",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7915613.4895325201,
                "y": 5211013.590745016
            }
        },
        {
            "attributes": {
                "OBJECTID": 561,
                "FACILITYID": null,
                "NAME": "HUNTINGTON AVE/MISSION ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Boston",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "66",
                "DESCRIPT": " ",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7915630.2450457336,
                "y": 5211057.7798498683
            }
        },
        {
            "attributes": {
                "OBJECTID": 562,
                "FACILITYID": null,
                "NAME": "HUNTINGTON AVE/WATI ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Boston",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "66",
                "DESCRIPT": " ",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7915488.1802397771,
                "y": 5211051.6471110433
            }
        },
        {
            "attributes": {
                "OBJECTID": 563,
                "FACILITYID": null,
                "NAME": "HUNTINGTON AVE/WATI ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Boston",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "66",
                "DESCRIPT": " ",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7915500.7784950193,
                "y": 5211087.4495136207
            }
        },
        {
            "attributes": {
                "OBJECTID": 564,
                "FACILITYID": null,
                "NAME": "COREY ST/WELD ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Boston",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "51",
                "DESCRIPT": " ",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7921556.5204557916,
                "y": 5204772.5435666116
            }
        },
        {
            "attributes": {
                "OBJECTID": 565,
                "FACILITYID": null,
                "NAME": "COREY ST/WELD ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Boston",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "51",
                "DESCRIPT": " ",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7921547.5755752977,
                "y": 5204751.8601823803
            }
        },
        {
            "attributes": {
                "OBJECTID": 566,
                "FACILITYID": null,
                "NAME": "WELD ST/WILLOW ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Boston",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "51",
                "DESCRIPT": " ",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7921020.1227524457,
                "y": 5204808.3776219729
            }
        },
        {
            "attributes": {
                "OBJECTID": 567,
                "FACILITYID": null,
                "NAME": "WELD ST/WILLOW ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Boston",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "51",
                "DESCRIPT": " ",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7921025.7933257744,
                "y": 5204836.7912972067
            }
        },
        {
            "attributes": {
                "OBJECTID": 568,
                "FACILITYID": null,
                "NAME": "WELD ST/MAPLE ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Boston",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "51",
                "DESCRIPT": " ",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7921167.793405897,
                "y": 5204758.6975303162
            }
        },
        {
            "attributes": {
                "OBJECTID": 569,
                "FACILITYID": null,
                "NAME": "WELD ST/MAPLE ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Boston",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "51",
                "DESCRIPT": " ",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7921165.295718981,
                "y": 5204734.1167826233
            }
        },
        {
            "attributes": {
                "OBJECTID": 570,
                "FACILITYID": null,
                "NAME": "WELD ST/RUSSETT RD",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Boston",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "51",
                "DESCRIPT": " ",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7920657.0970632834,
                "y": 5205000.3714556908
            }
        },
        {
            "attributes": {
                "OBJECTID": 571,
                "FACILITYID": null,
                "NAME": "WELD ST/RUSSETT RD",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Boston",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "51",
                "DESCRIPT": " ",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7920676.4093163284,
                "y": 5204987.4420714565
            }
        },
        {
            "attributes": {
                "OBJECTID": 572,
                "FACILITYID": null,
                "NAME": "WELD ST/MANTHORNE ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Boston",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "51",
                "DESCRIPT": " ",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7920886.0202404903,
                "y": 5204960.9377475996
            }
        },
        {
            "attributes": {
                "OBJECTID": 573,
                "FACILITYID": null,
                "NAME": "WELD ST/CHURCHE ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Boston",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "51",
                "DESCRIPT": " ",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7920319.5338449515,
                "y": 5204968.3225255636
            }
        },
        {
            "attributes": {
                "OBJECTID": 574,
                "FACILITYID": null,
                "NAME": "WELD ST/CHURCHE ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Boston",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "51",
                "DESCRIPT": " ",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7920338.1934227459,
                "y": 5204983.2661269521
            }
        },
        {
            "attributes": {
                "OBJECTID": 575,
                "FACILITYID": null,
                "NAME": "WELD ST/W ROXBURY PKWAY",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Boston",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "51",
                "DESCRIPT": " ",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7919961.5238821479,
                "y": 5205074.7258978505
            }
        },
        {
            "attributes": {
                "OBJECTID": 576,
                "FACILITYID": null,
                "NAME": "WELD ST/W ROXBURY PKWAY",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Boston",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "51",
                "DESCRIPT": " ",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7919920.7675119871,
                "y": 5205086.2224623859
            }
        },
        {
            "attributes": {
                "OBJECTID": 577,
                "FACILITYID": null,
                "NAME": "WELD ST/BURNSIDE AVE",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Boston",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "51",
                "DESCRIPT": " ",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7919793.667389079,
                "y": 5205008.673873283
            }
        },
        {
            "attributes": {
                "OBJECTID": 578,
                "FACILITYID": null,
                "NAME": "WELD ST/BURNSIDE AVE",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Boston",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "51",
                "DESCRIPT": " ",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7919771.8331323005,
                "y": 5205028.1983740591
            }
        },
        {
            "attributes": {
                "OBJECTID": 579,
                "FACILITYID": null,
                "NAME": "VFW PARKWAY/COREY ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Boston",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "51",
                "DESCRIPT": " ",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7921764.434405678,
                "y": 5205018.0497995755
            }
        },
        {
            "attributes": {
                "OBJECTID": 580,
                "FACILITYID": null,
                "NAME": "WELD ST/MANTHORNE ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Boston",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "51",
                "DESCRIPT": " ",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7920864.1725540711,
                "y": 5204951.763754881
            }
        },
        {
            "attributes": {
                "OBJECTID": 581,
                "FACILITYID": null,
                "NAME": "WELD ST/RUSKIN ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Boston",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "51",
                "DESCRIPT": " ",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7921318.0294475872,
                "y": 5204788.5190634066
            }
        },
        {
            "attributes": {
                "OBJECTID": 582,
                "FACILITYID": null,
                "NAME": "WELD ST/RUSKIN ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Boston",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "51",
                "DESCRIPT": " ",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7921308.1645622095,
                "y": 5204792.2992337849
            }
        }
    ]""")



test2 = """
[
        {
            "attributes": {
                "OBJECTID": 437,
                "FACILITYID": null,
                "NAME": "BROOKLINE AVE",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Brookline",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "65",
                "DESCRIPT": "OUTBOUND: KENMORE - BRIGHTON",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7916116.574052511,
                "y": 5211282.820506682
            }
        },
        {
            "attributes": {
                "OBJECTID": 438,
                "FACILITYID": null,
                "NAME": "WASHINGTON ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Brookline",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "65",
                "DESCRIPT": "OUTBOUND: KENMORE - BRIGHTON",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7917388.896202298,
                "y": 5211260.857902907
            }
        },
        {
            "attributes": {
                "OBJECTID": 439,
                "FACILITYID": null,
                "NAME": "WASHINGTON ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Brookline",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "65",
                "DESCRIPT": "OUTBOUND: KENMORE - BRIGHTON",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7917922.089954247,
                "y": 5211785.56408028
            }
        },
        {
            "attributes": {
                "OBJECTID": 440,
                "FACILITYID": null,
                "NAME": "WASHINGTON ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Brookline",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "65",
                "DESCRIPT": "OUTBOUND: KENMORE - BRIGHTON",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7919070.156718281,
                "y": 5212246.819561962
            }
        },
        {
            "attributes": {
                "OBJECTID": 441,
                "FACILITYID": null,
                "NAME": "WASHINGTON ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Brookline",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "65",
                "DESCRIPT": "OUTBOUND: KENMORE - BRIGHTON",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7918296.966218766,
                "y": 5211809.22558338
            }
        },
        {
            "attributes": {
                "OBJECTID": 442,
                "FACILITYID": null,
                "NAME": "WASHINGTON ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Brookline",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "65",
                "DESCRIPT": "OUTBOUND: KENMORE - BRIGHTON",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7918666.5375123555,
                "y": 5211900.821397762
            }
        },
        {
            "attributes": {
                "OBJECTID": 443,
                "FACILITYID": null,
                "NAME": "WASHINGTON ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Brookline",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "65",
                "DESCRIPT": "INBOUND: BRIGHTON - KENMORE",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7919058.390724127,
                "y": 5212211.523490504
            }
        },
        {
            "attributes": {
                "OBJECTID": 444,
                "FACILITYID": null,
                "NAME": "WASHINGTON ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Brookline",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "65",
                "DESCRIPT": "INBOUND: BRIGHTON - KENMORE",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7918813.521635293,
                "y": 5211988.934804798
            }
        },
        {
            "attributes": {
                "OBJECTID": 445,
                "FACILITYID": null,
                "NAME": "WASHINGTON ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Brookline",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "65",
                "DESCRIPT": "INBOUND: BRIGHTON - KENMORE",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7918594.676677775,
                "y": 5211841.980727792
            }
        },
        {
            "attributes": {
                "OBJECTID": 446,
                "FACILITYID": null,
                "NAME": "WASHINGTON ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Brookline",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "65",
                "DESCRIPT": "INBOUND: BRIGHTON - KENMORE",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7917703.213970144,
                "y": 5211506.428557692
            }
        },
        {
            "attributes": {
                "OBJECTID": 447,
                "FACILITYID": null,
                "NAME": "WASHINGTON ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Brookline",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "65",
                "DESCRIPT": "INBOUND: BRIGHTON - KENMORE",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7918083.1770421965,
                "y": 5211800.742941336
            }
        },
        {
            "attributes": {
                "OBJECTID": 448,
                "FACILITYID": null,
                "NAME": "WASHINGTON ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Brookline",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "65",
                "DESCRIPT": "INBOUND: BRIGHTON - KENMORE",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7918351.581099294,
                "y": 5211794.986645734
            }
        },
        {
            "attributes": {
                "OBJECTID": 449,
                "FACILITYID": null,
                "NAME": "WASHINGTON ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Brookline",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "65",
                "DESCRIPT": "INBOUND: BRIGHTON - KENMORE",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7917588.572599403,
                "y": 5211339.148449587
            }
        },
        {
            "attributes": {
                "OBJECTID": 450,
                "FACILITYID": null,
                "NAME": "WASHINGTON ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Brookline",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "65",
                "DESCRIPT": "INBOUND: BRIGHTON - KENMORE",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7916932.978055578,
                "y": 5210996.083449429
            }
        },
        {
            "attributes": {
                "OBJECTID": 451,
                "FACILITYID": null,
                "NAME": "BROOKLINE AVE",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Brookline",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "65",
                "DESCRIPT": "INBOUND: BRIGHTON - KENMORE",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7916412.575788774,
                "y": 5210854.973858573
            }
        },
        {
            "attributes": {
                "OBJECTID": 452,
                "FACILITYID": null,
                "NAME": "BROOKLINE AVE",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Brookline",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "65",
                "DESCRIPT": "INBOUND: BRIGHTON - KENMORE",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7916266.897172153,
                "y": 5211041.53076946
            }
        },
        {
            "attributes": {
                "OBJECTID": 453,
                "FACILITYID": null,
                "NAME": "380 ft East of River Rd",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Brookline",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "65",
                "DESCRIPT": "INBOUND: BRIGHTON - KENMORE",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7916092.266586247,
                "y": 5211250.927201084
            }
        },
        {
            "attributes": {
                "OBJECTID": 454,
                "FACILITYID": null,
                "NAME": "WASHINGTON ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Brookline",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "65",
                "DESCRIPT": "INBOUND: BRIGHTON - KENMORE",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7916900.635054242,
                "y": 5210937.726573459
            }
        },
        {
            "attributes": {
                "OBJECTID": 455,
                "FACILITYID": null,
                "NAME": "BROOKLINE AVE",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Brookline",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "65",
                "DESCRIPT": "OUTBOUND: KENMORE - BRIGHTON",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7916357.483767159,
                "y": 5210975.236624356
            }
        },
        {
            "attributes": {
                "OBJECTID": 456,
                "FACILITYID": null,
                "NAME": "BROOKLINE AVE",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Brookline",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "65",
                "DESCRIPT": "OUTBOUND: KENMORE - BRIGHTON",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7916262.887593312,
                "y": 5211095.949419579
            }
        },
        {
            "attributes": {
                "OBJECTID": 457,
                "FACILITYID": null,
                "NAME": "HARVARD ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Brookline",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "66",
                "DESCRIPT": "OUTBOUND: DUDLEY - ALLSTON",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7917156.974248903,
                "y": 5212325.269843713
            }
        },
        {
            "attributes": {
                "OBJECTID": 458,
                "FACILITYID": null,
                "NAME": "BABCOCK ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Brookline",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "66",
                "DESCRIPT": "OUTBOUND: DUDLEY - ALLSTON",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7917422.559066412,
                "y": 5212584.74765383
            }
        },
        {
            "attributes": {
                "OBJECTID": 459,
                "FACILITYID": null,
                "NAME": "HARVARD ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Brookline",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "66",
                "DESCRIPT": "OUTBOUND: DUDLEY - ALLSTON",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7917844.377502648,
                "y": 5212889.122932068
            }
        },
        {
            "attributes": {
                "OBJECTID": 460,
                "FACILITYID": null,
                "NAME": "HARVARD ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Brookline",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "66",
                "DESCRIPT": "OUTBOUND: DUDLEY - ALLSTON",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7917945.395078886,
                "y": 5213036.937767695
            }
        },
        {
            "attributes": {
                "OBJECTID": 461,
                "FACILITYID": null,
                "NAME": "HARVARD ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Brookline",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "66",
                "DESCRIPT": "OUTBOUND: DUDLEY - ALLSTON",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7918059.578473637,
                "y": 5213276.921466092
            }
        },
        {
            "attributes": {
                "OBJECTID": 462,
                "FACILITYID": null,
                "NAME": "HARVARD ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Brookline",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "66",
                "DESCRIPT": "OUTBOUND: DUDLEY - ALLSTON",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7916961.960673376,
                "y": 5211291.110344153
            }
        },
        {
            "attributes": {
                "OBJECTID": 463,
                "FACILITYID": null,
                "NAME": "HARVARD ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Brookline",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "66",
                "DESCRIPT": "OUTBOUND: DUDLEY - ALLSTON",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7917112.220728257,
                "y": 5211475.196893705
            }
        },
        {
            "attributes": {
                "OBJECTID": 464,
                "FACILITYID": null,
                "NAME": "HARVARD ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Brookline",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "66",
                "DESCRIPT": "OUTBOUND: DUDLEY - ALLSTON",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7917195.0602085395,
                "y": 5211644.3215244375
            }
        },
        {
            "attributes": {
                "OBJECTID": 465,
                "FACILITYID": null,
                "NAME": "HARVARD ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Brookline",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "66",
                "DESCRIPT": "OUTBOUND: DUDLEY - ALLSTON",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7917164.42026615,
                "y": 5211886.90965389
            }
        },
        {
            "attributes": {
                "OBJECTID": 466,
                "FACILITYID": null,
                "NAME": "HARVARD ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Brookline",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "66",
                "DESCRIPT": "OUTBOUND: DUDLEY - ALLSTON",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7917694.156535649,
                "y": 5212778.344436235
            }
        },
        {
            "attributes": {
                "OBJECTID": 467,
                "FACILITYID": null,
                "NAME": "WASHINGTON ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Brookline",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "65",
                "DESCRIPT": "INBOUND: BRIGHTON - KENMORE",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7916778.479994524,
                "y": 5210712.2558378065
            }
        },
        {
            "attributes": {
                "OBJECTID": 468,
                "FACILITYID": null,
                "NAME": "WASHINGTON ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Brookline",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "66",
                "DESCRIPT": "INBOUND: ALLSTON - DUDLEY",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7916777.146931738,
                "y": 5210711.936543205
            }
        },
        {
            "attributes": {
                "OBJECTID": 469,
                "FACILITYID": null,
                "NAME": "WASHINGTON ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Brookline",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "65",
                "DESCRIPT": "INBOUND: BRIGHTON - KENMORE",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7917358.086626942,
                "y": 5211220.664857027
            }
        },
        {
            "attributes": {
                "OBJECTID": 470,
                "FACILITYID": null,
                "NAME": "WASHINGTON ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Brookline",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "65",
                "DESCRIPT": "OUTBOUND: KENMORE - BRIGHTON",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7917573.810598882,
                "y": 5211356.884981477
            }
        },
        {
            "attributes": {
                "OBJECTID": 471,
                "FACILITYID": null,
                "NAME": "WASHINGTON ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Brookline",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "65",
                "DESCRIPT": "OUTBOUND: KENMORE - BRIGHTON",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7917708.843684004,
                "y": 5211554.181539058
            }
        },
        {
            "attributes": {
                "OBJECTID": 472,
                "FACILITYID": null,
                "NAME": "WASHINGTON ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Brookline",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "65",
                "DESCRIPT": "OUTBOUND: KENMORE - BRIGHTON",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7916939.767986185,
                "y": 5211031.653150417
            }
        },
        {
            "attributes": {
                "OBJECTID": 473,
                "FACILITYID": null,
                "NAME": "BOYLSTON ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Brookline",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "60",
                "DESCRIPT": "OUTBOUND:KENMORE-CHESTNUT HILL",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7922170.20200383,
                "y": 5209519.64931027
            }
        },
        {
            "attributes": {
                "OBJECTID": 474,
                "FACILITYID": null,
                "NAME": "BOYLSTON ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Brookline",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "60",
                "DESCRIPT": "INBOUND:CHESTNUT HILL-KENMORE",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7921025.175123384,
                "y": 5209835.901239291
            }
        },
        {
            "attributes": {
                "OBJECTID": 475,
                "FACILITYID": null,
                "NAME": "BOYLSTON ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Brookline",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "60",
                "DESCRIPT": "INBOUND:CHESTNUT HILL-KENMORE",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7917994.383059105,
                "y": 5210468.749085256
            }
        },
        {
            "attributes": {
                "OBJECTID": 476,
                "FACILITYID": null,
                "NAME": " ",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Brookline",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "65 ",
                "DESCRIPT": "OUTBOUND: KENMORE - BRIGHTON",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7916602.612676427,
                "y": 5210836.751353311
            }
        },
        {
            "attributes": {
                "OBJECTID": 477,
                "FACILITYID": null,
                "NAME": "CHESTNUT HILL AVE",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Brookline",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "51",
                "DESCRIPT": " ",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7920256.914389668,
                "y": 5211296.368775928
            }
        },
        {
            "attributes": {
                "OBJECTID": 478,
                "FACILITYID": null,
                "NAME": "CHESTNUT HILL AVE",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Brookline",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "51",
                "DESCRIPT": "INBOUND:CLEVLAND CL-FOREST HIL",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7920024.347163393,
                "y": 5210880.325088
            }
        },
        {
            "attributes": {
                "OBJECTID": 479,
                "FACILITYID": null,
                "NAME": "CHESTNUT HILL AVE",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Brookline",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "51",
                "DESCRIPT": "INBOUND:CLEVLAND CL-FOREST HIL",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7919944.20474885,
                "y": 5210539.569909758
            }
        },
        {
            "attributes": {
                "OBJECTID": 480,
                "FACILITYID": null,
                "NAME": "GROVE ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Brookline",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "51",
                "DESCRIPT": "INBOUND:CLEVLAND CL-FOREST HIL",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7920437.314312712,
                "y": 5206653.661287776
            }
        },
        {
            "attributes": {
                "OBJECTID": 481,
                "FACILITYID": null,
                "NAME": "GROVE ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Brookline",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "51",
                "DESCRIPT": "INBOUND:CLEVLAND CL-FOREST HIL",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7920854.189785894,
                "y": 5206185.55918812
            }
        },
        {
            "attributes": {
                "OBJECTID": 482,
                "FACILITYID": null,
                "NAME": "GROVE ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Brookline",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "51",
                "DESCRIPT": "INBOUND:CLEVLAND CL-FOREST HIL",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7920970.220658819,
                "y": 5206047.199925127
            }
        },
        {
            "attributes": {
                "OBJECTID": 483,
                "FACILITYID": null,
                "NAME": "GROVE ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Brookline",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "51",
                "DESCRIPT": "INBOUND:CLEVLAND CL-FOREST HIL",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7921162.771641931,
                "y": 5205765.985828667
            }
        },
        {
            "attributes": {
                "OBJECTID": 484,
                "FACILITYID": null,
                "NAME": "GROVE ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Brookline",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "51",
                "DESCRIPT": "OUTBOUND:FOREST HILL-CLEVELAND",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7921141.532289298,
                "y": 5205750.096247806
            }
        },
        {
            "attributes": {
                "OBJECTID": 485,
                "FACILITYID": null,
                "NAME": "GROVE ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Brookline",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "51",
                "DESCRIPT": "OUTBOUND:FOREST HILL-CLEVELAND",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7920951.23644272,
                "y": 5206029.145299288
            }
        },
        {
            "attributes": {
                "OBJECTID": 486,
                "FACILITYID": null,
                "NAME": "GROVE ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Brookline",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "51",
                "DESCRIPT": "OUTBOUND:FOREST HILL-CLEVELAND",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7920795.280880646,
                "y": 5206217.193650736
            }
        },
        {
            "attributes": {
                "OBJECTID": 487,
                "FACILITYID": null,
                "NAME": "CHESTNUT HILL AVE",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Brookline",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "51",
                "DESCRIPT": "OUTBOUND:FOREST HILL-CLEVELAND",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7919921.294871111,
                "y": 5210552.677119292
            }
        },
        {
            "attributes": {
                "OBJECTID": 488,
                "FACILITYID": null,
                "NAME": "CHESTNUT HILL AVE",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Brookline",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "51",
                "DESCRIPT": "OUTBOUND:FOREST HILL-CLEVELAND",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7920009.540391522,
                "y": 5210906.124799846
            }
        },
        {
            "attributes": {
                "OBJECTID": 489,
                "FACILITYID": null,
                "NAME": "CYPRESS ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Brookline",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "60",
                "DESCRIPT": "INBOUND:CHESTNUT HILL-KENMORE",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7917728.334993408,
                "y": 5210435.667583783
            }
        },
        {
            "attributes": {
                "OBJECTID": 490,
                "FACILITYID": null,
                "NAME": "CYPRESS ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Brookline",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "60",
                "DESCRIPT": "INBOUND:CHESTNUT HILL-KENMORE",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7917482.059360059,
                "y": 5210046.272364825
            }
        },
        {
            "attributes": {
                "OBJECTID": 491,
                "FACILITYID": null,
                "NAME": "HIGH ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Brookline",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "60",
                "DESCRIPT": "INBOUND:CHESTNUT HILL-KENMORE",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7917065.938113725,
                "y": 5209936.792142676
            }
        },
        {
            "attributes": {
                "OBJECTID": 492,
                "FACILITYID": null,
                "NAME": "HIGH ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Brookline",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "60",
                "DESCRIPT": "INBOUND:CHESTNUT HILL-KENMORE",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7916947.447397203,
                "y": 5210211.851948232
            }
        },
        {
            "attributes": {
                "OBJECTID": 493,
                "FACILITYID": null,
                "NAME": "BOYLSTON ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Brookline",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "60",
                "DESCRIPT": "INBOUND:CHESTNUT HILL-KENMORE",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7916662.078098114,
                "y": 5210773.591074351
            }
        },
        {
            "attributes": {
                "OBJECTID": 494,
                "FACILITYID": null,
                "NAME": "HIGH ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Brookline",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "60",
                "DESCRIPT": "OUTBOUND:KENMORE-CHESTNUT HILL",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7916975.521568579,
                "y": 5210180.854775072
            }
        },
        {
            "attributes": {
                "OBJECTID": 495,
                "FACILITYID": null,
                "NAME": "HIGH ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Brookline",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "60",
                "DESCRIPT": "OUTBOUND:KENMORE-CHESTNUT HILL",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7917057.209931542,
                "y": 5209995.418154029
            }
        },
        {
            "attributes": {
                "OBJECTID": 496,
                "FACILITYID": null,
                "NAME": "CYPRESS ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Brookline",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "60",
                "DESCRIPT": "INBOUND:CHESTNUT HILL-KENMORE",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7917299.10817905,
                "y": 5209870.482549113
            }
        },
        {
            "attributes": {
                "OBJECTID": 497,
                "FACILITYID": null,
                "NAME": "CYPRESS ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Brookline",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "60",
                "DESCRIPT": "OUTBOUND:KENMORE-CHESTNUT HILL",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7917252.579013795,
                "y": 5209860.113335104
            }
        },
        {
            "attributes": {
                "OBJECTID": 498,
                "FACILITYID": null,
                "NAME": "CYPRESS ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Brookline",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "60",
                "DESCRIPT": "OUTBOUND:KENMORE-CHESTNUT HILL",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7917483.524849877,
                "y": 5210089.885328026
            }
        },
        {
            "attributes": {
                "OBJECTID": 499,
                "FACILITYID": null,
                "NAME": "CYPRESS ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Brookline",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "60",
                "DESCRIPT": "OUTBOUND:KENMORE-CHESTNUT HILL",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7917683.794701426,
                "y": 5210306.495442125
            }
        },
        {
            "attributes": {
                "OBJECTID": 500,
                "FACILITYID": null,
                "NAME": "CYPRESS ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Brookline",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "60",
                "DESCRIPT": "INBOUND:CHESTNUT HILL-KENMORE",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7917702.432736128,
                "y": 5210296.414865536
            }
        },
        {
            "attributes": {
                "OBJECTID": 501,
                "FACILITYID": null,
                "NAME": "BOYLSTON ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Brookline",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "60",
                "DESCRIPT": "OUTBOUND:KENMORE-CHESTNUT HILL",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7917983.132082046,
                "y": 5210501.66581414
            }
        },
        {
            "attributes": {
                "OBJECTID": 502,
                "FACILITYID": null,
                "NAME": "150 ft West of Tully St",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Brookline",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "60",
                "DESCRIPT": " ",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7922380.16435046,
                "y": 5209376.980536394
            }
        },
        {
            "attributes": {
                "OBJECTID": 503,
                "FACILITYID": null,
                "NAME": "BOYLSTON ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Brookline",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "60",
                "DESCRIPT": " ",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7922487.727973728,
                "y": 5209402.945627672
            }
        },
        {
            "attributes": {
                "OBJECTID": 504,
                "FACILITYID": null,
                "NAME": "BOYLSTON ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Brookline",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "60",
                "DESCRIPT": "OUTBOUND:KENMORE-CHESTNUT HILL",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7922332.923753001,
                "y": 5209461.185608043
            }
        },
        {
            "attributes": {
                "OBJECTID": 505,
                "FACILITYID": null,
                "NAME": "BOYLSTON ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Brookline",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "60",
                "DESCRIPT": "INBOUND:CHESTNUT HILL-KENMORE",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7921950.635019327,
                "y": 5209530.663070651
            }
        },
        {
            "attributes": {
                "OBJECTID": 506,
                "FACILITYID": null,
                "NAME": "BOYLSTON ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Brookline",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "60",
                "DESCRIPT": "OUTBOUND:KENMORE-CHESTNUT HILL",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7921914.919649594,
                "y": 5209586.886113145
            }
        },
        {
            "attributes": {
                "OBJECTID": 507,
                "FACILITYID": null,
                "NAME": "BOYLSTON ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Brookline",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "60",
                "DESCRIPT": "INBOUND:CHESTNUT HILL-KENMORE",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7921442.179380171,
                "y": 5209701.882773534
            }
        },
        {
            "attributes": {
                "OBJECTID": 508,
                "FACILITYID": null,
                "NAME": "BOYLSTON ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Brookline",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "60",
                "DESCRIPT": "OUTBOUND:KENMORE-CHESTNUT HILL",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7921442.7542354865,
                "y": 5209740.038232284
            }
        },
        {
            "attributes": {
                "OBJECTID": 509,
                "FACILITYID": null,
                "NAME": "BOYLSTON ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Brookline",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "60",
                "DESCRIPT": "OUTBOUND:KENMORE-CHESTNUT HILL",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7921030.910473036,
                "y": 5209877.387471506
            }
        },
        {
            "attributes": {
                "OBJECTID": 510,
                "FACILITYID": null,
                "NAME": "BOYLSTON ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Brookline",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "60",
                "DESCRIPT": "OUTBOUND:KENMORE-CHESTNUT HILL",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7920394.053662085,
                "y": 5210060.785768832
            }
        },
        {
            "attributes": {
                "OBJECTID": 511,
                "FACILITYID": null,
                "NAME": "BOYLSTON ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Brookline",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "60",
                "DESCRIPT": "INBOUND:CHESTNUT HILL-KENMORE",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7920243.625986467,
                "y": 5210012.2381975
            }
        },
        {
            "attributes": {
                "OBJECTID": 512,
                "FACILITYID": null,
                "NAME": "BOYLSTON ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Brookline",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "60",
                "DESCRIPT": "OUTBOUND:KENMORE-CHESTNUT HILL",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7920124.140132441,
                "y": 5210036.964996539
            }
        },
        {
            "attributes": {
                "OBJECTID": 513,
                "FACILITYID": null,
                "NAME": "BOYLSTON ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Brookline",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "60",
                "DESCRIPT": "INBOUND:CHESTNUT HILL-KENMORE",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7919845.709151927,
                "y": 5209985.61100275
            }
        },
        {
            "attributes": {
                "OBJECTID": 514,
                "FACILITYID": null,
                "NAME": "BOYLSTON ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Brookline",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "60",
                "DESCRIPT": "OUTBOUND:KENMORE-CHESTNUT HILL",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7919862.461008236,
                "y": 5210017.9078585785
            }
        },
        {
            "attributes": {
                "OBJECTID": 515,
                "FACILITYID": null,
                "NAME": "BOYLSTON ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Brookline",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "51",
                "DESCRIPT": "INBOUND:CLEVLAND CL-FOREST HIL",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7919646.404072191,
                "y": 5210049.83018272
            }
        },
        {
            "attributes": {
                "OBJECTID": 516,
                "FACILITYID": null,
                "NAME": "BOYLSTON ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Brookline",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "60",
                "DESCRIPT": "INBOUND:CHESTNUT HILL-KENMORE",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7919611.477316248,
                "y": 5209980.094153795
            }
        },
        {
            "attributes": {
                "OBJECTID": 517,
                "FACILITYID": null,
                "NAME": "CHESTNUT HILL AVE",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Brookline",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "51",
                "DESCRIPT": "OUTBOUND:FOREST HILL-CLEVELAND",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7919595.046151389,
                "y": 5210064.25315686
            }
        },
        {
            "attributes": {
                "OBJECTID": 518,
                "FACILITYID": null,
                "NAME": "LEE ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Brookline",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "51",
                "DESCRIPT": "INBOUND:CLEVLAND CL-FOREST HIL",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7919359.617033474,
                "y": 5209943.921844208
            }
        },
        {
            "attributes": {
                "OBJECTID": 519,
                "FACILITYID": null,
                "NAME": "LEE ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Brookline",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "51",
                "DESCRIPT": "OUTBOUND:FOREST HILL-CLEVELAND",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7919323.978154581,
                "y": 5209964.855595362
            }
        },
        {
            "attributes": {
                "OBJECTID": 520,
                "FACILITYID": null,
                "NAME": "LEE ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Brookline",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "51",
                "DESCRIPT": "OUTBOUND:FOREST HILL-CLEVELAND",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7919068.673471795,
                "y": 5209385.14466256
            }
        },
        {
            "attributes": {
                "OBJECTID": 521,
                "FACILITYID": null,
                "NAME": "LEE ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Brookline",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "51",
                "DESCRIPT": "OUTBOUND:FOREST HILL-CLEVELAND",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7919343.568287369,
                "y": 5208777.24367865
            }
        },
        {
            "attributes": {
                "OBJECTID": 522,
                "FACILITYID": null,
                "NAME": "CLYDE ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Brookline",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "51",
                "DESCRIPT": "OUTBOUND:FOREST HILL-CLEVELAND",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7919495.899978737,
                "y": 5208204.365368129
            }
        },
        {
            "attributes": {
                "OBJECTID": 523,
                "FACILITYID": null,
                "NAME": "LEE ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Brookline",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "51",
                "DESCRIPT": "INBOUND:CLEVLAND CL-FOREST HIL",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7919526.453759551,
                "y": 5208202.194177612
            }
        },
        {
            "attributes": {
                "OBJECTID": 524,
                "FACILITYID": null,
                "NAME": "CLYDE ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Brookline",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "51",
                "DESCRIPT": "INBOUND:CLEVLAND CL-FOREST HIL",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7919554.194892685,
                "y": 5207728.029515571
            }
        },
        {
            "attributes": {
                "OBJECTID": 525,
                "FACILITYID": null,
                "NAME": "CLYDE ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Brookline",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "51",
                "DESCRIPT": "OUTBOUND:FOREST HILL-CLEVELAND",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7919525.658939638,
                "y": 5207732.3161829
            }
        },
        {
            "attributes": {
                "OBJECTID": 526,
                "FACILITYID": null,
                "NAME": "NEWTON ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Brookline",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "51",
                "DESCRIPT": "INBOUND:CLEVLAND CL-FOREST HIL",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7919958.083917905,
                "y": 5207184.330969242
            }
        },
        {
            "attributes": {
                "OBJECTID": 527,
                "FACILITYID": null,
                "NAME": "NEWTON ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Brookline",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "51",
                "DESCRIPT": "OUTBOUND:FOREST HILL-CLEVELAND",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7919942.521574616,
                "y": 5207152.616157287
            }
        },
        {
            "attributes": {
                "OBJECTID": 528,
                "FACILITYID": null,
                "NAME": "GROVE ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Brookline",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "51",
                "DESCRIPT": "OUTBOUND:FOREST HILL-CLEVELAND",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7920121.9418063965,
                "y": 5206875.916154293
            }
        },
        {
            "attributes": {
                "OBJECTID": 529,
                "FACILITYID": null,
                "NAME": "GROVE ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Brookline",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "51",
                "DESCRIPT": "OUTBOUND:FOREST HILL-CLEVELAND",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7920571.76064268,
                "y": 5206459.86224401
            }
        },
        {
            "attributes": {
                "OBJECTID": 530,
                "FACILITYID": null,
                "NAME": "HARVARD ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Brookline",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "66",
                "DESCRIPT": "INBOUND: ALLSTON - DUDLEY",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7916945.896675891,
                "y": 5211183.198329939
            }
        },
        {
            "attributes": {
                "OBJECTID": 531,
                "FACILITYID": null,
                "NAME": "HARVARD ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Brookline",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "66",
                "DESCRIPT": "INBOUND: ALLSTON - DUDLEY",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7917092.883199522,
                "y": 5211415.615432274
            }
        },
        {
            "attributes": {
                "OBJECTID": 532,
                "FACILITYID": null,
                "NAME": "HARVARD ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Brookline",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "66",
                "DESCRIPT": "INBOUND: ALLSTON - DUDLEY",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7917216.884531003,
                "y": 5211733.360305725
            }
        },
        {
            "attributes": {
                "OBJECTID": 533,
                "FACILITYID": null,
                "NAME": "HARVARD ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Brookline",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "66",
                "DESCRIPT": "INBOUND: ALLSTON - DUDLEY",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7917150.3547424665,
                "y": 5212030.755347491
            }
        },
        {
            "attributes": {
                "OBJECTID": 534,
                "FACILITYID": null,
                "NAME": "HARVARD ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Brookline",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "66",
                "DESCRIPT": "INBOUND: ALLSTON - DUDLEY",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7917231.495431961,
                "y": 5212400.254504259
            }
        },
        {
            "attributes": {
                "OBJECTID": 535,
                "FACILITYID": null,
                "NAME": "HARVARD ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Brookline",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "66",
                "DESCRIPT": "INBOUND: ALLSTON - DUDLEY",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7917860.026002068,
                "y": 5212862.663758516
            }
        },
        {
            "attributes": {
                "OBJECTID": 536,
                "FACILITYID": null,
                "NAME": "HARVARD ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Brookline",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "66",
                "DESCRIPT": "INBOUND: ALLSTON - DUDLEY",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7917965.6828282485,
                "y": 5213010.257623545
            }
        },
        {
            "attributes": {
                "OBJECTID": 537,
                "FACILITYID": null,
                "NAME": "HARVARD ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Brookline",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "66",
                "DESCRIPT": "INBOUND: ALLSTON - DUDLEY",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7918117.938803394,
                "y": 5213332.034892721
            }
        },
        {
            "attributes": {
                "OBJECTID": 538,
                "FACILITYID": null,
                "NAME": "HARVARD ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Brookline",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "66",
                "DESCRIPT": "INBOUND: ALLSTON - DUDLEY",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7917667.452649626,
                "y": 5212723.898118637
            }
        },
        {
            "attributes": {
                "OBJECTID": 539,
                "FACILITYID": null,
                "NAME": "HARVARD ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Brookline",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "66",
                "DESCRIPT": "INBOUND: ALLSTON - DUDLEY",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7917448.026402218,
                "y": 5212568.937447007
            }
        },
        {
            "attributes": {
                "OBJECTID": 540,
                "FACILITYID": null,
                "NAME": "CHESTNUT HILL AVE",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Brookline",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "51",
                "DESCRIPT": " ",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7920337.200549241,
                "y": 5211271.335668967
            }
        },
        {
            "attributes": {
                "OBJECTID": 541,
                "FACILITYID": null,
                "NAME": "WASHINGTON ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Brookline",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "66",
                "DESCRIPT": " ",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7916684.452548988,
                "y": 5210833.821675266
            }
        },
        {
            "attributes": {
                "OBJECTID": 542,
                "FACILITYID": null,
                "NAME": "BOYLSTON ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Boston",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "60",
                "DESCRIPT": " ",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7922487.722610168,
                "y": 5209402.926887124
            }
        },
        {
            "attributes": {
                "OBJECTID": 543,
                "FACILITYID": null,
                "NAME": "BOYLSTON ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Boston",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "60",
                "DESCRIPT": "OUTBOUND:KENMORE-CHESTNUT HILL",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7922332.92701235,
                "y": 5209461.196975074
            }
        },
        {
            "attributes": {
                "OBJECTID": 544,
                "FACILITYID": null,
                "NAME": "BOYLSTON ST - HPKW",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Boston",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "60",
                "DESCRIPT": " ",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7922853.854379842,
                "y": 5209240.016188937
            }
        },
        {
            "attributes": {
                "OBJECTID": 545,
                "FACILITYID": null,
                "NAME": "BOYLSTON ST - HPKW",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Boston",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "60",
                "DESCRIPT": " ",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7922842.4317951435,
                "y": 5209213.117707174
            }
        },
        {
            "attributes": {
                "OBJECTID": 546,
                "FACILITYID": null,
                "NAME": "WASHINGTON ST/COREY RD",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Boston",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "65",
                "DESCRIPT": " ",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7919295.006778173,
                "y": 5212406.540335004
            }
        },
        {
            "attributes": {
                "OBJECTID": 547,
                "FACILITYID": null,
                "NAME": "WASHINGTON ST/COREY RD",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Boston",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "65",
                "DESCRIPT": " ",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7919312.1169718355,
                "y": 5212389.564870901
            }
        },
        {
            "attributes": {
                "OBJECTID": 548,
                "FACILITYID": null,
                "NAME": "WASHINGTON ST/COMM AVE",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Boston",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "65",
                "DESCRIPT": " ",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7919549.658283259,
                "y": 5212598.139987154
            }
        },
        {
            "attributes": {
                "OBJECTID": 549,
                "FACILITYID": null,
                "NAME": "WASHINGTON ST/COMM AVE",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Boston",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "65",
                "DESCRIPT": " ",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7919560.313001289,
                "y": 5212572.9741079025
            }
        },
        {
            "attributes": {
                "OBJECTID": 550,
                "FACILITYID": null,
                "NAME": "WASHINGTON ST/EUSTON RD",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Boston",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "65",
                "DESCRIPT": " ",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7919755.630513311,
                "y": 5212745.206795199
            }
        },
        {
            "attributes": {
                "OBJECTID": 551,
                "FACILITYID": null,
                "NAME": "WASHINGTON ST/EUSTON RD",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Boston",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "65",
                "DESCRIPT": " ",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7919770.737049249,
                "y": 5212726.774982454
            }
        },
        {
            "attributes": {
                "OBJECTID": 552,
                "FACILITYID": null,
                "NAME": "HARVARD AVE/BRIGHTON AVE",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Boston",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "66",
                "DESCRIPT": " ",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7918363.551385022,
                "y": 5213972.016011077
            }
        },
        {
            "attributes": {
                "OBJECTID": 553,
                "FACILITYID": null,
                "NAME": "HARVARD AVE/BRIGHTON AVE",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Boston",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "66",
                "DESCRIPT": " ",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7918396.738455155,
                "y": 5213970.712987437
            }
        },
        {
            "attributes": {
                "OBJECTID": 554,
                "FACILITYID": null,
                "NAME": "HARVARD ST/COMM AVE",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Boston",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "66",
                "DESCRIPT": " ",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7918228.309080144,
                "y": 5213562.531503669
            }
        },
        {
            "attributes": {
                "OBJECTID": 555,
                "FACILITYID": null,
                "NAME": "HARVARD ST/COMM AVE",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Boston",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "66",
                "DESCRIPT": " ",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7918262.963369849,
                "y": 5213548.215430999
            }
        },
        {
            "attributes": {
                "OBJECTID": 556,
                "FACILITYID": null,
                "NAME": "HUNTINGTON AVE/JAMAICA WAY",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Boston",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "66",
                "DESCRIPT": " ",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7916190.454189205,
                "y": 5210852.915127696
            }
        },
        {
            "attributes": {
                "OBJECTID": 557,
                "FACILITYID": null,
                "NAME": "HUNTINGTON AVE/JAMAICA WAY",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Boston",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "66",
                "DESCRIPT": " ",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7916182.5253025275,
                "y": 5210813.7268133825
            }
        },
        {
            "attributes": {
                "OBJECTID": 558,
                "FACILITYID": null,
                "NAME": "HUNTINGTON AVE/PARKERHILL AVE",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Boston",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "66",
                "DESCRIPT": " ",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7915898.165074637,
                "y": 5211000.749492841
            }
        },
        {
            "attributes": {
                "OBJECTID": 559,
                "FACILITYID": null,
                "NAME": "HUNTINGTON AVE/PARKERHILL AVE",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Boston",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "66",
                "DESCRIPT": " ",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7915868.719459347,
                "y": 5211042.349783827
            }
        },
        {
            "attributes": {
                "OBJECTID": 560,
                "FACILITYID": null,
                "NAME": "HUNTINGTON AVE/MISSION ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Boston",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "66",
                "DESCRIPT": " ",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7915613.48953252,
                "y": 5211013.590745016
            }
        },
        {
            "attributes": {
                "OBJECTID": 561,
                "FACILITYID": null,
                "NAME": "HUNTINGTON AVE/MISSION ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Boston",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "66",
                "DESCRIPT": " ",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7915630.245045734,
                "y": 5211057.779849868
            }
        },
        {
            "attributes": {
                "OBJECTID": 562,
                "FACILITYID": null,
                "NAME": "HUNTINGTON AVE/WATI ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Boston",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "66",
                "DESCRIPT": " ",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7915488.180239777,
                "y": 5211051.647111043
            }
        },
        {
            "attributes": {
                "OBJECTID": 563,
                "FACILITYID": null,
                "NAME": "HUNTINGTON AVE/WATI ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Boston",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "66",
                "DESCRIPT": " ",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7915500.778495019,
                "y": 5211087.449513621
            }
        },
        {
            "attributes": {
                "OBJECTID": 564,
                "FACILITYID": null,
                "NAME": "COREY ST/WELD ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Boston",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "51",
                "DESCRIPT": " ",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7921556.520455792,
                "y": 5204772.543566612
            }
        },
        {
            "attributes": {
                "OBJECTID": 565,
                "FACILITYID": null,
                "NAME": "COREY ST/WELD ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Boston",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "51",
                "DESCRIPT": " ",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7921547.575575298,
                "y": 5204751.86018238
            }
        },
        {
            "attributes": {
                "OBJECTID": 566,
                "FACILITYID": null,
                "NAME": "WELD ST/WILLOW ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Boston",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "51",
                "DESCRIPT": " ",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7921020.122752446,
                "y": 5204808.377621973
            }
        },
        {
            "attributes": {
                "OBJECTID": 567,
                "FACILITYID": null,
                "NAME": "WELD ST/WILLOW ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Boston",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "51",
                "DESCRIPT": " ",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7921025.793325774,
                "y": 5204836.791297207
            }
        },
        {
            "attributes": {
                "OBJECTID": 568,
                "FACILITYID": null,
                "NAME": "WELD ST/MAPLE ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Boston",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "51",
                "DESCRIPT": " ",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7921167.793405897,
                "y": 5204758.697530316
            }
        },
        {
            "attributes": {
                "OBJECTID": 569,
                "FACILITYID": null,
                "NAME": "WELD ST/MAPLE ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Boston",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "51",
                "DESCRIPT": " ",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7921165.295718981,
                "y": 5204734.116782623
            }
        },
        {
            "attributes": {
                "OBJECTID": 570,
                "FACILITYID": null,
                "NAME": "WELD ST/RUSSETT RD",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Boston",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "51",
                "DESCRIPT": " ",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7920657.097063283,
                "y": 5205000.371455691
            }
        },
        {
            "attributes": {
                "OBJECTID": 571,
                "FACILITYID": null,
                "NAME": "WELD ST/RUSSETT RD",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Boston",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "51",
                "DESCRIPT": " ",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7920676.409316328,
                "y": 5204987.442071456
            }
        },
        {
            "attributes": {
                "OBJECTID": 572,
                "FACILITYID": null,
                "NAME": "WELD ST/MANTHORNE ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Boston",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "51",
                "DESCRIPT": " ",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7920886.02024049,
                "y": 5204960.9377476
            }
        },
        {
            "attributes": {
                "OBJECTID": 573,
                "FACILITYID": null,
                "NAME": "WELD ST/CHURCHE ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Boston",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "51",
                "DESCRIPT": " ",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7920319.533844952,
                "y": 5204968.322525564
            }
        },
        {
            "attributes": {
                "OBJECTID": 574,
                "FACILITYID": null,
                "NAME": "WELD ST/CHURCHE ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Boston",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "51",
                "DESCRIPT": " ",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7920338.193422746,
                "y": 5204983.266126952
            }
        },
        {
            "attributes": {
                "OBJECTID": 575,
                "FACILITYID": null,
                "NAME": "WELD ST/W ROXBURY PKWAY",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Boston",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "51",
                "DESCRIPT": " ",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7919961.523882148,
                "y": 5205074.7258978505
            }
        },
        {
            "attributes": {
                "OBJECTID": 576,
                "FACILITYID": null,
                "NAME": "WELD ST/W ROXBURY PKWAY",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Boston",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "51",
                "DESCRIPT": " ",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7919920.767511987,
                "y": 5205086.222462386
            }
        },
        {
            "attributes": {
                "OBJECTID": 577,
                "FACILITYID": null,
                "NAME": "WELD ST/BURNSIDE AVE",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Boston",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "51",
                "DESCRIPT": " ",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7919793.667389079,
                "y": 5205008.673873283
            }
        },
        {
            "attributes": {
                "OBJECTID": 578,
                "FACILITYID": null,
                "NAME": "WELD ST/BURNSIDE AVE",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Boston",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "51",
                "DESCRIPT": " ",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7919771.8331323005,
                "y": 5205028.198374059
            }
        },
        {
            "attributes": {
                "OBJECTID": 579,
                "FACILITYID": null,
                "NAME": "VFW PARKWAY/COREY ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Boston",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "51",
                "DESCRIPT": " ",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7921764.434405678,
                "y": 5205018.0497995755
            }
        },
        {
            "attributes": {
                "OBJECTID": 580,
                "FACILITYID": null,
                "NAME": "WELD ST/MANTHORNE ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Boston",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "51",
                "DESCRIPT": " ",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7920864.172554071,
                "y": 5204951.763754881
            }
        },
        {
            "attributes": {
                "OBJECTID": 581,
                "FACILITYID": null,
                "NAME": "WELD ST/RUSKIN ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Boston",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "51",
                "DESCRIPT": " ",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7921318.029447587,
                "y": 5204788.519063407
            }
        },
        {
            "attributes": {
                "OBJECTID": 582,
                "FACILITYID": null,
                "NAME": "WELD ST/RUSKIN ST",
                "OWNER": null,
                "OWNTYPE": null,
                "SUBTYPEFIELD": null,
                "FEATURECODE": null,
                "FULLADDR": null,
                "MUNICIPALITY": "Boston",
                "STATE": "MA",
                "CAPTUREMETH": null,
                "LOCATIONTYPE": "51",
                "DESCRIPT": " ",
                "FACAREA": null,
                "AGENCYURL": null,
                "OPERDAYS": null,
                "OPERHOURS": null,
                "CONTACT": null,
                "PHONE": null,
                "EMAIL": null
            },
            "geometry": {
                "x": -7921308.1645622095,
                "y": 5204792.299233785
            }
        }
    ]
"""