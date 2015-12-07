import sys
import base64
import re
from Crypto.Util.strxor import strxor_c


def strxor(a, b):     # xor two strings of different lengths
  if len(a) > len(b):
    return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a[:len(b)], b)])
  else:
    return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a, b[:len(a)])])

freqs = {
    'a': 0.0651738,
    'b': 0.0124248,
    'c': 0.0217339,
    'd': 0.0349835,
    'e': 0.1041442,
    'f': 0.0197881,
    'g': 0.0158610,
    'h': 0.0492888,
    'i': 0.0558094,
    'j': 0.0009033,
    'k': 0.0050529,
    'l': 0.0331490,
    'm': 0.0202124,
    'n': 0.0564513,
    'o': 0.0596302,
    'p': 0.0137645,
    'q': 0.0008606,
    'r': 0.0497563,
    's': 0.0515760,
    't': 0.0729357,
    'u': 0.0225134,
    'v': 0.0082903,
    'w': 0.0171272,
    'x': 0.0013692,
    'y': 0.0145984,
    'z': 0.0007836,
    ' ': 0.1918182
}

def score(s):
    score = 0
    s = s.lower()
    keys = freqs.keys()
    for c in s:
      if c in keys:
        score += freqs[c]
    return score

def breakSingleByteXOR(s):
  bestScore = -100
  bestKey = 0
  for i in range(0,256):
    t = score(strxor_c(s,i))
    if t > bestScore:
      bestScore = t
      bestKey = i
  return chr(bestKey)

def hamming(str1, str2): 
  total = 0
  length = min(len(str1), len(str2))
  for i in range(0,length):
    diff = ord(str1[i]) ^ ord(str2[i])
    for i in range(0,8):
      total += diff & 0x1
      diff = diff >> 1
  return total

with open(sys.argv[1],'rb') as f: 
  text = "".join(f.readlines())
  text = base64.b64decode(text)
  print len(text)

diffs = []
for keysize in range(2,40):
  for i in range(0,4):
    diff = hamming(text[keysize*i:keysize*(i+1)], text[keysize*(i+1):keysize*(i+2)])
  diff = diff/4

  diffs.append({keysize:diff})

# Only these sizes are particularly small
for keysize in range(2,12):
  key = ""
  for i in range(0,keysize):
    block = ""
    for j in range(i,len(text),keysize):
      block += text[j]
    key += breakSingleByteXOR(block)
  message = ""
  print key.encode('hex') + ":" + str(keysize)
  for i in range(0,len(text), keysize): 
    message += strxor(key, text[i:i+keysize])
  print ">>>>>" + message + "<<<<<"

  
