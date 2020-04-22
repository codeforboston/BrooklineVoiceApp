"""
unit test for BrooklineController
"""

import brookline_controller as bl_con
import mycity.intents.intent_constants as intent_constants
import mycity.test.unit_tests.base as base


class BrooklineControllerUnitTestCase(base.BaseTestCase):
    """
    testing:
        execute_request
        on_intent
        get_welcome_response
        handle_session_end_request
    """

    def test_welcome_response(self):
        self.request.is_new_session = False
        self.request.request_type = "LaunchRequest"
        expected_session_attributes = self.request.session_attributes
        expected_output_speech = bl_con.LAUNCH_SPEECH
        expected_reprompt_text = bl_con.LAUNCH_REPROMPT_SPEECH
        expected_card_title = "Welcome"
        response = self.controller.execute_request(self.request)
        self.assertEqual(
            response.session_attributes,
            expected_session_attributes
        )
        self.assertEqual(response.output_speech, expected_output_speech)
        self.assertEqual(response.reprompt_text, expected_reprompt_text)
        self.assertFalse(response.should_end_session)

    def test_execute_request_with_no_request_speech(self):
        self.request.is_new_session = False
        self.request.request_type = None
        expected_output_speech = bl_con.NO_REQUEST_SPEECH
        response = self.controller.execute_request(self.request)
        self.assertEqual(response.output_speech, expected_output_speech)

    def test_on_intent_AMAZON_StopIntent(self):
        expected_attributes = self.request.session_attributes
        expected_output_speech = (
            "Thank you for using the Brookline Info skill. "
            "See you next time!"
        )
        expected_card_title = "Brookline Info - Thanks"
        self.request.request_type = "IntentRequest"
        self.request.intent_name = "AMAZON.StopIntent"
        response = self.controller.execute_request(self.request)
        self.assertEqual(response.session_attributes, expected_attributes)
        self.assertEqual(response.output_speech, expected_output_speech)
        self.assertEqual(response.card_title, expected_card_title)
        self.assertIsNone(response.reprompt_text)

    def test_unknown_intent(self):
        self.request.intent_name = "MadeUpIntent"
        self.request.session_attributes[intent_constants.CURRENT_ADDRESS_KEY] = '46 Everdean St'
        with self.assertRaises(ValueError):
            self.controller.on_intent(self.request)
