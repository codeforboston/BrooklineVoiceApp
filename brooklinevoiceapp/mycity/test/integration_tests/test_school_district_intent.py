import copy
import logging

from mycity.intents import (
    intent_constants,
    school_district_intent as ps_intent,
)
from mycity.test import test_constants
from mycity.test.integration_tests import (
    intent_base_case as base_case,
    intent_test_mixins as mix_ins,
)

############################################
# TestCase class for school_district_intent #
############################################

MOCK_RESPONSE = test_constants.GET_SCHOOL_DISTRICT_API_MOCK

NO_RESULTS_RESPONSE = intent_constants.NO_RESULTS_RESPONSE

FEATURES = ps_intent.FEATURES_PATH
ATTRIBUTES = ps_intent.ATTRIBUTES_PATH
NAME = ps_intent.NAME_PATH

class SchoolDistrictTestCase(mix_ins.RepromptTextTestMixIn,
                            mix_ins.CardTitleTestMixIn,
                            base_case.IntentBaseCase):
    intent_to_test = "SchoolDistrictIntent"
    expected_title = ps_intent.CARD_TITLE_SCHOOL_DISTRICT
    returns_reprompt_text = False

    def setUp(self):
        """
        Patching out the functions in SchoolDistrictIntent that use requests.get
        """
        super().setUp()
        self.mock_requests(get_geocode_data=copy.deepcopy(test_constants.GET_ADDRESS_CANDIDATES_API_MOCK),
                           get_data=copy.deepcopy(test_constants.GET_SCHOOL_DISTRICT_API_MOCK))

    def testResponseContainsName(self):
        response = self.controller.on_intent(self.request)
        for feature in MOCK_RESPONSE[FEATURES]:
            self.assertIn(feature[ATTRIBUTES][NAME], response.output_speech)

    def testNoFeatureResults(self):
        self.mock_requests(get_geocode_data=copy.deepcopy(test_constants.GET_ADDRESS_CANDIDATES_API_MOCK),
                           get_data=copy.deepcopy(test_constants.NO_RESULTS_GET_SCHOOL_DISTRICT_API_MOCK))
        response = self.controller.on_intent(self.request)
        self.assertEqual(response.output_speech, NO_RESULTS_RESPONSE)
