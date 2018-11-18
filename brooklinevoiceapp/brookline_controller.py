"""
Dispatches MyCityRequestsObjects to the appropriate Brookline intent
"""

from mycity.mycity_response_data_model import MyCityResponseDataModel

def execute_request(mycity_request):
    """
    Executes a request to the town of Brookline available intents
    :param mycity_request: MyCityRequestDataModel with intent request info
    :return: MyCityResponseDataModel with response to provide to user.
    """

    response = MyCityResponseDataModel()
    response.output_speech = "Hello from Brookline!"
    return response
