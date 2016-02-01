import pickle

with open('hamming.pickle','rb') as f:
    dist = pickle.load(f)

def byteDiff(a,b):
    return dist[a][b]

def strDiff(a,b):
    if len(a) < len(b):
        l = len(a)
    else: 
        l = len(b)
    diff = 0
    for i in range(0,l):
        diff += byteDiff(ord(a[i]),ord(b[i]))
    return diff
