from tools.oracles import AES_ECB
from base64 import b64decode

cipher = AES_ECB("YELLOW SUBMARINE")

cypher = ""
with open('7.txt', 'r') as f:
    ts = f.readlines()
    for t in ts:
        cypher += b64decode(t.strip())

print cipher.decrypt(cypher)
