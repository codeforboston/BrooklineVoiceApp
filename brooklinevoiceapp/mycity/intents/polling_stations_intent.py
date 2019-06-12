""" Intent for responding to polling station requests """
import logging
from mycity.mycity_response_data_model import MyCityResponseDataModel
from mycity.intents import intent_constants
from mycity.utils.address_utils import set_address_in_session
from mycity.utils.brookline_arcgis_api_utils import get_polling_locations_json


LOGGER = logging.getLogger(__name__)

# User facing strings
CARD_TITLE_POLLING = "Polling Locations"
OUTPUT_SPEECH_TEMPLATE = "The {} polling station in {} is located at {}. "

# Strings used in parsing json data returned by server
FEATURES_PATH = "features"
ATTRIBUTES_PATH = "attributes"
NAME_PATH = "NAME"
PRECINCT_PATH = "PRECINCT"
ADDR_PATH = "FULLADD"

# Request data model strings
NUMBER_LOCATIONS_SLOT_NAME = "number_requests"
MAX_LOCATIONS = 10
DEFAULT_LOCATIONS = 3

def get_polling_location_info(mycity_request):
    """
    Generates a response to a polling location request

    :param mycity_request: MyCityRequestDataModel containing the user request
    :return: MyCityResponseDataModel containing the speech to return to the user
    """
    LOGGER.debug('Getting polling location information')

    response = MyCityResponseDataModel()
    set_address_in_session(mycity_request)
    current_address = \
            mycity_request.session_attributes.get(intent_constants.CURRENT_ADDRESS_KEY)
    if current_address is None:
        # Delegate to the Alexa interaction model for getting the user address
        LOGGER.debug('Requesting user address.')
        response.dialog_directive = "Delegate"
    else:
        response.output_speech = _get_output_speech_for_address(current_address, mycity_request)
        response.card_title = CARD_TITLE_POLLING

    return response


def _get_output_speech_for_address(address, mycity_request):
    """
    Creates output speech for polling locations near the provided address

    :param address: Current address
    :return: Output speech string
    """
    number_locations = _number_of_locations(mycity_request)
    response = get_polling_locations_json(address)
    try:
        results = response[FEATURES_PATH]
        output_speech = ""
        for result in results[:number_locations]:
            output_speech += _build_speech_from_result(result)
    except (IndexError, KeyError):
        LOGGER.error("Error extracting polling station response.")
        return intent_constants.NO_RESULTS_RESPONSE

    if not output_speech:
        return intent_constants.NO_RESULTS_RESPONSE

    return output_speech


def _number_of_locations(mycity_request):
    """
    Returns number of locations from the request if available or a default value
    :param mycity_request: MyCityRequestDataModel object
    :return: Number of polling station requests to return from this intent
    """
    if NUMBER_LOCATIONS_SLOT_NAME in \
            mycity_request.intent_variables and \
            "value" in mycity_request.intent_variables[
                NUMBER_LOCATIONS_SLOT_NAME]:
        return min(
            int(mycity_request.intent_variables[NUMBER_LOCATIONS_SLOT_NAME]["value"]),
            MAX_LOCATIONS)

    return DEFAULT_LOCATIONS


def _build_speech_from_result(result):
    """
    Builds a speech string from a given polling location result
    :param result: JSON object of a single polling location result
    :return: Speech string representing this result
    """

    try:
        attributes = result[ATTRIBUTES_PATH]
        name = attributes[NAME_PATH]
        precinct = attributes[PRECINCT_PATH]
        address = attributes[ADDR_PATH]
    except KeyError:
        LOGGER.error("Polling station response json did not contain the expected attributes.")
        raise KeyError

    return OUTPUT_SPEECH_TEMPLATE.format(name, precinct, address)
