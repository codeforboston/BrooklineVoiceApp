from mycity.test import test_constants
from mycity.test.unit_tests import base
from mycity.utils import address_utils as utils


class AddressUtilsTestCase(base.BaseTestCase):

    def test_get_closest_address(self):
        expected = [
            test_constants.GET_POLLING_LOCATIONS_API_MOCK['features'][1],
            test_constants.GET_POLLING_LOCATIONS_API_MOCK['features'][0],
            test_constants.GET_POLLING_LOCATIONS_API_MOCK['features'][2]
        ]
        actual = utils.get_sorted_features(
            test_constants.GET_POLICE_STATION_API_MOCK['features'][0]['geometry'],
            test_constants.GET_POLLING_LOCATIONS_API_MOCK['features']
        )
        self.assertEqual(expected, actual)
