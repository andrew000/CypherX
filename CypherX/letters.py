"""
We don't use 'string' library because it has not Cyrillic chars.

We calculate the lengths of the alphabets in advance so as not to count them during cipher calculations.

So be nice)
"""

_ASCII_LOWERCASE = 'abcdefghijklmnopqrstuvwxyz'
_ASCII_UPPERCASE = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
_CYRILLIC_LOWERCASE = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяі'
_CYRILLIC_UPPERCASE = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯІ'

_LEN_ASCII_LOWERCASE = len(_ASCII_LOWERCASE)
_LEN_ASCII_UPPERCASE = len(_ASCII_UPPERCASE)
_LEN_CYRILLIC_LOWERCASE = len(_CYRILLIC_LOWERCASE)
_LEN_CYRILLIC_UPPERCASE = len(_CYRILLIC_UPPERCASE)
