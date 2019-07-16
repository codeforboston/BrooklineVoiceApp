""" Utilities for interacting with the Brookline argGIS server """
from enum import Enum
import json
import logging
import typing

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
    POLLING_LOCATION = 21


CANDIDATES_PATH = "candidates"
LOCATION_PATH = "location"
X_PATH = "x"
Y_PATH = "y"
FULL_ADDR_PATH = "FULLADDR"
SPATIAL_REFERENCE_PATH = "spatialReference"



def get_first_address_candidate(address: str,
    _requests: typing.ClassVar = requests) -> object:
    """
    Retrieves the first address candidate for a given address

    :param address: Address string to query
    :param _requests: Requests library object
    :return: Json response object address and spatial reference
    """

    url_params = {
        F_PARAM: "json",
        SINGLE_LINE_PARAM: address,
        OUT_FIELDS_PARAM: "*",
        OUTSR_PARAM: "102100"
    }
    with _requests.Session() as session:
        response = session.get(GEOCODE_URL, params=url_params)

    logger.debug('Got address candidate response: ' + str(response))
    candidate_address = response.json()[CANDIDATES_PATH][0]
    spatial_reference = response.json()[SPATIAL_REFERENCE_PATH]
    return candidate_address, spatial_reference



def geocode_address(address: str,
    _get_first_address_candidate: callable = get_first_address_candidate) -> dict:
    """
    Retrieves address candidates with coordinates for a given address

    :param address: Address string to query
    :param _get_first_address_candidate: injectable function for test
    :return: Dictionary of coordinates with associated spatial reference
    """
    try:
        candidate, spatial_reference = _get_first_address_candidate(address)
        location = candidate[LOCATION_PATH]
        location[SPATIAL_REFERENCE_PATH] = spatial_reference
    except IndexError:
        return {}

    return location



def get_nearest_feature_json(address: str,
    map_feature_id: MapFeatureID,
    _requests: typing.ClassVar = requests,
    _geocode_address: callable = geocode_address) -> object:
    """
    Gets the information of the provided map feature from Brookline argis server

    :param address: Adress string to use in query
    :param map_feature_id: MapFeatureID to query the server for
    :param _requests: Requests library object
    :param _geocode_address: injectable function for test
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
        GEOMETRY_PARAM: json.dumps(_geocode_address(address))
    }
    with _requests.Session() as session:
        response = session.post(url, headers=headers, data=payload)

    logger.debug('Got response from Brookline arcgis: ' + str(response))
    return response.json()



def get_nearest_police_station_json(address: str,
    _get_nearest_feature_json: callable = get_nearest_feature_json,
    _geocode_address: callable = geocode_address) -> object:
    """
    Queries the Brookline arcgis server for the nearest police station

    :param address: Address string to query
    :return: Json data object response
    """
    logger.debug('Finding closest police station for address: ' + str(address))
    location = _geocode_address(address)
    coordinates = [location['x'], location['y']]
    custom_geocode = lambda arg: coordinates
    return _get_nearest_feature_json(address, MapFeatureID.POLICE_STATION,
                                     _geocode_address=custom_geocode)



def get_polling_locations(address: str,
                          _get_nearest_feature_json: callable = get_nearest_feature_json,
                          _geocode_address: callable = geocode_address) -> object:
    """
    Queries the Brookline arcgis server for nearby polling stations

    :param address: Address string to query
    :param _get_nearest_feature_json: Callable to get the arcgis server response
    :param _geocode_address: Callable to transform string address to [x,y]
    :return: Json data object response
    """
    logger.debug('Finding polling stations for address: ' + str(address))
    location = _geocode_address(address)
    coordinates = [location['x'], location['y']]
    custom_geocode = lambda arg: coordinates
    return _get_nearest_feature_json(address, MapFeatureID.POLLING_LOCATION,
                                     _geocode_address=custom_geocode)



def get_trash_day_json(address: str,
    _get_nearest_feature_json: callable = get_nearest_feature_json) -> object:
    """
    Queries the Brookline arcgis server for trash day

    :param address: Address string to query
    :return: Json object response from the server
    """
    logger.debug('Finding trash day for address: ' + str(address))
    return _get_nearest_feature_json(address, MapFeatureID.TRASH_DAY)
