from hamming import strDiff
from base64 import b64decode
from breakByteXOR import breakSingleByteXOR
maxKeysize = 40
dists = {}

def transform(text, blockSize):
    blocks = []
    for i in range(0,blockSize): 
        b = ""
        for j in range(i, len(text), blockSize):
            b += text[j]
        blocks.append(b)
    return blocks


def popSmallest(dists):
    smallestValue = 10 # Bigger than any possible hamming distance
    smallestKey = 0
    for k in dists.keys():
        if smallestValue > dists[k]:
            smallestValue = dists[k]
            smallestKey = k
    
    dists.pop(smallestKey)
    return smallestKey

cypher = ""
with open('6.txt', 'r') as f:
    ts = f.readlines()
    for t in ts:
        cypher += b64decode(t.strip())


print "Cypher Length: " + str(len(cypher))
numSamples = 10
for i in range(1, maxKeysize):
    d = 0.0
    for j in range(0, numSamples):
        d += strDiff(cypher[i*(j): i*(1+j)], cypher[i*(1+j): i*(2+j)])
    d = d / ( numSamples * i )
    dists[i] = d

sizes = []
numKeysizes = 5
for i in range(0, numKeysizes):
    sizes.append( popSmallest(dists) )

results = []
for size in sizes:
    blocks = transform(cypher, size)
    
    score = 0
    key = ""
    strs = []
    for i in range(0,size):
        b, s, string = breakSingleByteXOR(blocks[i])  
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
print max(results, key=key)
