import base64
import sys

print base64.b64encode(sys.argv[1].decode('hex'))
