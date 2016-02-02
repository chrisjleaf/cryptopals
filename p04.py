from tools.KeyCipherBreaker import KeyCipherBreaker

with open('4.txt', 'r') as f:
    cypher = []
    ts = f.readlines()
    for t in ts:
        cypher.append( t.strip().decode('hex') )


attempts = []
breaker = KeyCipherBreaker()
for s in cypher:
    attempts.append( breaker.breakSingleByteKey(s) )
def score(p):
    return p[1]
print max(attempts, key=score)
