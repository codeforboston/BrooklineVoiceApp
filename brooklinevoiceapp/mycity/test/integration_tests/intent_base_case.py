import typing
import unittest
from unittest import mock

import requests

import brookline_controller as my_controller
from mycity import mycity_request_data_model as req
from mycity.intents import intent_constants
from mycity.utils import brookline_arcgis_api_utils as utils


###############################################################################
# TestCase parent class for all intent TestCases, which are integration tests #
# to see if any changes in codebase have broken response-request model.       #
#                                                                             #
# NOTE: Assumes that address has already been set.                            #
###############################################################################


# Mock class for the API response
class ResponseStub:

    def __init__(self, status_code: int, response_data: typing.Dict = {}):
        self.status_code = status_code
        self.response_data = response_data

    def json(self):
        return self.response_data


class IntentBaseCase(unittest.TestCase):
    intent_to_test = None
    expected_title = "Unhandled"
    returns_reprompt_text = False

    def setUp(self):
        self._requests_original = utils.requests
        self.controller = my_controller
        self.request = req.MyCityRequestDataModel()
        key = intent_constants.CURRENT_ADDRESS_KEY
        self.request._session_attributes[key] = "333 Washington St"
        self.request.intent_name = self.intent_to_test

    def tearDown(self):
        self.controller = None
        self.request = None
        utils.requests = self._requests_original

    def mock_requests(
            self,
            get_status=200,
            post_status=200,
            get_data=None,
            post_data=None):
        mock_requests = requests
        # replace request Session REST methods with mocks
        mock_requests.Session.get = mock.MagicMock(return_value=ResponseStub(get_status, get_data))
        mock_requests.Session.post = mock.MagicMock(return_value=ResponseStub(post_status, post_data))
        utils.requests = mock_requests
