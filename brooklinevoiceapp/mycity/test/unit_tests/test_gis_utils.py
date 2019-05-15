import mycity.test.test_constants as test_constants
import mycity.utils.brookline_arcgis_api_utils as utils
import mycity.test.unit_tests.base as base
import unittest.mock as mock
import copy


SPACIAL = utils.SPATIAL_REFERENCE_PATH

class GISUtilitiesTestCase(base.BaseTestCase):

    def test_get_first_address_candidate(self):
        expected_candidate = copy.deepcopy(test_constants.ADDRESS_CANDIDATE_MOCK)
        expected_spacial = test_constants.SPACIAL_REFERENCE_MOCK
        mock_requests = self.build_requests_stub(get_status=200,
             get_data=test_constants.GET_ADDRESS_CANDIDATES_API_MOCK)
        candidate_result, spacial_result = utils.get_first_address_candidate(self.test_address, mock_requests)
        self.assertEqual(expected_candidate, candidate_result)
        self.assertEqual(expected_spacial, spacial_result)

    def test_geocode_address(self):
        expected_result = test_constants.GEOCODE_MOCK
        mock_call = mock.MagicMock(return_value=[copy.deepcopy(test_constants.ADDRESS_CANDIDATE_MOCK),
                                                 test_constants.SPACIAL_REFERENCE_MOCK])
        result = utils.geocode_address(self.test_address, mock_call)
        self.assertEqual(expected_result, result)

    def test_get_nearest_police_station_json(self):
        mock_nearest_feature_call = mock.MagicMock(return_value=test_constants.GET_POLICE_STATION_API_MOCK)
        mock_geocode_call = mock.MagicMock(return_value=test_constants.LOCATION_MOCK)
        result = utils.get_nearest_police_station_json(self.test_address,
                                                       _get_nearest_feature_json=mock_nearest_feature_call,
                                                       _geocode_address=mock_geocode_call)
        self.assertEqual(result, test_constants.GET_POLICE_STATION_API_MOCK)

    def test_get_trash_day_json(self):
        mock_call = mock.MagicMock(return_value=test_constants.GET_TRASH_PICKUP_API_MOCK)
        result = utils.get_trash_day_json(self.test_address, mock_call)
        self.assertEqual(result, test_constants.GET_TRASH_PICKUP_API_MOCK)

    def test_get_polling_locations_json(self):
        mock_nearest_feature_call = mock.MagicMock(return_value=test_constants.GET_POLLING_LOCATIONS_API_MOCK)
        mock_geocode_call = mock.MagicMock(return_value=test_constants.LOCATION_MOCK)
        result = utils.get_nearest_police_station_json(self.test_address,
                                                       _get_nearest_feature_json=mock_nearest_feature_call,
                                                       _geocode_address=mock_geocode_call)
        self.assertEqual(result, test_constants.GET_POLLING_LOCATIONS_API_MOCK)

