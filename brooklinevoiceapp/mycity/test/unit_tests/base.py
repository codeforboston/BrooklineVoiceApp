import unittest
import unittest.mock as mock
import typing
import requests
import brookline_controller as my_controller
import mycity.mycity_request_data_model as my_req


# Mock class for the API response
class ResponseStub:

    def __init__(self, status_code: int, response_data: typing.Dict = {}):
        self.status_code = status_code
        self.response_data = response_data

    def json(self):
        return self.response_data


class BaseTestCase(unittest.TestCase):

    def setUp(self):
        self.controller = my_controller
        self.request = my_req.MyCityRequestDataModel()
        self.test_address = "333 Washington St."

    def tearDown(self):
        self.controller = None
        self.request = None

    def build_requests_stub(
            self,
            get_status=200,
            post_status=200,
            get_data=None,
            post_data=None):
        requests_stub = requests
        # replace request Session REST methods with mocks
        requests_stub.Session.get = mock.MagicMock(return_value=ResponseStub(get_status, get_data))
        requests_stub.Session.post = mock.MagicMock(return_value=ResponseStub(post_status, post_data))
        return requests_stub

