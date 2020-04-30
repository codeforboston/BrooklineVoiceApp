##################################################################
# Mocked returns for patched functions that access web resources #
##################################################################


GET_POLICE_STATION_API_MOCK = {
    "displayFieldName": "NAME",
    "fieldAliases": {
        "OBJECTID": "OBJECTID",
        "FACILITYID": "Facility Identifier",
        "NAME": "Name of Facility",
        "OWNER": "Owner Name",
        "OWNTYPE": "Owner Type",
        "SUBTYPEFIELD": "Subtype Field",
        "FEATURECODE": "Feature Code",
        "FULLADDR": "Full Address",
        "AGENCYURL": "Website",
        "OPERDAYS": "Operational Days",
        "OPERHOURS": "Operational Hours",
        "CONTACT": "Contact Name",
        "PHONE": "Phone",
        "EMAIL": "Email"
    },
    "features": [
        {
            "attributes": {
                "OBJECTID": 1,
                "FACILITYID": None,
                "NAME": "Brookline Public Safety HQ",
                "OWNER": "Town of Brookline",
                "OWNTYPE": None,
                "SUBTYPEFIELD": None,
                "FEATURECODE": None,
                "FULLADDR": "350 Washington St, Brookline, MA 02445",
                "AGENCYURL": "http://www.brooklinepolice.com/",
                "OPERDAYS": "Other",
                "OPERHOURS": "Other",
                "CONTACT": None,
                "PHONE": "617-730-2222",
                "EMAIL": None
            },
            "geometry": {
                "x": -71.121409303637222,
                "y": 42.333789044263746
            }
        }
    ]
}

NO_RESULTS_GET_POLICE_STATION_API_MOCK = {
    "displayFieldName": "NAME",
    "fieldAliases": {
        "OBJECTID": "OBJECTID",
        "FACILITYID": "Facility Identifier",
        "NAME": "Name of Facility",
        "OWNER": "Owner Name",
        "OWNTYPE": "Owner Type",
        "SUBTYPEFIELD": "Subtype Field",
        "FEATURECODE": "Feature Code",
        "FULLADDR": "Full Address",
        "AGENCYURL": "Website",
        "OPERDAYS": "Operational Days",
        "OPERHOURS": "Operational Hours",
        "CONTACT": "Contact Name",
        "PHONE": "Phone",
        "EMAIL": "Email"
    },
    "features": []
}

GEOCODE_MOCK = {
    "spatialReference": {
        "wkid": 4326,
        "latestWkid": 4326
    },
    "x": -71.120614336337198,
    "y": 42.334020535512529,
    "z": 0
}

LOCATION_MOCK = {
    "x": -71.120614336337198,
    "y": 42.334020535512529,
    "z": 0
}

SPACIAL_REFERENCE_MOCK = {
    "wkid": 4326,
    "latestWkid": 4326
}

ADDRESS_CANDIDATE_MOCK = {
    "address": "333 WASHINGTON ST",
    "location": {
        "x": -71.120614336337198,
        "y": 42.334020535512529,
        "z": 0
    },
    "score": 100,
    "attributes": {
        "Loc_name": "Building",
        "Score": 100,
        "Match_addr": "333 WASHINGTON ST"
    }
}

GET_ADDRESS_CANDIDATES_API_MOCK = {
    "spatialReference": {
        "wkid": 4326,
        "latestWkid": 4326
    },
    "candidates": [
        {
            "address": "333 WASHINGTON ST",
            "location": {
                "x": -71.120614336337198,
                "y": 42.334020535512529,
                "z": 0
            },
            "score": 100,
            "attributes": {
                "Loc_name": "Building",
                "Score": 100,
                "Match_addr": "333 WASHINGTON ST"
            }
        }
    ]
}

GEOCODE_ADDRESS_MOCK = {
    'geometry':{'x':-7917110.640673582,'y':5211147.471469648}}

