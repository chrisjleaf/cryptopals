
def strxor(a, b):
    ret = ""
    if len(a) < len(b): 
        l = len(a)
    else: 
        l = len(b)
    for i in range(0,l):
        ret += chr( ord(a[i]) ^ ord(b[i]) )
    return ret
