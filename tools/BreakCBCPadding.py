from oracles import *
from utils import *

def _nextByte(check, known, targets):
  valid = None
  for c in range(0,256):
    pad = len(known) + 1
    pad = chr(pad)*pad
    guess = targets[:15-len(known)]
    guess = guess + strxor( targets[15-len(known):16], 
                            strxor(pad, chr(c) + known) ) 
    guess = guess + targets[16:]
    
    if ( not check(guess) == None ):
      if len(known) == 0:
        guess = targets[:14]
        guess = guess + strxor( targets[14:16], strxor('\x01' + pad, '\x00' + chr(c)) ) 
        guess = guess + targets[16:]
        if not check(guess) == None:
          valid = c
      else:
        valid = c
     
  return valid

def breakCBC(req, check):
  cipher = req()
  numBlocks = len(cipher)/16
  secret = ''
  for i in range(0,numBlocks-1):
    targets = cipher[i*16:i*16+32]
    s = ''
    for i in range(0,16):
      c = _nextByte(check, s, targets)
      if c == None:
        return secret + s
      s = chr(c) + s
    secret += s

  return secret

