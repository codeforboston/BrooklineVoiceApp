""" Integration tests for TrashDayIntent """
import unittest.mock as mock
import mycity.test.test_constants as test_constants
import mycity.test.integration_tests.intent_base_case as base_case
import mycity.test.integration_tests.intent_test_mixins as mix_ins
import mycity.intents.trash_day_intent as trash_intent
import mycity.intents.intent_constants as intent_constants


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
        self.get_trash_day_json = \
            mock.patch(
                ('mycity.intents.trash_day_intent.'
                 'get_trash_day_json'),
                return_value=test_constants.GET_TRASH_PICKUP_API_MOCK)

    def test_response_contains_day_of_the_week(self):
        self.get_trash_day_json.start()
        response = self.controller.on_intent(self.request)
        self.assertTrue("Wednesday" in response.output_speech)
        self.get_trash_day_json.stop()

    def test_no_feature_results(self):
        self.get_trash_day_json = \
            mock.patch(
                ('mycity.intents.trash_day_intent.'
                 'get_trash_day_json'),
                return_value=test_constants.NO_RESPONSE_TRASH_PICKUP_API_MOCK)
        self.get_trash_day_json.start()
        response = self.controller.on_intent(self.request)
        self.assertEqual(response.output_speech, intent_constants.NO_RESULTS_RESPONSE)
        self.get_trash_day_json.stop()
