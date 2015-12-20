import os
from random import randint
from Crypto.Cipher import AES
from base64 import b64decode
import util

suffix = b64decode ("Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkg\
    aGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBq\
    dXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUgYnkK")

key = None

def encryptionOracle(plain):
  global key
  if key == None:
    key = 'A' * 16 #util.randbytes(16)
  plain = plain + suffix
  padding = 16 - (len(plain) % 16)
  plain += chr(padding) * padding

  cypher = AES.new(key, AES.MODE_ECB )
  return cypher.encrypt( plain )

def detectBlockSize(oracle):
  length = len( oracle("") )
  i = 0
  while True:
    l = len( oracle("A" * i) )
    if length != l:
      return l - length
    i = i + 1
    
def detectMode(oracle,bsize):
  msg = "A" * bsize * 4
  enc = oracle( msg )
  
  if enc[bsize:bsize*2] == enc[bsize*2:bsize*3]:
    mode = "ECB"
  else: 
    mode = "CBC"
  
  return mode

def nextByte(oracle, known, blockSize):
  padding = "A" * (blockSize - (len(known) % blockSize) - 1)
  d = {}
  for i in range(0,256):
    t = padding + known + chr(i)
    enc = oracle( t )[0:len(padding) + len(known) + 1]
    d[enc] = chr(i)
  enc = oracle(padding)[0:len(padding) + len(known) + 1]
  if enc in d:
    return d[enc]
  return None

if __name__ == '__main__':
  blockSize = detectBlockSize(encryptionOracle)
  print blockSize

  mode = detectMode(encryptionOracle, blockSize)
  print mode

  known = 'R'
  while True:
    b = nextByte(encryptionOracle, known, blockSize)
    if b == None:
      break
    known += b
  print known
