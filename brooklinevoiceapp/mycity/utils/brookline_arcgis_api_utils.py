""" Utilities for interacting with the Brookline argGIS server """
import json
import logging
import typing
from enum import Enum

import requests

from mycity.utils import address_utils
from mycity.utils.exceptions import NoAddressFound

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

FEATURES_PATH = "features"


class MapFeatureID(Enum):
    """Brookline GIS feature types"""
    POLICE_STATION = 10
    TRASH_DAY = 12
    LIBRARY = 9
    SCHOOL_DISTRICT = 16
    VOTING_PRECINCT = 20

class NonSortedFeatures(Enum):
    """Brookline GIS feature types that shouldn't be sorted"""
    TRASH_DAY = 12
    VOTING_PRECINCT = 20


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
    try:
        candidate_address = response.json()[CANDIDATES_PATH][0]
        spatial_reference = response.json()[SPATIAL_REFERENCE_PATH]
    except (IndexError, KeyError):
        raise NoAddressFound()
    return candidate_address, spatial_reference


def geocode_address(address: str,
                    _get_first_address_candidate: callable = get_first_address_candidate) -> dict:
    """
    Retrieves address candidates with coordinates for a given address

    :param address: Address string to query
    :param _get_first_address_candidate: injectable function for test
    :return: Dictionary of coordinates with associated spatial reference
    """
    candidate, spatial_reference = _get_first_address_candidate(address)
    location = candidate[LOCATION_PATH]
    location[SPATIAL_REFERENCE_PATH] = spatial_reference

    return location


def get_sorted_features_json(address: str,
                             map_feature_id: MapFeatureID,
                             geometry_params: dict,
                             home_address: dict = {},
                             _requests: typing.ClassVar = requests) -> object:
    """
    Gets the information of the provided map feature from Brookline arcgis server

    :param address: Address string to use in query
    :param map_feature_id: MapFeatureID to query the server for
    :param _requests: Requests library object
    :param _geocode_address: injectable function for test
    :return: Json data object response
    """
    if not isinstance(map_feature_id, MapFeatureID):
        raise Exception('get_nearest_feature_json() called with invalid feature ID')

    notSorted = [mapId.value for mapId in NonSortedFeatures]
    url = MAPSERVER_URL.format(map_feature_id.value)
    headers = {CONTENT_TYPE_HEADER: "application/x-www-form-urlencoded"}
    params = {
        F_PARAM: "json",
        RETURN_GEOMETRY_PARAM: "true",
        INSR_PARAM: "102100",
        OUT_FIELDS_PARAM: "*",
        OUTSR_PARAM: "102100",
        **geometry_params
    }
    with _requests.Session() as session:
        response = session.get(url, headers=headers, params=params)

    logger.debug('Got response from Brookline arcgis: ' + repr(response.json()))
    features = response.json()[FEATURES_PATH]
    logger.debug("map:" + str(notSorted))
    if map_feature_id.value in notSorted:
        logger.debug("returning features")
        return features
    return address_utils.get_sorted_features(home_address, features)


def get_sorted_police_station_json(address: str,
                                   _get_sorted_features_json: callable = get_sorted_features_json,
                                   _geocode_address: callable = geocode_address) -> object:
    """
    Queries the Brookline arcgis server for the nearest police station

    :param address: Address string to query
    :return: Json data object response
    """
    logger.debug('Finding closest police station for address: ' + str(address))
    home_address = _geocode_address(address)
    coordinates = '[{},{}]'.format(home_address['x'], home_address['y']) 
    if 'z' in home_address:
        del home_address['z']
            
    geometry_params = {
        SPATIAL_REL_PARAM: "esriSpatialRelIntersects",
        GEOMETRY_TYPE_PARAM: "esriGeometryPoint",
        GEOMETRY_PARAM: coordinates,
    }

    return _get_sorted_features_json(address, MapFeatureID.POLICE_STATION, geometry_params, home_address)


def get_sorted_library_json(address: str,
                                   _get_sorted_features_json: callable = get_sorted_features_json,
                                   _geocode_address: callable = geocode_address) -> object:
    """
    Queries the Brookline arcgis server for the nearest library

    :param address: Address string to query
    :return: Json data object response
    """
    logger.debug('Finding closest library for address: ' + str(address))
    home_address = _geocode_address(address)
    coordinates = '[{},{}]'.format(home_address['x'], home_address['y']) 

    if 'z' in home_address:
        del home_address['z']
            
    geometry_params = {
        SPATIAL_REL_PARAM: "esriSpatialRelIntersects",
        GEOMETRY_TYPE_PARAM: "esriGeometryPoint",
        GEOMETRY_PARAM: coordinates,
    }

    return _get_sorted_features_json(address, MapFeatureID.LIBRARY, geometry_params, home_address)

def get_sorted_school_district_json(address: str,
                            _get_sorted_features_json: callable = get_sorted_features_json,
                            _geocode_address: callable = geocode_address) -> object:
    """
    Queries the Brookline arcgis server for the nearest school district

    :param address: Address string to query
    :return: Json data object response
    """
    logger.debug('Finding closest school district for address: ' + str(address))
    home_address = _geocode_address(address)
    coordinates = '[{},{}]'.format(home_address['x'], home_address['y'])

    if 'z' in home_address:
        del home_address['z']

    geometry_params = {
        SPATIAL_REL_PARAM: "esriSpatialRelIntersects",
        GEOMETRY_TYPE_PARAM: "esriGeometryPolygon",
        GEOMETRY_PARAM: coordinates,
    }

    return _get_sorted_features_json(address, MapFeatureID.SCHOOL_DISTRICT, geometry_params, home_address)

def get_voting_precinct_json(address: str,
                        _get_sorted_features_json: callable = get_sorted_features_json,
                        _geocode_address: callable = geocode_address) -> object:
    """
    Queries the Brookline arcgis server for nearby voting precinct location

    :param address: Address string to query
    :param _get_sorted_features_json: Callable to get the arcgis server response
    :param _geocode_address: Callable to transform string address to [x,y]
    :return: Json data object response
    """
    logger.debug('Finding voting precinct for address: ' + str(address))
    home_address = _geocode_address(address)
    coordinates = '{},{}'.format(home_address['x'], home_address['y']) 
    if 'z' in home_address:
        del home_address['z']

    geometry_params = {
        SPATIAL_REL_PARAM: "esriSpatialRelIntersects",
        GEOMETRY_TYPE_PARAM: "esriGeometryPoint",
        GEOMETRY_PARAM: coordinates,
    }

    return _get_sorted_features_json(address, MapFeatureID.VOTING_PRECINCT, geometry_params)


def get_trash_day_json(address: str,
                       _get_sorted_features_json: callable = get_sorted_features_json,
                       _geocode_address: callable = geocode_address) -> object:
    """
    Queries the Brookline arcgis server for trash day

    :param address: Address string to query
    :return: Json object response from the server
    """
    logger.debug('Finding trash day for address: ' + str(address))
    home_address = _geocode_address(address)
    if 'z' in home_address:
        del home_address['z']
            
    geometry_params = {
        SPATIAL_REL_PARAM: "esriSpatialRelWithin",
        GEOMETRY_TYPE_PARAM: "esriGeometryPoint",
        GEOMETRY_PARAM: json.dumps(home_address),
    }

    return _get_sorted_features_json(address, MapFeatureID.TRASH_DAY, geometry_params)
