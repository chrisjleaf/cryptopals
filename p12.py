import os
from Crypto.Cipher import AES
from base64 import b64decode
from tools.utils import *
from tools.oracles import *
from tools.BreakECBPadding import *

suffix = b64decode ("Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkg\
    aGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBq\
    dXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUgYnkK")

key = None

def encryptionOracle(plain):
  global key
  if key == None:
    key = randbytes(16)
  plain = plain + suffix
  padding = 16 - (len(plain) % 16)
  plain += chr(padding) * padding

  cypher = AES.new(key, AES.MODE_ECB )
  return cypher.encrypt( plain )

print breakECB(encryptionOracle)
