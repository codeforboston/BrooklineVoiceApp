""" Integration tests for TrashDayIntent """
import copy

from mycity.intents import intent_constants, trash_day_intent as trash_intent
from mycity.test import test_constants
from mycity.test.integration_tests import (
    intent_base_case as base_case,
    intent_test_mixins as mix_ins,
)

MOCK_RESPONSE = test_constants.GET_TRASH_PICKUP_API_MOCK

class TrashPickupTestCase(mix_ins.RepromptTextTestMixIn,
                          mix_ins.CardTitleTestMixIn,
                          base_case.IntentBaseCase):

    intent_to_test = "TrashDayIntent"
    expected_title = trash_intent.CARD_TITLE_TRASH_DAY
    returns_reprompt_text = False

    def setUp(self):
        super().setUp()

        # Patch requests.get in TrashDayIntent
        self.mock_requests(get_data=copy.deepcopy(test_constants.GET_ADDRESS_CANDIDATES_API_MOCK),
                           post_data=copy.deepcopy(test_constants.GET_TRASH_PICKUP_API_MOCK))

    def test_response_contains_day_of_the_week(self):
        response = self.controller.on_intent(self.request)
        self.assertTrue("Wednesday" in response.output_speech)

    def test_no_feature_results(self):
        self.mock_requests(get_data=copy.deepcopy(test_constants.GET_ADDRESS_CANDIDATES_API_MOCK),
                           post_data=copy.deepcopy(test_constants.NO_RESPONSE_TRASH_PICKUP_API_MOCK))
        response = self.controller.on_intent(self.request)
        self.assertEqual(response.output_speech, intent_constants.NO_RESULTS_RESPONSE)
