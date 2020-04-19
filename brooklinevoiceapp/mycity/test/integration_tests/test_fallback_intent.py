"""Integration tests for fallback intent"""

from mycity.intents import fallback_intent
from mycity.test import test_constants
from mycity.test.integration_tests import (
    intent_base_case as base_case,
    intent_test_mixins as mix_ins,
)

class FallbackIntentTestCase(mix_ins.RepromptTextTestMixIn,
                             mix_ins.CardTitleTestMixIn,
                             base_case.IntentBaseCase):
    intent_to_test = "AMAZON.FallbackIntent"
    expected_title = fallback_intent.CARD_TITLE
    returns_reprompt_text = False

    def test_returns_default_fallback_speech(self):
        response = self.controller.on_intent(self.request)
        self.assertEquals(response.output_speech, fallback_intent.OUTPUT_SPEECH)
