import os
from Crypto.Cipher import AES
import re
from tools.utils import *

key = None
iv = None
def cbcOracle(plain):
  global key
  global iv
  if key == None:
    key = randbytes(16)
  if iv == None:
    iv = randbytes(16)
  padding = 16 - (len(plain) % 16)
  plain += chr(padding) * padding

  cypher = AES.new(key, AES.MODE_CBC, iv)
  return iv + cypher.encrypt( plain )


def wrap_text(text):
  text = re.sub("[^A-Za-z0-9@.+_-]","",text) #eat special Characters
  param = "comment1=cooking%20MCs;userdata=" + text + ";comment2=%20like%20a%20pound%20of%20bacon"
  return cbcOracle(param)


def checkProfile(profile):
  global key
  global iv 
  if key == None:
    key = randbytes(16)
  iv = profile[0:16]
  profile = profile[16:]
  cypher = AES.new(key, AES.MODE_CBC, iv )
  
  o = {}
  ms = cypher.decrypt( profile )
  ms = ms[:-ord(ms[-1])]
  for m in ms.split(";"):
    ps = m.split("=")
    o[ps[0]] = ps[1]
 
  return (ms,o)

def checkAdmin(profile):
 (ms, o) = checkProfile(profile)
 return o['admin'].lower() == "true"

def bitFlipping(oracle):
  c = oracle("YELLOW_SUBMARINE" * 2)
  change = strxor("YELLOW_SUBMARINE","aaaaa;admin=true")
  c = strxor( ('\x00'*16*3) + change + '\x00'*(len(c) - 4*16) , c) 
  return c

profile = bitFlipping(wrap_text)
if checkAdmin(profile) == True:
  print "User is an Admin"
else: 
  print "User is NOT an Admin"

