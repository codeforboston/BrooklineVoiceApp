"""
Dispatches MyCityRequestsObjects to the appropriate Brookline intent
"""

import logging

from mycity.intents.police_station_intent import find_closest_police_station
from mycity.intents.library_intent import find_closest_library
from mycity.intents.voting_precinct_intent import get_voting_precinct
from mycity.intents.trash_day_intent import get_trash_pickup_info
from mycity.intents.school_district_intent import find_closest_school_district
from mycity.intents.fallback_intent import get_fallback_intent_response
from mycity.mycity_response_data_model import MyCityResponseDataModel
from mycity.utils.exceptions import BaseOutputSpeechError

logger = logging.getLogger(__name__)


LAUNCH_SPEECH = "Welcome to the Brookline Info skill. How can I help you?"
LAUNCH_REPROMPT_SPEECH = "You can ask about the nearest city services."
NO_REQUEST_SPEECH = "Hello from Brookline! We do not support that yet"


def execute_request(mycity_request):
    """
    Executes a request to the town of Brookline available intents
    :param mycity_request: MyCityRequestDataModel with intent request info
    :return: MyCityResponseDataModel with response to provide to user.
    """

    if mycity_request.is_new_session:
        mycity_request = on_session_started(mycity_request)

    if mycity_request.request_type == "LaunchRequest":
        response = get_welcome_response(mycity_request)
    elif mycity_request.request_type == "IntentRequest":
        response = on_intent(mycity_request)
    elif mycity_request.request_type == "SessionEndedRequest":
        response = on_session_ended(mycity_request)
    else:
        response = MyCityResponseDataModel()
        response.output_speech = NO_REQUEST_SPEECH

    response.session_attributes = mycity_request.session_attributes
    return response


def on_session_ended(mycity_request):
    """
    Called when the user ends the session.
    Is not called when the skill returns should_end_session=true

    :param mycity_request: MyCityRequestDataModel object with
        request_type SessionEndedRequest
    :return: MyCityResponseDataModel object containing a clean instance
        of the response datamodel
    """
    logger.debug('MyCityRequestDataModel received:' + mycity_request.get_logger_string())

    return MyCityResponseDataModel()
    # add cleanup logic here


def get_welcome_response(mycity_request):
    """
    Welcomes the user and sets initial session attributes. Is triggered on
    initial launch and on AMAZON.HelpIntent.

    If we wanted to initialize the session to have some attributes we could
    add those here.

    :param mycity_request: MyCityRequestDataModel object
    :return: MyCityResponseDataModel object that will initiate
        a welcome process on the user's device
    """
    mycity_response = MyCityResponseDataModel()
    mycity_response.session_attributes = mycity_request.session_attributes
    mycity_response.card_title = "Welcome"
    mycity_response.output_speech = LAUNCH_SPEECH

    # If the user either does not reply to the welcome message or says
    # something that is not understood, they will be prompted again with
    # this text.
    mycity_response.reprompt_text = LAUNCH_REPROMPT_SPEECH
    mycity_response.should_end_session = False
    return mycity_response


def on_session_started(mycity_request):
    """
    Called when the session starts. Creates a log entry with session info
    and inserts device address into session attributes if available.

    :param mycity_request: MyCityRequestDataModel object
    :return: MyCityRequestDataModel object
    """
    logger.debug('Request object: ' + mycity_request.get_logger_string())
    return mycity_request


def on_intent(mycity_request):
    """
    If the event type is "request" and the request type is "IntentRequest",
    this function is called to execute the logic associated with the
    provided intent and build a response. Checks for required
    session_attributes when applicable.

    :param mycity_request: MyCityRequestDataModel object with
        request_type IntentRequest
    :return: MyCityResponseDataModel object corresponding to the intent_name
    :raises: ValueError
    """

    try:
        if mycity_request.intent_name == "PoliceStationIntent":
            return find_closest_police_station(mycity_request)
        elif mycity_request.intent_name == "TrashDayIntent":
            return get_trash_pickup_info(mycity_request)
        elif mycity_request.intent_name == "LibraryIntent":
            return find_closest_library(mycity_request)
        elif mycity_request.intent_name == "SchoolDistrictIntent":
            return find_closest_school_district(mycity_request)
        elif mycity_request.intent_name == "VotingPrecinctIntent":
            return get_voting_precinct(mycity_request)
        elif mycity_request.intent_name == "AMAZON.FallbackIntent":
            return get_fallback_intent_response(mycity_request)
        elif mycity_request.intent_name == "AMAZON.StopIntent":
            return handle_session_end_request(mycity_request)
        else:
            raise ValueError("Invalid Intent")
    except BaseOutputSpeechError as e:
        response = on_session_ended(mycity_request)
        response.output_speech = e.output_speech
        return response


def handle_session_end_request(mycity_request):
    """
    Ends a user's session (with the Brookline Info skill).
    Called when request intent is AMAZON.StopIntent.

    :param mycity_request: MyCityRequestDataModel object
    :return: MyCityResponseDataModel object that will end a user's session
    """
    logger.debug('Closing')
    mycity_response = MyCityResponseDataModel()
    mycity_response.session_attributes = mycity_request.session_attributes
    mycity_response.card_title = "Brookline Info - Thanks"
    mycity_response.output_speech = \
        "Thank you for using the Brookline Info skill. " \
        "See you next time!"
    mycity_response.should_end_session = True
    return mycity_response
