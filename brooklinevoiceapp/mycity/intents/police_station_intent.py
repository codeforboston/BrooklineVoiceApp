from mycity.utils.address_utils import set_address_in_session
from mycity.intents import intent_constants
from mycity.mycity_response_data_model import MyCityResponseDataModel
from mycity.utils.brookline_arcgis_api_utils import \
    get_nearest_police_station_response

import logging

logger = logging.getLogger(__name__)

OUTPUT_SPEECH_TEMPLATE = \
    "The nearest police station to you is {} located at {}."

FEATURES_PATH = "features"
ATTRIBUTES_PATH = "attributes"
NAME_PATH = "NAME"
FULLADDR_PATH = "FULLADDR"

def find_closest_police_station(mycity_request):
    """
    Finds the closest police station in Brookline
    to a given address

    :param mycity_request: MyCityRequestDataModel object
    :return: MyCityResponseDataModel object
    """
    logger.debug('Finding closest police station')

    response = MyCityResponseDataModel()
    set_address_in_session(mycity_request)
    response.session_attributes = mycity_request.session_attributes
    current_address = \
            mycity_request.session_attributes.get(intent_constants.CURRENT_ADDRESS_KEY)
    if current_address is None: 
        response.dialog_directive = "Delegate"
    else:
        response.output_speech = _get_output_speech_for_address(current_address)

    return response



