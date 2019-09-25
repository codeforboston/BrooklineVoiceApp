""" Intent for responding to trash day requests """
import logging

from mycity.intents import intent_constants
from mycity.mycity_response_data_model import MyCityResponseDataModel
from mycity.utils.address_utils import set_address_in_session
from mycity.utils.brookline_arcgis_api_utils import get_trash_day_json

LOGGER = logging.getLogger(__name__)

# User facing strings
CARD_TITLE_TRASH_DAY = "Trash Day"
OUTPUT_SPEECH_TEMPLATE = "Trash is picked up on {}"

# Strings used in parsing json data returned by server
ATTRIBUTES_PATH = "attributes"
NAME_PATH = "NAME"


def get_trash_pickup_info(mycity_request):
    """
    Generates a response to a trash day request

    :param mycity_request: MyCityRequestDataModel containing the user request
    :return: MyCityResponseDataModel containing the speech to return to the user
    """
    LOGGER.debug('Getting trash day information')

    response = MyCityResponseDataModel()
    set_address_in_session(mycity_request)
    current_address = \
        mycity_request.session_attributes.get(intent_constants.CURRENT_ADDRESS_KEY)
    if current_address is None:
        # Delegate to the Alexa interaction model for getting the user address
        LOGGER.debug('Requesting user address')
        response.dialog_directive = "Delegate"
    else:
        response.output_speech = _get_output_speech_for_address(current_address)
        response.card_title = CARD_TITLE_TRASH_DAY

    return response


def _get_output_speech_for_address(address):
    """
    Creates output speech for trash day at the provided address

    :param address: Current address
    :return: Output speech string
    """
    response = get_trash_day_json(address)
    try:
        first_feature = response[0]

        # Trash day is returned as "<DAY OF THE WEEK> Trash". We just want the
        # day so we split immediately
        trash_day = first_feature[ATTRIBUTES_PATH][NAME_PATH].split()[0]
    except (IndexError, KeyError):
        return intent_constants.NO_RESULTS_RESPONSE

    return OUTPUT_SPEECH_TEMPLATE.format(trash_day)
