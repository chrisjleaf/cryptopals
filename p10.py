from Crypto.Cipher import AES
from tools.utils import *
from base64 import b64decode

def CBC_decrypt(cipher, text, IV):
  previous = IV
  blockLen = 16
  plain = ""
  for i in range(0,len(text),blockLen):
    block = text[i:i+blockLen]
    t = cipher.decrypt(block)
    plain += strxor(t,previous)
    previous = block
  padLen = ord(plain[-1])
  return plain[:-padLen]


def CBC_encrypt(cipher, text, IV):
  previous = IV
  blockLen = 16
  cipher_text = ""
  text = pad_pkcs7(text, blockLen)

  for i in range(0,len(text),blockLen):
    t = strxor(text[i:i+16], previous)
    block = cipher.encrypt(t)
    cipher_text += block
    previous = block

  return cipher_text

cypher = ""
with open('10.txt', 'r') as f:
    ts = f.readlines()
    for t in ts:
        cypher += b64decode(t.strip())

c = AES.new("YELLOW SUBMARINE", AES.MODE_ECB)
print CBC_decrypt(c, cypher, '\x00'*16)
