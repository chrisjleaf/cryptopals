
with open('8.txt', 'r') as f:
    lines = []
    ts = f.readlines()
    for t in ts:
        lines.append( t.strip().decode('hex') )

scores = []
for s in lines:
    blocks = [s[i:i+16] for i in range(0,len(s), 16)]
    scores.append(len(blocks) - len(set(blocks)))

print scores.index(max(scores))
