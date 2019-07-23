from mycity.intents import intent_constants
from math import sin, cos, radians, acos, degrees
from mycity.intents.mock_response import mock_features, mock_home
import logging
import json

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


def get_closest_result():
    closest = {
        'feature': {},
        'distance': 100000000
    }

    for feature in mock_features:
        feat = {
            'x': feature['geometry']['x'],
            'y': feature['geometry']['y']
        }
        dist = get_distance(
            mock_home,
            feat
        )
        if dist < closest['distance']:
            closest = {
                'feature': feature,
                'distance': dist
            }
        print('current: ' + str(dist))
        print('closest: ' + str(closest['distance']))
    print(closest)


get_closest_result()