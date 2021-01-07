XORCypher
-------------
Simple XOR encoder and decoder.

:Example:
    >>> from CypherX import XORCypher
    >>> string = "Hello world"
    >>> key = "super random secret key"
    >>> xor = XORCypher(string, key)
    >>> print(xor.encoded)
    >>> b'OxAcCR0ABQ4cCAs='
    >>>
    >>> xor = XORCypher('OxAcCR0ABQ4cCAs=', key)
    >>> print(xor.decoded)
    >>> 'Hello world'

:Fast access:
    >>> from CypherX import XORCypher
    >>> print(XORCypher.encode('Hello world', 'super random secret key'))
    >>> b'OxAcCR0ABQ4cCAs='

.. autoclass:: CypherX.XORCypher
    :members:
    :inherited-members:
    :show-inheritance:

