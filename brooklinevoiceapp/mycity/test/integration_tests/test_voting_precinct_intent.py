""" Integration tests for PollingStationIntent """

import copy
from mycity.test import test_constants
from mycity.test.integration_tests import (
    intent_base_case as base_case,
    intent_test_mixins as mix_ins,
)
from mycity.intents import (
    intent_constants,
    voting_precinct_intent as voting_precinct_intent,
)

FEATURES=voting_precinct_intent.FEATURES_PATH
ATTRIBUTES=voting_precinct_intent.ATTRIBUTES_PATH

class VotingPrecinctIntentTestCase(mix_ins.RepromptTextTestMixIn,
                              mix_ins.CardTitleTestMixIn,
                              base_case.IntentBaseCase):

    intent_to_test = "VotingPrecinctIntent"
    expected_title = voting_precinct_intent.CARD_TITLE_VOTING
    returns_reprompt_text = False

    def setUp(self):
        super().setUp()

        # Patch requests.get in VotingPrecinctIntent
        self.mock_requests(get_geocode_data=copy.deepcopy(test_constants.GET_ADDRESS_CANDIDATES_API_MOCK),
                           get_data=copy.deepcopy(test_constants.GET_VOTING_PRECINCT_API_MOCK))

    def test_response_contains_correct_voting_precinct(self):
        expected_response = "Your voting location for precinct 6 is located at 115 GREENOUGH ST. "
        response = self.controller.on_intent(self.request)
        self.assertEqual(expected_response,response.output_speech)

    def test_no_feature_results(self):
        self.mock_requests(get_geocode_data=copy.deepcopy(test_constants.GET_ADDRESS_CANDIDATES_API_MOCK),
                           get_data=copy.deepcopy(test_constants.NO_RESPONSE_VOTING_PRECINCT_API_MOCK))
        response = self.controller.on_intent(self.request)
        self.assertEqual(response.output_speech, intent_constants.NO_RESULTS_RESPONSE)
