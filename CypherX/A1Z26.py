from .letters import _ASCII_LOWERCASE, _CYRILLIC_LOWERCASE, _LEN_ASCII_LOWERCASE, _LEN_CYRILLIC_LOWERCASE


def _pre_process_encode(raw_string, lang):
    return {'en': (str(_ASCII_LOWERCASE.index(char) + 1)
                   if char in _ASCII_LOWERCASE else char for char in raw_string),
            'ru': (str(_CYRILLIC_LOWERCASE.index(char) + 1)
                   if char in _CYRILLIC_LOWERCASE else char for char in raw_string)
            }[lang]


def _pre_process_decode(raw_string, lang):
    return {'en': (_ASCII_LOWERCASE[int(index) - 1] for index in raw_string.split('-') if
                   index.isdigit() and 0 <= int(index) <= _LEN_ASCII_LOWERCASE),
            'ru': (_CYRILLIC_LOWERCASE[int(index) - 1] for index in raw_string.split('-')
                   if
                   index.isdigit() and 0 <= int(index) <= _LEN_CYRILLIC_LOWERCASE)}[lang]


class A1Z26:

    def __init__(self, raw_string: str, lang='en'):
        """

        :param raw_string:
        :param lang: accept 'en' or 'ru'
        """

        self.__raw_string = raw_string.lower()
        self.__lang = lang

        self.__pre_process_encode = _pre_process_encode(self.__raw_string, self.__lang)
        self.__pre_process_decode = _pre_process_decode(self.__raw_string, self.__lang)

        self.__encoded = self.encode()
        self.__decoded = self.decode()

    def encode(self):
        self.__encoded = "-".join(self.__pre_process_encode)
        return self.__encoded

    def decode(self):
        self.__decoded = "".join(self.__pre_process_decode)
        return self.__decoded

    @property
    def raw_string(self):
        return self.__raw_string

    @raw_string.setter
    def raw_string(self, value: str):
        self.__raw_string = value.lower()
        self.__pre_process_encode = _pre_process_encode(self.__raw_string, self.__lang)
        self.__pre_process_decode = _pre_process_decode(self.__raw_string, self.__lang)
        self.encode()
        self.decode()

    @property
    def lang(self):
        return self.__lang

    @lang.setter
    def lang(self, value: str):
        self.__lang = value
        self.__pre_process_encode = _pre_process_encode(self.__raw_string, self.__lang)
        self.__pre_process_decode = _pre_process_decode(self.__raw_string, self.__lang)
        self.encode()
        self.decode()

    @property
    def encoded(self):
        return self.__encoded

    @encoded.setter
    def encoded(self, value):
        raise AttributeError

    @property
    def pre_process_encode(self):
        return self.__pre_process_encode

    @pre_process_encode.setter
    def pre_process_encode(self, value):
        raise AttributeError

    @property
    def pre_process_decode(self):
        return self.__pre_process_decode

    @pre_process_decode.setter
    def pre_process_decode(self, value):
        raise AttributeError

    def __str__(self):
        return "RAW: {}\n" \
               "Key: {}\n" \
               "Encoded: {}\n" \
               "Decoded: {}".format(self.__raw_string, self.__lang, self.__encoded, self.__decoded)

    def __repr__(self):
        return self.__str__()
