ASCII_LOWERCASE = tuple('abcdefghijklmnopqrstuvwxyz')
ASCII_UPPERCASE = tuple('ABCDEFGHIJKLMNOPQRSTUVWXYZ')


class BadString(Exception):
    def __init__(self, raw_string):
        self.raw_string = raw_string

    def __str__(self):
        return f"Bad String -> {self.raw_string}"


class CaesarCypher:
    """
    Docs)
    """

    def __init__(self, raw_string: str, key: int):
        if not raw_string.isascii():
            raise BadString(raw_string)

        self.raw_string = raw_string
        self.key = key
        self.encoded_string = self.caesar_encode(self.key)
        self.decoded_string = self.caesar_decode(self.key)

    def caesar_encode(self, key: int):
        self.encoded_string = ''.join(
            [(lambda k: ASCII_LOWERCASE[abs(k % 26)])(ASCII_LOWERCASE.index(char) + key)
             if char in ASCII_LOWERCASE else
             (lambda k: ASCII_UPPERCASE[abs(k % 26)])(ASCII_UPPERCASE.index(char) + key)
             if char in ASCII_UPPERCASE else ' '
             for char in self.raw_string]
        )
        return self.encoded_string

    def caesar_decode(self, key: int):
        self.decoded_string = ''.join(
            [(lambda k: ASCII_LOWERCASE[abs(k % 26)])(ASCII_LOWERCASE.index(char) - key)
             if char in ASCII_LOWERCASE else
             (lambda k: ASCII_UPPERCASE[abs(k % 26)])(ASCII_UPPERCASE.index(char) - key)
             if char in ASCII_UPPERCASE else ' '
             for char in self.raw_string]
        )
        return self.decoded_string

    def __str__(self):
        return "RAW: {}\n" \
               "Key: {}\n" \
               "Encoded: {}\n" \
               "Decoded: {}".format(self.raw_string, self.key, self.encoded_string, self.decoded_string)

    def __repr__(self):
        return self.__str__()


class CaesarCracker:
    """
    Crack Caesar Cypher.

    Brute all 26 keys
    """

    def __init__(self, raw_string):
        self.raw_string = raw_string
        self.cracked = None

        self.crack()

    def crack(self):
        self.cracked = ["{}: {}".format(i, string) for i, string in
                        enumerate([CaesarCypher(self.raw_string, key).decoded_string for key in range(1, 27)], start=1)]
        return self.cracked

    def __str__(self):
        return "\n".join(self.cracked)

    def __repr__(self):
        return self.__str__()
