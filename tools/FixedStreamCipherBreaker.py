from KeyCipherBreaker import KeyCipherBreaker

class FixedStreamCipherBreaker(KeyCipherBreaker):
    def breakStreamKey(self, messages):
        o = messages
        d = {}
        for i in range(len(messages)):
            d[messages[i]] = ""
        offset = 0
        while (len(messages) > 0):
            l = min( [len(m) for m in messages] )
            ms, ps = self._nextIter(messages,l,offset)
            for i in range(0,len(ms)):
                p = d[ms[i]]
                d[ms[i]] = p + ps[i]
            offset += l
            messages = [m for m in messages if len(m) > l]
            break #Some Reason the recursion isn't working...
        return [ d[m] for m in o ]

    def _nextIter(self, messages, l, offset=0):    
        truncated = [m[:l] for m in messages]
        targets = "".join([ m[offset:] for m in truncated])
        _,_,t = self.divideAndConquer(targets,l)
        return (messages, [t[i:i+l] for i in range(0, len(t), l)])
