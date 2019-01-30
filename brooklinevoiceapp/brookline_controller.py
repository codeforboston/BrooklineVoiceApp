"""
Dispatches MyCityRequestsObjects to the appropriate Brookline intent
"""

from mycity.mycity_response_data_model import MyCityResponseDataModel
from mycity.intents.police_station_intent import find_closest_police_station

def execute_request(mycity_request):
    """
    Executes a request to the town of Brookline available intents
    :param mycity_request: MyCityRequestDataModel with intent request info
    :return: MyCityResponseDataModel with response to provide to user.
    """

    if mycity_request.request_type == "IntentRequest":
        return on_intent(mycity_request)
    else:
        response = MyCityResponseDataModel()
        response.output_speech = "Hello from Brookline! We do not support that yet"
        return response


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

    if mycity_request.intent_name == "PoliceStationIntent":
        return find_closest_police_station(mycity_request)
    else:
        raise ValueError("Invalid Intent")
        

