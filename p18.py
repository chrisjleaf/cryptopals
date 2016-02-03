from tools.utils import strxor
import struct 
import sys

from Crypto.Cipher import AES

key = "YELLOW SUBMARINE"
nonce = 0
block = 0

c = sys.argv[1]
cipher = AES.new(key, AES.MODE_ECB)

keystr = ""
for i in range(0,len(c), 16):
    k = struct.pack("<QQ", nonce, block)
    block += 1
    keystr += cipher.encrypt(k)

print strxor(keystr, c)

