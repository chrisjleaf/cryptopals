import sys
from tools.KeyCipherBreaker import KeyCipherBreaker

text = sys.argv[1].decode('hex')

breaker = KeyCipherBreaker()
print breaker.breakSingleByteKey(text)
