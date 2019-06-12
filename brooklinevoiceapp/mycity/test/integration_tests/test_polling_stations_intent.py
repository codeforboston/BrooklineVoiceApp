""" Integration tests for PollingStationIntent """
import mycity.test.test_constants as test_constants
import mycity.test.integration_tests.intent_base_case as base_case
import mycity.test.integration_tests.intent_test_mixins as mix_ins
import mycity.intents.polling_stations_intent as polling_intent
import mycity.intents.intent_constants as intent_constants
import copy

FEATURES=polling_intent.FEATURES_PATH
ATTRIBUTES=polling_intent.ATTRIBUTES_PATH
NAME=polling_intent.NAME_PATH

class PollingStationsTestCase(mix_ins.RepromptTextTestMixIn,
                              mix_ins.CardTitleTestMixIn,
                              base_case.IntentBaseCase):

    intent_to_test = "PollingStationIntent"
    expected_title = polling_intent.CARD_TITLE_POLLING
    returns_reprompt_text = False

    def setUp(self):
        super().setUp()

        # Patch requests.get in PollingStationIntent
        self.mock_requests(get_data=copy.deepcopy(test_constants.GET_ADDRESS_CANDIDATES_API_MOCK),
                           post_data=copy.deepcopy(test_constants.GET_POLLING_LOCATIONS_API_MOCK))

    def test_response_contains_polling_first_station_name(self):
        first_station_name = test_constants.GET_POLLING_LOCATIONS_API_MOCK[FEATURES][0][ATTRIBUTES][NAME]
        response = self.controller.on_intent(self.request)
        self.assertTrue(first_station_name in response.output_speech)

    def test_no_feature_results(self):
        self.mock_requests(get_data=copy.deepcopy(test_constants.GET_ADDRESS_CANDIDATES_API_MOCK),
                           post_data=copy.deepcopy(test_constants.NO_RESPONSE_POLLING_LOCATIONS_API_MOCK))
        response = self.controller.on_intent(self.request)
        self.assertEqual(response.output_speech, intent_constants.NO_RESULTS_RESPONSE)
