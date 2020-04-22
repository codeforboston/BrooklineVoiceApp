"""Alexa intent used to find school district associated with address"""

import logging

from mycity.intents import intent_constants
from mycity.mycity_response_data_model import MyCityResponseDataModel
from mycity.utils.address_utils import set_address_in_session
from mycity.utils.brookline_arcgis_api_utils import get_sorted_school_district_json

logger = logging.getLogger(__name__)

CARD_TITLE_SCHOOL_DISTRICT = "Nearest School District"

OUTPUT_SPEECH_TEMPLATE = \
    "The nearest school district to you is {}."

FEATURES_PATH = "features"
ATTRIBUTES_PATH = "attributes"
NAME_PATH = "NAME"

def find_closest_school_district(mycity_request):
    """
    Finds the closest school district in Brookline
    to a given address

    :param mycity_request: MyCityRequestDataModel object
    :return: MyCityResponseDataModel object
    """
    logger.debug('Finding closest school district')

    response = MyCityResponseDataModel()
    set_address_in_session(mycity_request)
    current_address = mycity_request \
        .session_attributes \
        .get(intent_constants.CURRENT_ADDRESS_KEY)
    logger.debug(current_address)
    if current_address is None:
        response.dialog_directive = "Delegate"
    else:
        response.output_speech = _get_output_speech_for_address(current_address)
        response.card_title = CARD_TITLE_SCHOOL_DISTRICT

    return response


def _get_output_speech_for_address(address):
    """
    Gets the API response and builds an output speech string

    :param address: Current address
    :return: Output speech string
    """

    logger.debug("Getting response for address " + str(address))
    features = get_sorted_school_district_json(address)
    logger.debug("school district response:", features)

    try:
        first_feature = features[0]
        logger.debug(first_feature)
        facility_name = first_feature[ATTRIBUTES_PATH][NAME_PATH]
    except IndexError:
        return intent_constants.NO_RESULTS_RESPONSE

    return OUTPUT_SPEECH_TEMPLATE.format(facility_name)
