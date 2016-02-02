import os
from random import randint
from Crypto.Cipher import AES
from tools.oracles import detectMode

def encryptionOracle(plain, mode):
  key = os.urandom(16)
  plain = os.urandom( randint(5,10) ) + plain + os.urandom( randint(5,10) )
  padding = 16 - (len(plain) % 16)
  plain += chr(padding) * padding

  if mode == "CBC":
    cypher = AES.new(key, AES.MODE_CBC, os.urandom(16) )
  else: 
    mode = "ECB"
    cypher = AES.new(key, AES.MODE_ECB, os.urandom(16) )

  return cypher.encrypt( plain )

if __name__ == '__main__':
  num = 10000
  correct = 0
  for i in range(0,num):
    mode = "CBC"
    if randint(0,10) % 2:
      mode = "ECB"
    def f (x) : return encryptionOracle(x, mode) 
    if  mode == detectMode(f):
      correct += 1

  print str(100 * correct / num) + "% Correctly detected"
