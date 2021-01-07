import binascii
from base64 import urlsafe_b64decode, urlsafe_b64encode
from itertools import cycle
from operator import xor
from typing import Union


class XORCypher:
    """
    XORCypher class to encode and decode text using XOR method.
    """

    def __init__(self, string: Union[str, bytes], key: str, encoding: str = 'UTF8'):
        """

        :param string: Input string for encoding or decoding
        :type string: :obj:`Union[str, bytes]`

        :param key: Random string key to encode or decode string
        :type key: :obj:`str`

        :param encoding: Set text encoding (default: 'UTF8')
        :type encoding: :obj:`str`
        """
        self.__string = string
        self.__key = key
        self.__encoding = encoding
        self.__encoded: bytes = self.encode(self.__string, self.__key, self.__encoding)
        self.__decoded: str = self.decode(self.__string, self.__key, self.__encoding)

    def __str__(self):
        return f"Key: {self.__key}\n" \
               f"Encoded: {self.__encoded}\n" \
               f"Decoded: {self.__decoded}"

    def __repr__(self):
        return f"{self.__class__} string={self.__string}, key={self.__key}, encoding={self.__encoding}, " \
               f"encoded={self.__encoded}, decoded={self.__decoded}"

    @staticmethod
    def encode(string: Union[str, bytes], key: str, encoding: str = 'UTF8') -> bytes:
        """
        :param string: Input string for encoding or decoding
        :type string: :obj:`Union[str, bytes]`

        :param key: Random string key to encode or decode string
        :type key: :obj:`str`

        :param encoding: Set text encoding (default: 'UTF8')
        :type encoding: :obj:`str`

        :return: Encoded string
        :rtype: :obj:`bytes`
        """
        if isinstance(string, bytes):
            string = string.decode(encoding)
        return urlsafe_b64encode(
            bytes("".join(map(chr, map(xor, map(ord, string), cycle(map(ord, key))))), encoding=encoding))

    @staticmethod
    def decode(string: Union[str, bytes], key: str, encoding: str = 'UTF8') -> str:
        """
        :param string: Input string for encoding or decoding
        :type string: :obj:`Union[str, bytes]`

        :param key: Random string key to encode or decode string
        :type key: :obj:`str`

        :param encoding: Set text encoding (default: 'UTF8')
        :type encoding: :obj:`str`

        :return: Decoded string
        :rtype: :obj:`str`
        """
        try:
            return "".join(
                map(chr, map(xor, map(ord, urlsafe_b64decode(string).decode(encoding=encoding)), cycle(map(ord, key)))))

        except binascii.Error:
            return 'Incorrect padding (This error can be raised if you encode string)'

    @property
    def string(self) -> str:
        """
        :return: Return input string
        :rtype: :obj:`str`
        """
        return self.__string

    @string.setter
    def string(self, value: Union[str, bytes]):
        self.__string = value
        self.__encoded = self.encode(self.__string, self.__key, self.__encoding)
        self.__decoded = self.decode(self.__string, self.__key, self.__encoding)

    @string.deleter
    def string(self):
        raise AttributeError

    @property
    def key(self) -> str:
        """
        :return: Return key
        :rtype: :obj:`str`
        """
        return self.__key

    @key.setter
    def key(self, value: str):
        self.__key = value
        self.__encoded = self.encode(self.__string, self.__key, self.__encoding)
        self.__decoded = self.decode(self.__string, self.__key, self.__encoding)

    @key.deleter
    def key(self):
        raise AttributeError

    @property
    def encoding(self) -> str:
        """
        :return: Return encoding
        :rtype: :obj:`str`
        """
        return self.__encoding

    @encoding.setter
    def encoding(self, value: str):
        self.__encoding = value
        self.__encoded = self.encode(self.__string, self.__key, self.__encoding)
        self.__decoded = self.decode(self.__string, self.__key, self.__encoding)

    @encoding.deleter
    def encoding(self):
        raise AttributeError

    @property
    def encoded(self) -> bytes:
        """
        :return: Return encoded string
        :rtype: :obj:`bytes`
        """
        return self.__encoded

    @encoded.setter
    def encoded(self, value):
        raise AttributeError

    @encoded.deleter
    def encoded(self):
        raise AttributeError

    @property
    def decoded(self) -> str:
        """
        :return: Return decoded string
        :rtype: :obj:`str`
        """
        return self.__decoded

    @decoded.setter
    def decoded(self, value):
        raise AttributeError

    @decoded.deleter
    def decoded(self):
        raise AttributeError
