# CypherX

Tool to encode and decode simple cyphers.

___

### CaesarCypher

Encode and decode Caesar cypher.
```python
from CypherX import CaesarCypher

cypher = CaesarCypher("Hello World!!!", 13)

print(cypher)

"""
RAW: Hello World!!!
Key: 13
Encoded: Uryyb Jbeyq!!!
Decoded: Uryyb Jbeyq!!!
"""

print(cypher.encoded)

"""
Uryyb Jbeyq!!!
"""

```

___

### CaesarCracker

Crack Caesar cypher.

```python
from CypherX import CaesarCracker

cracker = CaesarCracker("Uryyb Jbeyq!!!")

print(cracker)

"""
...
12: Ifmmp Xpsme!!!
13: Hello World!!!
14: Gdkkn Vnqkc!!!
...
"""
```

---

### VigenereCypher

Encode and decode Caesar cypher.
```python
from CypherX import VigenereCypher

cypher = VigenereCypher("Hello World!!!", "pizza")

print(cypher)

"""
RAW: Hello World!!!
Key: [15, 8, 25, 25, 0]
Encoded: Wmkko Lwqkd!!!
Decoded: Swmmo Hgsmd!!!
"""

print(cypher.encoded)

"""
Wmkko Lwqkd!!!
"""

```

___
