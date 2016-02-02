from Crypto.Random import random

def strxor(a, b):     # xor two strings of different lengths
  if len(a) > len(b):
    return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a[:len(b)], b)])
  else:
    return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a, b[:len(a)])])

def cipher_enc(text, key):
  c = ""
  for i in range(0, len(text), len(key)):
    c += strxor(key, text[i:i+len(key)])
  return c



def hamming(str1,str2):
  total = 0
  length = min(len(str1), len(str2))
  for i in range(0,length):
    diff = ord(str1[i]) ^ ord(str2[i])
    for i in range(0,8):
      total += diff & 0x1
      diff = diff >> 1
  return total

def pad_pkcs7(text,block_length=16):
  pad_length = block_length - ( len(text) % block_length )
  if pad_length == 0:
    pad_length = block_length

  return text + chr(pad_length)*pad_length

def checkPadding(message):
  lastByte = message[-1]
  if ord(lastByte) == 0:
    return False
  for i in range(1,ord(lastByte)+1):
    if message[-i] != lastByte:
      return False
  return True

def randbytes(k):
  return random.long_to_bytes(random.getrandbits(8*k))

def randInt(a,b):
  return random.randint(a,b)
