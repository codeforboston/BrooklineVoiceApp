""" Utilities for interacting with the Brookline argGIS server """
from enum import Enum
import json
import logging
import requests


logger = logging.getLogger(__name__)


CONTENT_TYPE_HEADER = "Content-Type"

F_PARAM = "f"
RETURN_GEOMETRY_PARAM = "returnGeometry"
SPATIAL_REL_PARAM = "spatialRel"
GEOMETRY_TYPE_PARAM = "geometryType"
GEOMETRY_PARAM = "geometry"
INSR_PARAM = "inSR"
OUTSR_PARAM = "outSR"
OUT_FIELDS_PARAM = "outFields"
SINGLE_LINE_PARAM = "SingleLine"

MAPSERVER_URL = \
    "http://gisweb.brooklinema.gov/arcgis/rest/services/MyGov/GovernmentServices/MapServer/{}/query"
GEOCODE_URL = \
    "http://gisweb.brooklinema.gov/arcgis/rest/services/Composite_WhereAmI/GeocodeServer/findAddressCandidates"


class MapFeatureID(Enum):
    """Brookline GIS feature types"""
    POLICE_STATION = 10
    TRASH_DAY = 12

CANDIDATES_PATH = "candidates"
LOCATION_PATH = "location"
X_PATH = "x"
Y_PATH = "y"
FULL_ADDR_PATH = "FULLADDR"
SPATIAL_REFERENCE_PATH = "spatialReference"


def get_nearest_police_station_json(address):
    """
    Queries the Brookline arcgis server for the nearest police station

    :param address: Address string to query
    :return: Json data object response
    """
    logger.debug('Finding closest police station for address: ' + str(address))
    return get_nearest_feature_json(address, MapFeatureID.POLICE_STATION)

def get_trash_day_json(address):
    """
    Queries the Brookline arcgis server for trash day

    :param address: Address string to query
    :return: Json object response from the server
    """
    logger.debug('Finding trash day for address: ' + str(address))
    return get_nearest_feature_json(address, MapFeatureID.TRASH_DAY)

def get_nearest_feature_json(address, map_feature_id):
    """
    Gets the information of the provided map feature from Brookline argis server

    :param address: Adress string to use in query
    :param map_feature_id: MapFeatureID to query the server for
    :return: Json data object response
    """


    if not isinstance(map_feature_id, MapFeatureID):
        raise Exception('get_nearest_feature_json() called with invalid feature ID')

    url = MAPSERVER_URL.format(map_feature_id.value)
    headers = {CONTENT_TYPE_HEADER: "application/x-www-form-urlencoded"}
    payload = {
        F_PARAM: "json",
        RETURN_GEOMETRY_PARAM: "true",
        SPATIAL_REL_PARAM: "esriSpatialRelIntersects",
        GEOMETRY_TYPE_PARAM: "esriGeometryPoint",
        INSR_PARAM: "102100",
        OUT_FIELDS_PARAM: "*",
        OUTSR_PARAM: "102100",
        GEOMETRY_PARAM: json.dumps(geocode_address(address))
    }
    with requests.Session() as session:
        response = session.post(url, headers=headers, data=payload)

    logger.debug('Got response from Brookline arcgis: ' + str(response))
    return response.json()



def geocode_address(address):
    """
    Retrieves address candidates with coordinates for a given address

    :param address: Address string to query
    :return: Dictionary of coordinates with associated spatial reference
    """
    try:
        candidate, spatial_reference = _get_first_address_candidate(address)
        location = candidate[LOCATION_PATH]
        location[SPATIAL_REFERENCE_PATH] = spatial_reference
    except IndexError:
        return {}

    return location



def _get_first_address_candidate(address):
    """
    Retrieves the first address candidate for a given address

    :param address: Address string to query
    :return: Json response object address and spatial reference
    """

    url_params = {
        F_PARAM: "json",
        SINGLE_LINE_PARAM: address,
        OUT_FIELDS_PARAM: "*",
        OUTSR_PARAM: "102100"
    }
    with requests.Session() as session:
        response = session.get(GEOCODE_URL, params=url_params)

    logger.debug('Got address candidate response: ' + str(response))
    candidate_address = response.json()[CANDIDATES_PATH][0]
    spatial_reference = response.json()[SPATIAL_REFERENCE_PATH]
    return candidate_address, spatial_reference
