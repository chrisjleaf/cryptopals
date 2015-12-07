import sys

key = "ICE"
words = sys.argv[1]

def strxor(a, b):     # xor two strings of different lengths
  if len(a) > len(b):
    return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a[:len(b)], b)])
  else:
    return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a, b[:len(a)])])

cypher = ""
for i in range(0, len(words), len(key)):
  cypher += strxor(key, words[i:i+len(key)])

print cypher.encode('hex')
