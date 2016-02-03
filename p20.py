from tools.FixedStreamCipherBreaker import FixedStreamCipherBreaker
from tools.utils import *
import struct 
from base64 import b64decode
from Crypto.Cipher import AES

with open('20.txt', 'r') as f:
    cypher = []
    ts = f.readlines()
    for t in ts:
        cypher.append( b64decode(t.strip()) )

nonce = 0
block = 0
key = randbytes(16)
cipher = AES.new(key, AES.MODE_ECB)
keystr = ""
for i in range(0,1000, 16):
    k = struct.pack("<QQ", nonce, block)
    block += 1
    keystr += cipher.encrypt(k)

cypher = [strxor(keystr,c) for c in cypher]

breaker = FixedStreamCipherBreaker()
for s in breaker.breakStreamKey(cypher):
    print s
