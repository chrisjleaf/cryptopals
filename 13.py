import os
from Crypto.Cipher import AES
import re
import util

key = None

def ecbOracle(plain):
  global key
  if key == None:
    key = util.randbytes(16)
  padding = 16 - (len(plain) % 16)
  plain += chr(padding) * padding

  cypher = AES.new(key, AES.MODE_ECB )
  return cypher.encrypt( plain )


def profile_for(email):
  email = re.sub("[^A-Za-z0-9@.+_-]","",email) #eat special Characters
  param = "email=" + email + "&uid=10&role=user"
  return ecbOracle(param)

def checkProfile(profile):
  global key
  if key == None:
    key = util.randbytes(16)

  cypher = AES.new(key, AES.MODE_ECB )
  o = {}
  ms = cypher.decrypt( profile )
  ms = ms[:-ord(ms[-1])]
  for m in ms.split("&"):
    ps = m.split("=")
    o[ps[0]] = ps[1]
 
  return (ms,o)

def checkAdmin(profile):
  (ms, o) = checkProfile(profile)
  return o['role'] == "admin"

def cutNPaste(oracle):
  e1 = oracle("foobarbaz@admin")
  e2 = oracle("fooba@xyz.com")

  return e2[0:32] + e1[16:32] + e1[0:16] + e2[32:]

profile = cutNPaste(profile_for)
if checkAdmin(profile) == True:
  print "User is an Admin"
else: 
  print "User is NOT an Admin"

