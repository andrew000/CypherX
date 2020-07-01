from collections import deque
from itertools import cycle

ASCII_LOWERCASE = 'abcdefghijklmnopqrstuvwxyz'
ASCII_UPPERCASE = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
CYRILLIC_LOWERCASE = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяі'
CYRILLIC_UPPERCASE = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯІ'

LEN_ASCII_LOWERCASE = len(ASCII_LOWERCASE)
LEN_ASCII_UPPERCASE = len(ASCII_UPPERCASE)
LEN_CYRILLIC_LOWERCASE = len(CYRILLIC_LOWERCASE)
LEN_CYRILLIC_UPPERCASE = len(CYRILLIC_UPPERCASE)


def _caesar_translator(key: int) -> dict:
    chars = deque(ASCII_LOWERCASE), deque(ASCII_UPPERCASE), \
            deque(CYRILLIC_LOWERCASE), deque(CYRILLIC_UPPERCASE)
    rotor = {}

    [de.rotate(-key) for de in chars]

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

    def __init__(self, raw_string: str, key: int, encode: bool = True, decode: bool = True):
        self.raw_string = raw_string
        self.key = key
        self.encoded = self.rotators(self.key) if encode is True else None
        self.decoded = self.rotators(-self.key) if decode is True else None

    def rotators(self, key: int):
        translator = _caesar_translator(key)
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


class VigenereCypher:

    def __init__(self, raw_string: str, key: str, encode: bool = True, decode: bool = True):
        self.raw_string = raw_string
        self.key = [
            ASCII_LOWERCASE.index(char) if char in ASCII_LOWERCASE else
            ASCII_UPPERCASE.index(char) if char in ASCII_UPPERCASE else
            CYRILLIC_LOWERCASE.index(char) if char in CYRILLIC_LOWERCASE else
            CYRILLIC_UPPERCASE.index(char) if char in CYRILLIC_UPPERCASE else
            char for char in key]
        self.encoded = self.rotor(self.key) if encode is True else None
        self.decoded = self.rotor([-x for x in self.key]) if decode is True else None

    def rotor(self, key: list):
        t_cycle = cycle(key)

        return "".join([ASCII_LOWERCASE[(ASCII_LOWERCASE.index(char) + next(t_cycle)) % LEN_ASCII_LOWERCASE]
                        if char in ASCII_LOWERCASE else

                        ASCII_UPPERCASE[(ASCII_UPPERCASE.index(char) + next(t_cycle)) % LEN_ASCII_UPPERCASE]
                        if char in ASCII_UPPERCASE else

                        CYRILLIC_LOWERCASE[(CYRILLIC_LOWERCASE.index(char) + next(t_cycle)) % LEN_CYRILLIC_LOWERCASE]
                        if char in CYRILLIC_LOWERCASE else

                        CYRILLIC_UPPERCASE[(CYRILLIC_UPPERCASE.index(char) + next(t_cycle)) % LEN_CYRILLIC_UPPERCASE]
                        if char in CYRILLIC_UPPERCASE else

                        char for char in self.raw_string])

    def __str__(self):
        return "RAW: {}\n" \
               "Key: {}\n" \
               "Encoded: {}\n" \
               "Decoded: {}".format(self.raw_string, self.key, self.encoded, self.decoded)

    def __repr__(self):
        return self.__str__()