GET_TRASH_PICKUP_API_MOCK = {
    "displayFieldName": "DISTRICTID",
    "fieldAliases": {
        "OBJECTID": "OBJECTID",
        "DISTRICTID": "District ID",
        "NAME": "District Name",
        "AGENCY": "Agency",
        "AGENCYURL": "Website",
        "CONTACT": "Contact Name",
        "PHONE": "Phone",
        "EMAIL": "Email",
        "SUBTYPEFIELD": "Subtype Field",
        "SCHEDULE": "Schedule",
        "DESCRIPT": "Additional Information",
        "MONDAY": "Monday",
        "TUESDAY": "Tuesday",
        "WEDNESDAY": "Wednesday",
        "THURSDAY": "Thursday",
        "FRIDAY": "Friday",
        "SATURDAY": "Saturday",
        "SUNDAY": "Sunday",
        "GlobalID": "GlobalID"
    },
    "features": [
        {
            "attributes": {
                "OBJECTID": 2,
                "DISTRICTID": "1",
                "NAME": "Wednesday Trash",
                "AGENCY": "Town of Brookline",
                "AGENCYURL": "http://ma-brookline.civicplus.com/820/Trash-Recycling-Information",
                "CONTACT": "Brookline Public Works",
                "PHONE": "null",
                "EMAIL": "null",
                "SUBTYPEFIELD": 0,
                "SCHEDULE": "Weekly",
                "DESCRIPT": "http://ma-brookline.civicplus.com/834/Holiday-Schedule-Christmas-Tree-Pick-Up",
                "MONDAY": "No",
                "TUESDAY": "No",
                "WEDNESDAY": "Yes",
                "THURSDAY": "No",
                "FRIDAY": "No",
                "SATURDAY": "No",
                "SUNDAY": "No",
                "GlobalID": "{20538BBF-EB83-4CCD-B1E8-93EF36554413}"
            },
            "geometry": {
                "x": -71.121409303637222,
                "y": 42.333789044263746
            }
        }
    ]
}

NO_RESPONSE_TRASH_PICKUP_API_MOCK = {
    "displayFieldName": "DISTRICTID",
    "fieldAliases": {
        "OBJECTID": "OBJECTID",
        "DISTRICTID": "District ID",
        "NAME": "District Name",
        "AGENCY": "Agency",
        "AGENCYURL": "Website",
        "CONTACT": "Contact Name",
        "PHONE": "Phone",
        "EMAIL": "Email",
        "SUBTYPEFIELD": "Subtype Field",
        "SCHEDULE": "Schedule",
        "DESCRIPT": "Additional Information",
        "MONDAY": "Monday",
        "TUESDAY": "Tuesday",
        "WEDNESDAY": "Wednesday",
        "THURSDAY": "Thursday",
        "FRIDAY": "Friday",
        "SATURDAY": "Saturday",
        "SUNDAY": "Sunday",
        "GlobalID": "GlobalID"
    },
    "features": []
}
NO_RESPONSE_VOTING_PRECINCT_API_MOCK = {
    "displayFieldName": "NAME",
    "fieldAliases": {
        "OBJECTID": "OBJECTID",
        "PRECINCTID": "Precinct ID",
        "NAME": "Precinct Name",
        "COUNTY": "County",
        "LASTUPDATE": "Last Update Date",
        "LASTEDITOR": "Last Editor",
        "SHAPE_Length": "SHAPE_Length",
        "SHAPE_Area": "SHAPE_Area",
        "STR_NUM": "STR_NUM",
        "STREET": "STREET",
        "ADDRESS": "ADDRESS",
        "LOC_DESC": "LOC_DESC"
    },
    "geometryType": "esriGeometryPolygon",
    "spatialReference": {
        "wkid": 102100,
        "latestWkid": 3857
    },
    "fields": [
        {
            "name": "OBJECTID",
            "type": "esriFieldTypeOID",
            "alias": "OBJECTID"
        },
        {
            "name": "PRECINCTID",
            "type": "esriFieldTypeString",
            "alias": "Precinct ID",
            "length": 10
        },
        {
            "name": "NAME",
            "type": "esriFieldTypeString",
            "alias": "Precinct Name",
            "length": 50
        },
        {
            "name": "COUNTY",
            "type": "esriFieldTypeString",
            "alias": "County",
            "length": 50
        },
        {
            "name": "LASTUPDATE",
            "type": "esriFieldTypeDate",
            "alias": "Last Update Date",
            "length": 8
        },
        {
            "name": "LASTEDITOR",
            "type": "esriFieldTypeString",
            "alias": "Last Editor",
            "length": 50
        },
        {
            "name": "SHAPE_Length",
            "type": "esriFieldTypeDouble",
            "alias": "SHAPE_Length"
        },
        {
            "name": "SHAPE_Area",
            "type": "esriFieldTypeDouble",
            "alias": "SHAPE_Area"
        },
        {
            "name": "STR_NUM",
            "type": "esriFieldTypeString",
            "alias": "STR_NUM",
            "length": 8
        },
        {
            "name": "STREET",
            "type": "esriFieldTypeString",
            "alias": "STREET",
            "length": 32
        },
        {
            "name": "ADDRESS",
            "type": "esriFieldTypeString",
            "alias": "ADDRESS",
            "length": 64
        },
        {
            "name": "LOC_DESC",
            "type": "esriFieldTypeString",
            "alias": "LOC_DESC",
            "length": 128
        }
    ],
    "features": [

    ]
}

