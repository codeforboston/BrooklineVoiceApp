import mycity.test.test_constants as test_constants
import mycity.utils.brookline_arcgis_api_utils as utils
import mycity.test.unit_tests.base as base
import unittest.mock as mock


CANDIDATES = utils.CANDIDATES_PATH
LOCATION = utils.LOCATION_PATH


class GISUtilitiesTestCase(base.BaseTestCase):

    def test_get_first_address_candidate(self):
        expected_result = test_constants.ADDRESS_CANDIDATE_MOCK
        mock_requests = self.build_requests_stub(get_status=200,
             get_data=test_constants.GET_ADDRESS_CANDIDATES_API_MOCK)
        result = utils.get_first_address_candidate(self.test_address, mock_requests)
        self.assertEqual(result, expected_result)

    def test_geocode_address(self):
        location = test_constants.LOCATION_MOCK
        expected_result = [location['x'], location['y']]
        mock_call = mock.MagicMock(return_value=test_constants.ADDRESS_CANDIDATE_MOCK)
        result = utils.geocode_address(self.test_address, mock_call)
        self.assertEqual(result, expected_result)

    def test_get_nearest_police_station_json(self):
        mock_requests = self.build_requests_stub(post_status=200,
             post_data=test_constants.GET_POLICE_STATION_API_MOCK)
        mock_call = mock.MagicMock(return_value=test_constants.GEOCODE_ADDRESS_MOCK)
        result = utils.get_nearest_police_station_json(self.test_address, mock_requests, mock_call)
        self.assertEqual(result, test_constants.GET_POLICE_STATION_API_MOCK)

