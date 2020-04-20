"""
unit test for BrooklineController
"""

import brookline_controller as bl_con
import mycity.test.unit_tests.base as base


class BrooklineControllerUnitTestCase(base.BaseTestCase):
    """
    testing:
        handle_session_end_request
    """

    def test_on_intent_AMAZON_StopIntent(self):
        expected_attributes = self.request.session_attributes
        expected_output_speech = (
            "Thank you for using the Brookline Info skill. "
            "See you next time!"
        )
        expected_card_title = "Brookline Info - Thanks"
        self.request.intent_name = "AMAZON.StopIntent"
        response = self.controller.on_intent(self.request)
        self.assertEqual(response.session_attributes, expected_attributes)
        self.assertEqual(response.output_speech, expected_output_speech)
        self.assertEqual(response.card_title, expected_card_title)
        self.assertIsNone(response.reprompt_text)
