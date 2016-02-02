from tools.utils import *
from base64 import b64decode
from Crypto.Cipher import AES
from tools.BreakCBCPadding import *

strings = [
    'MDAwMDAwTm93IHRoYXQgdGhlIHBhcnR5IGlzIGp1bXBpbmc=',
    'MDAwMDAxV2l0aCB0aGUgYmFzcyBraWNrZWQgaW4gYW5kIHRoZSBWZWdhJ3MgYXJlIHB1bXBpbic=',
    'MDAwMDAyUXVpY2sgdG8gdGhlIHBvaW50LCB0byB0aGUgcG9pbnQsIG5vIGZha2luZw==',
    'MDAwMDAzQ29va2luZyBNQydzIGxpa2UgYSBwb3VuZCBvZiBiYWNvbg==',
    'MDAwMDA0QnVybmluZyAnZW0sIGlmIHlvdSBhaW4ndCBxdWljayBhbmQgbmltYmxl',
    'MDAwMDA1SSBnbyBjcmF6eSB3aGVuIEkgaGVhciBhIGN5bWJhbA==',
    'MDAwMDA2QW5kIGEgaGlnaCBoYXQgd2l0aCBhIHNvdXBlZCB1cCB0ZW1wbw==',
    'MDAwMDA3SSdtIG9uIGEgcm9sbCwgaXQncyB0aW1lIHRvIGdvIHNvbG8=',
    'MDAwMDA4b2xsaW4nIGluIG15IGZpdmUgcG9pbnQgb2g=',
    'MDAwMDA5aXRoIG15IHJhZy10b3AgZG93biBzbyBteSBoYWlyIGNhbiBibG93']

key = None
def oracle():
  global key
  if (key == None):
    key = randbytes(16)
  iv = randbytes(16)

  string = b64decode(strings[randInt(0,len(strings)-1)])
  #string = b64decode(strings[3])
  print string 

  padding = 16 - (len(string) % 16)
  string += chr(padding) * padding
  
  cypher = AES.new(key, AES.MODE_CBC, iv)
  return iv + cypher.encrypt( string )

def check(c):
  global key
  iv = c[0:16]
  c = c[16:]
  
  cypher = AES.new(key, AES.MODE_CBC, iv)
  p = cypher.decrypt(c)
  if (not checkPadding(p)):
    return None
  return "OK"

print breakCBC(oracle, check)
 
