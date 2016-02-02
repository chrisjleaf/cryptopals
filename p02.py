import sys
from tools.utils import strxor

str1 = sys.argv[1].decode('hex')
str2 = sys.argv[2].decode('hex')

print strxor(str1,str2).encode('hex')
