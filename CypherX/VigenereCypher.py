from itertools import cycle

from .letters import _ASCII_LOWERCASE, _ASCII_UPPERCASE, _CYRILLIC_LOWERCASE, _CYRILLIC_UPPERCASE, _LEN_ASCII_LOWERCASE, \
    _LEN_CYRILLIC_LOWERCASE, _LEN_ASCII_UPPERCASE, _LEN_CYRILLIC_UPPERCASE


class VigenereCypher:

    def __init__(self, raw_string: str, key: str, encode: bool = True, decode: bool = True):
        self.__raw_string = raw_string
        self.__key = [
            _ASCII_LOWERCASE.index(char) if char in _ASCII_LOWERCASE else
            _ASCII_UPPERCASE.index(char) if char in _ASCII_UPPERCASE else
            _CYRILLIC_LOWERCASE.index(char) if char in _CYRILLIC_LOWERCASE else
            _CYRILLIC_UPPERCASE.index(char) if char in _CYRILLIC_UPPERCASE else
            char for char in key]
        self.__encoded = self.rotor(self.__key) if encode is True else None
        self.__decoded = self.rotor([-x for x in self.__key]) if decode is True else None

    def rotor(self, key: list):
        t_cycle = cycle(key)

        return "".join([_ASCII_LOWERCASE[(_ASCII_LOWERCASE.index(char) + next(t_cycle)) % _LEN_ASCII_LOWERCASE]
                        if char in _ASCII_LOWERCASE else

                        _ASCII_UPPERCASE[(_ASCII_UPPERCASE.index(char) + next(t_cycle)) % _LEN_ASCII_UPPERCASE]
                        if char in _ASCII_UPPERCASE else

                        _CYRILLIC_LOWERCASE[(_CYRILLIC_LOWERCASE.index(char) + next(t_cycle)) % _LEN_CYRILLIC_LOWERCASE]
                        if char in _CYRILLIC_LOWERCASE else

                        _CYRILLIC_UPPERCASE[(_CYRILLIC_UPPERCASE.index(char) + next(t_cycle)) % _LEN_CYRILLIC_UPPERCASE]
                        if char in _CYRILLIC_UPPERCASE else

                        char for char in self.__raw_string])

    @property
    def raw_string(self):
        return self.__raw_string

    @raw_string.setter
    def raw_string(self, value):
        self.__raw_string = value
        self.__encoded = self.rotor(self.__key)
        self.__decoded = self.rotor([-x for x in self.__key])

    @property
    def key(self):
        return self.__key

    @key.setter
    def key(self, value):
        self.__key = [
            _ASCII_LOWERCASE.index(char) if char in _ASCII_LOWERCASE else
            _ASCII_UPPERCASE.index(char) if char in _ASCII_UPPERCASE else
            _CYRILLIC_LOWERCASE.index(char) if char in _CYRILLIC_LOWERCASE else
            _CYRILLIC_UPPERCASE.index(char) if char in _CYRILLIC_UPPERCASE else
            char for char in value]
        self.__encoded = self.rotor(self.__key)
        self.__decoded = self.rotor([-x for x in self.__key])

    @property
    def encoded(self):
        return self.__encoded

    @encoded.setter
    def encoded(self, value):
        raise AttributeError

    @property
    def decoded(self):
        return self.__decoded

    @decoded.setter
    def decoded(self, value):
        raise AttributeError

    def __str__(self):
        return "RAW: {}\n" \
               "Key: {}\n" \
               "Encoded: {}\n" \
               "Decoded: {}".format(self.__raw_string, self.__key, self.__encoded, self.__decoded)

    def __repr__(self):
        return self.__str__()
