import os
from Crypto.Cipher import AES

def AES_ECB(key):
  return AES.new(key, AES.MODE_ECB)

