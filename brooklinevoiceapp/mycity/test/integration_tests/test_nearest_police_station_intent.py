import unittest.mock as mock
import mycity.test.test_constants as test_constants
import mycity.test.integration_tests.intent_base_case as base_case
import mycity.test.integration_tests.intent_test_mixins as mix_ins
import mycity.intents.police_station_intent as ps_intent
import mycity.intents.intent_constants as intent_constants


############################################
# TestCase class for police_station_intent #
############################################

MOCK_RESPONSE = test_constants.GET_POLICE_STATION_API_MOCK

NO_RESULTS_RESPONSE = intent_constants.NO_RESULTS_RESPONSE

FEATURES = ps_intent.FEATURES_PATH
ATTRIBUTES = ps_intent.ATTRIBUTES_PATH
NAME = ps_intent.NAME_PATH
FULLADDR = ps_intent.FULLADDR_PATH

class PoliceStationTestCase(mix_ins.RepromptTextTestMixIn,
                             mix_ins.CardTitleTestMixIn,
                             base_case.IntentBaseCase):

    intent_to_test = "PoliceStationIntent"
    expected_title = ps_intent.CARD_TITLE_POLICE_STATION
    returns_reprompt_text = False

    def setUp(self):
        """
        Patching out the functions in PoliceStationIntent that use requests.get
        """
        super().setUp()
        self.get_nearest_police_station_json= \
            mock.patch(
                ('mycity.intents.police_station_intent.'
                 'get_nearest_police_station_json'),
                return_value=test_constants.GET_POLICE_STATION_API_MOCK)

    def tearDown(self):
        super().tearDown()


    def testResponseContainsNameAndFullAddress(self):
        self.get_nearest_police_station_json.start()
        response = self.controller.on_intent(self.request)
        for feature in MOCK_RESPONSE[FEATURES]:
            self.assertIn(feature[ATTRIBUTES][FULLADDR], response.output_speech)
            self.assertIn(feature[ATTRIBUTES][NAME], response.output_speech)
        self.get_nearest_police_station_json.stop()


    def testNoFeatureResults(self):
        self.get_nearest_police_station_json= \
            mock.patch(
                ('mycity.intents.police_station_intent.'
                 'get_nearest_police_station_json'),
                return_value=test_constants.NO_RESULTS_GET_POLICE_STATION_API_MOCK)
        self.get_nearest_police_station_json.start()
        response = self.controller.on_intent(self.request)
        self.assertEqual(response.output_speech, NO_RESULTS_RESPONSE)
        self.get_nearest_police_station_json.stop()
