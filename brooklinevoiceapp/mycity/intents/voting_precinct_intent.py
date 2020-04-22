""" Intent for responding to polling station requests """
import logging
from mycity.mycity_response_data_model import MyCityResponseDataModel
from mycity.intents import intent_constants
from mycity.utils.address_utils import set_address_in_session
from mycity.utils.brookline_arcgis_api_utils import get_voting_precinct_json


LOGGER = logging.getLogger(__name__)

# User facing strings
CARD_TITLE_VOTING = "Voting Location"
OUTPUT_SPEECH_TEMPLATE = "Your voting location for precinct {} is located at {}. "

# Strings used in parsing json data returned by server
FEATURES_PATH = "features"
ATTRIBUTES_PATH = "attributes"
ADDRESS_PATH = "ADDRESS"
PRECINCT_PATH = "PRECINCTID"

# Request data model strings
NUMBER_LOCATIONS_SLOT_NAME = "number_requests"
MAX_LOCATIONS = 10
DEFAULT_LOCATIONS = 3

def get_voting_precinct(mycity_request):
    """
    Generates a response to a voting precinct request

    :param mycity_request: MyCityRequestDataModel containing the user request
    :return: MyCityResponseDataModel containing the speech to return to the user
    """
    LOGGER.debug('Getting voting precinct information')

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
        response.card_title = CARD_TITLE_VOTING
        response.should_end_session = True

    return response


def _get_output_speech_for_address(address, mycity_request):
    """
    Creates output speech for polling locations near the provided address

    :param address: Current address
    :return: Output speech string
    """
    features = get_voting_precinct_json(address)
    try:
        first_feature = features[0]
        precinct_number = first_feature[ATTRIBUTES_PATH][PRECINCT_PATH]
        address = first_feature[ATTRIBUTES_PATH][ADDRESS_PATH]
    except (IndexError, KeyError):
        LOGGER.error("Error extracting voting precinct response.")
        return intent_constants.NO_RESULTS_RESPONSE

    return OUTPUT_SPEECH_TEMPLATE.format(precinct_number, address)