GET_VOTING_PRECINCT_API_MOCK = {
    "displayFieldName": "NAME",
    "fieldAliases": {
        "OBJECTID": "OBJECTID",
        "PRECINCTID": "Precinct ID",
        "NAME": "Precinct Name",
        "COUNTY": "County",
        "LASTUPDATE": "Last Update Date",
        "LASTEDITOR": "Last Editor",
        "SHAPE_Length": "SHAPE_Length",
        "SHAPE_Area": "SHAPE_Area",
        "STR_NUM": "STR_NUM",
        "STREET": "STREET",
        "ADDRESS": "ADDRESS",
        "LOC_DESC": "LOC_DESC"
    },
    "geometryType": "esriGeometryPolygon",
    "spatialReference": {
        "wkid": 102100,
        "latestWkid": 3857
    },
    "fields": [
        {
            "name": "OBJECTID",
            "type": "esriFieldTypeOID",
            "alias": "OBJECTID"
        },
        {
            "name": "PRECINCTID",
            "type": "esriFieldTypeString",
            "alias": "Precinct ID",
            "length": 10
        },
        {
            "name": "NAME",
            "type": "esriFieldTypeString",
            "alias": "Precinct Name",
            "length": 50
        },
        {
            "name": "COUNTY",
            "type": "esriFieldTypeString",
            "alias": "County",
            "length": 50
        },
        {
            "name": "LASTUPDATE",
            "type": "esriFieldTypeDate",
            "alias": "Last Update Date",
            "length": 8
        },
        {
            "name": "LASTEDITOR",
            "type": "esriFieldTypeString",
            "alias": "Last Editor",
            "length": 50
        },
        {
            "name": "SHAPE_Length",
            "type": "esriFieldTypeDouble",
            "alias": "SHAPE_Length"
        },
        {
            "name": "SHAPE_Area",
            "type": "esriFieldTypeDouble",
            "alias": "SHAPE_Area"
        },
        {
            "name": "STR_NUM",
            "type": "esriFieldTypeString",
            "alias": "STR_NUM",
            "length": 8
        },
        {
            "name": "STREET",
            "type": "esriFieldTypeString",
            "alias": "STREET",
            "length": 32
        },
        {
            "name": "ADDRESS",
            "type": "esriFieldTypeString",
            "alias": "ADDRESS",
            "length": 64
        },
        {
            "name": "LOC_DESC",
            "type": "esriFieldTypeString",
            "alias": "LOC_DESC",
            "length": 128
        }
    ],
    "features": [
        {
            "attributes": {
                "OBJECTID": 19,
                "PRECINCTID": "6",
                "NAME": "Precinct 6 - Vote at 115 Greenough St",
                "COUNTY": "Norfolk",
                "LASTUPDATE": 'null',
                "LASTEDITOR": 'null',
                "SHAPE_Length": 15810.092868688193,
                "SHAPE_Area": 7070142.9764727177,
                "STR_NUM": "115",
                "STREET": "GREENOUGH ST",
                "ADDRESS": "115 GREENOUGH ST",
                "LOC_DESC": "BHS Schluntz Gymnasium, 115 Greenough Street"
            },
        }
    ]
}

