
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

LOCATION_MOCK = {
    "x": -71.120614336337198,
    "y": 42.334020535512529,
    "z": 0
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
