from collections import deque

ASCII_LOWERCASE = 'abcdefghijklmnopqrstuvwxyz'
ASCII_UPPERCASE = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
CYRILLIC_LOWERCASE = 'абвгдеёжзийклмнопстуфхцчшщъыьэюя'
CYRILLIC_UPPERCASE = 'АБВГДЕЁЖЗИЙКЛМНОПСТУФХЦЧШЩЪЫЬЭЮЯ'


def _make_translator(key):
    chars = deque(ASCII_LOWERCASE), deque(ASCII_UPPERCASE), \
            deque(CYRILLIC_LOWERCASE), deque(CYRILLIC_UPPERCASE)
    rotor = {}

    for de in chars:
        de.rotate(-key)

    for sym, de in zip((ASCII_LOWERCASE, ASCII_UPPERCASE, CYRILLIC_LOWERCASE, CYRILLIC_UPPERCASE), chars):
        rotor.update(str.maketrans(sym, "".join(de)))

    return rotor


class CaesarCypher:
    """
    Encode:

    - Just put raw_string and key into class

    Decode:

    - Just put encoded string and key into class
    """

    def __init__(self, raw_string: str, key: int):
        self.raw_string = raw_string
        self.key = key
        self.encoded = self.rotators(self.key)
        self.decoded = self.rotators(-self.key)

    def rotators(self, key: int):
        translator = _make_translator(key)
        return self.raw_string.translate(translator)

    def __str__(self):
        return "RAW: {}\n" \
               "Key: {}\n" \
               "Encoded: {}\n" \
               "Decoded: {}".format(self.raw_string, self.key, self.encoded, self.decoded)

    def __repr__(self):
        return self.__str__()


class CaesarCracker:
    """
    Crack Caesar Cypher.

    Brute all 26 keys
    """

    def __init__(self, raw_string: str):
        self.raw_string = raw_string
        self.cracked = None

        self.crack()

    def crack(self):
        self.cracked = ["{}: {}".format(i, string) for i, string in
                        enumerate([CaesarCypher(self.raw_string, key).decoded for key in range(1, 27)], start=1)]
        return self.cracked

    def __str__(self):
        return "\n".join(self.cracked)

    def __repr__(self):
        return self.__str__()
