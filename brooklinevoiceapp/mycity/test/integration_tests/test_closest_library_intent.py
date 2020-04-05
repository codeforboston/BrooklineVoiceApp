import copy

from mycity.intents import (
    intent_constants,
    library_intent as lib_intent,
)
from mycity.test import test_constants
from mycity.test.integration_tests import (
    intent_base_case as base_case,
    intent_test_mixins as mix_ins,
)

############################################
# TestCase class for library_intent #
############################################

NO_RESULTS_RESPONSE = intent_constants.NO_RESULTS_RESPONSE
FEATURES = lib_intent.FEATURES_PATH
ATTRIBUTES = lib_intent.ATTRIBUTES_PATH
NAME = lib_intent.NAME_PATH
FULLADDR = lib_intent.FULLADDR_PATH
EXPECTED_GOOD_RESPONSE = "The nearest library to you is Main Library located at 361 Washington St, Brookline, MA 02445."

class LibraryIntentTestCase(mix_ins.RepromptTextTestMixIn,
                            mix_ins.CardTitleTestMixIn,
                            base_case.IntentBaseCase):
    
    intent_to_test = "LibraryIntent"
    expected_title = lib_intent.CARD_TITLE_LIBRARY
    returns_reprompt_text = False

    def setUp(self):
        """
        Patching responses for Library Intent requests
        """
        super().setUp()
        self.mock_requests(get_geocode_data=copy.deepcopy(test_constants.GET_ADDRESS_CANDIDATES_API_MOCK), 
                            get_data=copy.deepcopy(test_constants.GET_LIBRARY_API_MOCK))


    def testResponseContainsMainLibrary(self):
        response = self.controller.on_intent(self.request)
        self.assertEqual(response.output_speech, EXPECTED_GOOD_RESPONSE)
            
                        