from tools.utils import pad_pkcs7
import sys 

padded = pad_pkcs7(sys.argv[1], block_length=20)
print padded.encode('hex')

