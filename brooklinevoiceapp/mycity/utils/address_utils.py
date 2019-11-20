import logging
from math import (
    acos,
    cos,
    degrees,
    radians,
    sin,
)
from operator import itemgetter

from mycity.intents import intent_constants

logger = logging.getLogger(__name__)

# a minute is 1/60th of a degree
MINUTES_PER_DEGREE = 60
# nautical miles are based on the earth's circumference.
# statute miles are what we conventionally refer to as miles (5,280 feet)
STATUTE_MILES_PER_NAUTICAL_MILE = 1.1515


def set_address_in_session(mycity_request):
    """
    Adds an address to the provided session object

    :param mycity_request: MyCityRequestDataModel object
    :return: None
    """

    if 'Address' in mycity_request.intent_variables and \
            'value' in mycity_request.intent_variables['Address']:
        address = mycity_request.intent_variables['Address']['value']
        logger.debug(
            "Setting Address in Session Attributes. Address: {}".format(
                str(address)
            )
        )
        mycity_request.session_attributes[
            intent_constants.CURRENT_ADDRESS_KEY
        ] = address
        if intent_constants.ZIP_CODE_KEY in mycity_request.session_attributes:
            # We clear out any zip code saved if the user has
            # changed the address
            del(mycity_request.session_attributes
                [intent_constants.ZIP_CODE_KEY])


def get_distance(start, end):
    """
    Calculates the distance between two map points. See:
    https://github.com/Esri/my-government-services/blob/85fcf753b4871f0e7c6713f34f49f9812a88cc91/js/carousel.js#L1571

    :param start: Start point for distance calculation.
    :param end: End point for distance calculation.
    :return: Distance between start and end.
    """
    lon1 = start['x']
    lat1 = start['y']
    lon2 = end['x']
    lat2 = end['y']
    theta = lon1 - lon2
    dist = sin(radians(lat1)) * sin(radians(lat2)) \
        + cos(radians(lat1)) * cos(radians(lat2)) * cos(radians(theta))
    dist = acos(dist)
    dist = degrees(dist)
    dist = dist * MINUTES_PER_DEGREE * STATUTE_MILES_PER_NAUTICAL_MILE
    return (dist * 10) / 10


def get_sorted_features(home_coordinates, features):
    """
    Given a home location and a list of features, returns the closest feature
    to home.

    :param home_coordinates: The user's location.
                             {x:longitude, y:latitude}
    :param features: The feature list from an arcgis query response.
    :return: The closest feature.
    """
    # If we don't have an x or y value for home, we can't calculate a closest feature.
    if 'x' not in home_coordinates or 'y' not in home_coordinates:
        return []

    return sorted(features, key=lambda feature: get_distance(home_coordinates, feature['geometry']))
