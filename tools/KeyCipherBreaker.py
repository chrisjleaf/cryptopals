import sys
import base64
import re
from utils import *
from ByteCipherBreaker import ByteCipherBreaker
import operator 

def transform(text, blockSize):
    blocks = []
    for i in range(0,blockSize): 
        b = ""
        for j in range(i, len(text), blockSize):
            b += text[j]
        blocks.append(b)
    return blocks


class KeyCipherBreaker(ByteCipherBreaker):
  def breakKey(self,text,maxKeyLen=40,sizesToTry=4,numSamples=5):
    dists = {}
    for i in range(1, maxKeyLen):
        d = 0.0
        for j in range(0, numSamples):
            d += hamming(text[i*(j): i*(1+j)], text[i*(1+j): i*(2+j)])
        d = d / ( numSamples * i )
        dists[i] = d

    sizes = [ size for (size, diff) in sorted(
        dists.items(), key=operator.itemgetter(1), reverse=False
        )] [0:sizesToTry]
    
    results = []
    for size in sizes:
        blocks = transform(text, size)
        
        score = 0
        key = ""
        strs = []
        for i in range(0,size):
            b, s, string = self.breakSingleByteKey(blocks[i])  
            score += s
            key += chr(b)
            strs.append(string)
        
        score = score/size
        clear = ""
        for i in range(0,len(strs[0])):
            for j in range(0,len(strs)):
                if i < len(strs[j]):
                    clear += strs[j][i]
    
        results.append((str(key),score,clear))
    def key(p):
        return p[1]
    return max(results, key=key)

if __name__ == "__main__":
    with open(sys.argv[1],'rb') as f: 
      text = "".join(f.readlines())
      text = base64.b64decode(text)
      print len(text)

    breaker = KeyCipherBreaker()

    print breaker.breakKey(text)
