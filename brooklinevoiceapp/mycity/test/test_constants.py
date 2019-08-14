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

GEOCODE_ADDRESS_MOCK = [42.35351814, -71.13117064]

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

GET_POLLING_LOCATIONS_API_MOCK = {
    "features": [
        {
            "attributes": {
                "OBJECTID": 1,
                "NAME": "Young Israel of Brookline, 62 Green St (Side En",
                "POLLINGID": "8",
                "FULLADD": "345 HARVARD ST",
                "CITY": "Brookline",
                "STATE": "MA",
                "CONTACT": "Brookline Town Clerk",
                "PHONE": "617-730-2010",
                "EMAIL": "pward@brooklinema.gov",
                "PRECINCT": "Precinct 8"
            },
            "geometry": {
                "x": -7917111.8624876123,
                "y": 5212769.3177538002
            }
        },
        {
            "attributes": {
                "OBJECTID": 2,
                "NAME": "(New) Lincoln School, 19 Kennard Road",
                "POLLINGID": "5",
                "FULLADD": "19 KENNARD RD",
                "CITY": "Brookline",
                "STATE": "MA",
                "CONTACT": "Brookline Town Clerk",
                "PHONE": "617-730-2010",
                "EMAIL": "pward@brooklinema.gov",
                "PRECINCT": "Precinct 5"
            },
            "geometry": {
                "x": -7918086.1184908934,
                "y": 5210343.692659962
            }
        },
        {
            "attributes": {
                "OBJECTID": 3,
                "NAME": "Heath School Gymnasium, 100 Eliot Street",
                "POLLINGID": "14",
                "FULLADD": "100 ELIOT ST",
                "CITY": "Brookline",
                "STATE": "MA",
                "CONTACT": "Brookline Town Clerk",
                "PHONE": "617-730-2010",
                "EMAIL": "pward@brooklinema.gov",
                "PRECINCT": "Precinct 14"
            },
            "geometry": {
                "x": -7920158.8921198044,
                "y": 5210251.6698454535
            }
        }
    ]
}