GET_LIBRARY_API_MOCK = {
    "features": [
        {
            "attributes": {
                "OBJECTID": 1,
                "FACILITYID": "None",
                "NAME": "Coolidge Corner Library",
                "OWNER": "Town of Brookline",
                "OWNTYPE": "None",
                "SUBTYPEFIELD": "None",
                "FEATURECODE": "None",
                "FULLADDR": "31 Pleasant St, Brookline, MA 02446",
                "AGENCYURL": "http://www.brooklinelibrary.org/",
                "OPERDAYS": "Other",
                "OPERHOURS": "Other",
                "CONTACT": "None",
                "PHONE": "617-730-2380",
                "EMAIL": "http://www.brooklinelibrary.org/about/email"
            },
            "geometry": {
                "x": -7916949.550832789,
                "y": 5212579.537906414
            }
        },
        {
            "attributes": {
                "OBJECTID": 2,
                "FACILITYID": "None",
                "NAME": "Main Library",
                "OWNER": "Town of Brookline",
                "OWNTYPE": "None",
                "SUBTYPEFIELD": "None",
                "FEATURECODE": "None",
                "FULLADDR": "361 Washington St, Brookline, MA 02445",
                "AGENCYURL": "http://www.brooklinelibrary.org/",
                "OPERDAYS": "Other",
                "OPERHOURS": "Other",
                "CONTACT": "None",
                "PHONE": "617-730-2370",
                "EMAIL": "http://www.brooklinelibrary.org/about/email"
            },
            "geometry": {
                "x": -7917194.260973867,
                "y": 5211229.5272506215
            }
        },
        {
            "attributes": {
                "OBJECTID": 3,
                "FACILITYID": "None",
                "NAME": "Putterham Branch Library",
                "OWNER": "Town of Brookline",
                "OWNTYPE": "None",
                "SUBTYPEFIELD": "None",
                "FEATURECODE": "None",
                "FULLADDR": "959 W Roxbury Pky, Brookline, MA 02467",
                "AGENCYURL": "http://www.brooklinelibrary.org/",
                "OPERDAYS": "Other",
                "OPERHOURS": "Other",
                "CONTACT": "None",
                "PHONE": "617-730-2385",
                "EMAIL": "http://www.brooklinelibrary.org/about/email"
            },
            "geometry": {
                "x": -7920391.679580264,
                "y": 5206399.414108847
            }
        }
    ]
}

GET_SCHOOL_DISTRICT_API_MOCK = {
    "displayFieldName": "NAME",
    "fieldAliases": {
        "OBJECTID": "OBJECTID",
        "NAME": "School Name",
        "DISTRCTNAME": "School District Name",
        "SCHOOLAREA": "Area in Square Miles",
        "LASTUPDATE": "Last Update Date",
        "LASTEDITOR": "Last Editor"
    },
    "features": [
        {
            "attributes": {
                "OBJECTID": 1,
                "NAME": "Brookline School",
                "DISTRCTNAME": "Brookline",
                "SCHOOLAREA": "1",
                "LASTUPDATE": None,
                "LASTEDITOR": None
            },
            "geometry": {
                "x": -7920615.96685251,
                "y": 5205180.75934551
            }
        }
    ]
}

NO_RESULTS_GET_SCHOOL_DISTRICT_API_MOCK = {
    "displayFieldName": "NAME",
    "fieldAliases": {
        "OBJECTID": "OBJECTID",
        "NAME": "School Name",
        "DISTRCTNAME": "School District Name",
        "SCHOOLAREA": "Area in Square Miles",
        "LASTUPDATE": "Last Update Date",
        "LASTEDITOR": "Last Editor"
    },
    "features": []
}
