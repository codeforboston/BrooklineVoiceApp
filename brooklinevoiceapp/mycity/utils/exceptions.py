class BaseOutputSpeechError(Exception):
    def __init__(self):
        super().__init__(self.output_speech)

    output_speech = None


class NoAddressFound(BaseOutputSpeechError):
    output_speech = "Nothing could be found for that address"
