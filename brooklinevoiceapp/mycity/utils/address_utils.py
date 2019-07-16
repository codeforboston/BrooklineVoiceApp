import logging

from mycity.intents import intent_constants

logger = logging.getLogger(__name__)


def set_address_in_session(mycity_request):
    """
    Adds an address to the provided session object

    :param mycity_request: MyCityRequestDataModel object
    :return: None
    """

    if 'Address' in mycity_request.intent_variables and \
            'value' in mycity_request.intent_variables['Address']:
        address = mycity_request.intent_variables['Address']['value']
        logger.debug("Setting Address in Session Attributes. Address: {}".format(str(address)))
        mycity_request.session_attributes[intent_constants.CURRENT_ADDRESS_KEY] = address
        if intent_constants.ZIP_CODE_KEY in mycity_request.session_attributes:
            # We clear out any zip code saved if the user has
            # changed the address
            del (mycity_request.session_attributes
            [intent_constants.ZIP_CODE_KEY])
