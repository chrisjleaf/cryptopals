from tools.KeyCipherBreaker import KeyCipherBreaker
from base64 import b64decode

cypher = ""
with open('6.txt', 'r') as f:
    ts = f.readlines()
    for t in ts:
        cypher += b64decode(t.strip())

breaker = KeyCipherBreaker()
print breaker.breakKey(cypher)
