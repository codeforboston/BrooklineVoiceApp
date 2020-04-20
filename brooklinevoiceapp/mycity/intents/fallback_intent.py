"""Fallback intent for unknown requests"""

import logging

from mycity.mycity_response_data_model import MyCityResponseDataModel

LOGGER = logging.getLogger(__name__)

CARD_TITLE = "Town of Brookline"
OUTPUT_SPEECH = "I'm not sure what you are asking me. \
    Please ask me about services for the Town of Brookline"


def get_fallback_intent_response(mycity_request):
    """
    Returns a generic fallback intent reponse

    :param mycity_request: MyCityRequestDataModel with user's request
    :return MyCityResponseDataModel with reponse for fallback intent
    """
    LOGGER.debug("Fallback intent called")

    mycity_response = MyCityResponseDataModel()
    mycity_response.session_attributes = mycity_request.session_attributes
    mycity_response.card_title = CARD_TITLE
    mycity_response.output_speech = OUTPUT_SPEECH
    mycity_response.should_end_session = False
    return mycity_response