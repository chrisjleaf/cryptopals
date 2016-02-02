from oracles import *


def _nextByte(oracle, known, blockSize):
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


def breakECB(oracle):
  blockSize = detectBlockSize(oracle)
  print blockSize

  mode = detectMode(oracle, blockSize)
  print mode

  secret = ''
  while True:
    b = _nextByte(oracle, secret, blockSize)
    if b == None:
      break
    secret += b
  return secret
