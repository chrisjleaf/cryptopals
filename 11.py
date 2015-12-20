import os
from random import randint
from Crypto.Cipher import AES

def encryptionOracle(plain):
  key = os.urandom(16)
  plain = os.urandom( randint(5,10) ) + plain + os.urandom( randint(5,10) )
  padding = 16 - (len(plain) % 16)
  plain += chr(padding) * padding

  if randint(0,10) % 2:
    mode = "CBC"
    cypher = AES.new(key, AES.MODE_CBC, os.urandom(16) )
  else: 
    mode = "ECB"
    cypher = AES.new(key, AES.MODE_ECB, os.urandom(16) )

  return (mode, cypher.encrypt( plain ) )

def detectMode(oracle):
  msg = "A" * 16 * 4
  m, enc = oracle( msg )
  
  if enc[16:32] == enc[32:48]:
    mode = "ECB"
  else: 
    mode = "CBC"
  
  print mode == m

if __name__ == '__main__':
  for i in range(0,10):
    detectMode(encryptionOracle)
