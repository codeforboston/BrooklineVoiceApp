import requests
import logging

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


POLICE_STATION_ID = 10

CANDIDATES_PATH = "candidates"
LOCATION_PATH = "location"
X_PATH = "x"
Y_PATH = "y"
FULL_ADDR_PATH = "FULLADDR"


def get_nearest_police_station_response(address):
    """
    Queries the Brookline arcgis server for the nearest police station

    :param address: Address string to query
    :return: Json data object response
    """
    logger.debug('Finding closest police station for address: ' + str(address))

    url = MAPSERVER_URL.format(POLICE_STATION_ID)
    headers = {CONTENT_TYPE_HEADER: "application/x-www-form-urlencoded"}
    payload = {
        F_PARAM: "json",
        RETURN_GEOMETRY_PARAM: "true",
        SPATIAL_REL_PARAM: "esriSpatialRelIntersects",
        GEOMETRY_TYPE_PARAM: "esriGeometryPoint",
        INSR_PARAM: "4326",
        OUT_FIELDS_PARAM: "*",
        OUTSR_PARAM: "4326",
        GEOMETRY_PARAM: geocode_address(address)
    }
    with requests.Session() as session:
        response = session.post(url, headers=headers, data=payload)

    logger.debug('Got response from Brookline arcgis: ' + str(response))
    return response.json()



def geocode_address(address):
    """
    Retrieves address candidates with coordinates for a given address

    :param address: Address string to query
    :return: List of coordinates in the form [x, y]
    """

    candidate = _get_first_address_candidate(address)
    location = candidate[LOCATION_PATH]

    logger.debug('Got location for address: ' + str(location))
    return [location[X_PATH], location[Y_PATH]]



def _get_first_address_candidate(address):
    """
    Retrieves the first address candidate for a given address

    :param address: Address string to query
    :return: Json response object
    """

    url_params = {
        F_PARAM: "json",
        SINGLE_LINE_PARAM: address,
        OUT_FIELDS_PARAM: "*",
        OUTSR_PARAM: "4326"
    }
    with requests.Session() as session:
        response = session.get(GEOCODE_URL, params=url_params)

    logger.debug('Got response: ' + str(response))
    return response.json()[CANDIDATES_PATH][0]
