from breakByteXOR import breakSingleByteXOR

with open('4.txt', 'r') as f:
    cypher = []
    ts = f.readlines()
    for t in ts:
        cypher.append( t.strip().decode('hex') )


attempts = []
for s in cypher:
    attempts.append( breakSingleByteXOR(s) )
def score(p):
    return p[1]
print max(attempts, key=score)
