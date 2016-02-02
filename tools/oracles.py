import os
from Crypto.Cipher import AES

def AES_ECB(key):
  return AES.new(key, AES.MODE_ECB)

def detectMode(oracle,bsize=16):
  msg = "A" * 16 * 4
  enc = oracle( msg )
  
  if enc[bsize:bsize*2] == enc[bsize*2:bsize*3]:
    mode = "ECB"
  else: 
    mode = "CBC"
  
  return mode

### ONLY FOR ECB MODE ###

def detectBlockSize(oracle):
  length = len( oracle("") )
  i = 0
  while True:
    l = len( oracle("A" * i) )
    if length != l:
      return l - length
    i = i + 1
