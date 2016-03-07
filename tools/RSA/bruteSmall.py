import gmpy2 as g
import binascii
import sys

ctx = g.context(precision=10000000,round=g.RoundUp)
g.set_context(ctx)

def bruteSmall(N):
  zero = g.mpz(0)
  two = g.mpz(2)
  if g.f_mod(N, two) == zero:
    return two, g.mpz(g.div(N, two))

  i = g.mpz(3)
  while True:
    if g.f_mod(N, i) == zero:
      p = g.mpz(i)
      q = g.mpz( g.div(N,i) )
      if checkFactors(p,q,N) :
        return p,q
    i = g.add(i, two)

def checkFactors(p,q,N):
  x = g.f_mod( N, p )
  y = g.f_mod( N, q )
  zero = g.mpz('0')
  if g.is_prime(p) and g.is_prime(q):
    return N == g.mul(p,q) and x == zero and y == zero
  return False

def checkD(e,d,phi):
  if not g.f_mod( g.mul(e,d), phi ) == g.mpz('1'):
    raise Exception("Bad D generated")

def breakKey(N,e):
  P,Q = bruteSmall(N)

  phi = g.mul( g.sub(P,1), g.sub(Q,1) ) 
  D = g.invert(e,phi)
  checkD(e,D,phi)
  return (P,Q,D)

if __name__ == "__main__": 
  N = g.mpz("BAD20CF97ED5042DF696CE4DF3E5A678CF4FB3693D3DF12DFE9FD3FD8CC8AAB8B95533E414E3F\
    C0C377F4EE54827118B1D30561A3C741BEA7C76899789B51743E076092DF9EB05DC97EB1505CE9EB12B5AB9E\
    10ABF56F920A58E7E00ECF05977E872834DD8584CF4AC87CB7DC50159BD962C75CBEFB6C6AC3A31A74E7D8F1\
    E4C10D5",16)

  e = g.mpz("65537")
  p,q,d = breakKey(N,e)
  print "P = " + str(p)
  print "Q = " + str(q)
  print "D = " + str(d)
