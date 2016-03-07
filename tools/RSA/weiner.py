from fractions import Fraction
import binascii
import gmpy2 as g
ctx = g.context(precision=10000000,round=g.RoundUp)
g.set_context(ctx)

def f2cf(nu, de):
  '''
  Fraction nu/de to continued fraction
  '''
  cf = []
  while de:
    qu = nu // de
    cf.append(qu)
    nu, de = de, nu - de*qu
  return cf

def cf2f(cf):
  '''
  Continued fraction to fraction
  '''
  f = Fraction(0, 1)
  for x in reversed(cf):
    try:
      f = 1 / (f+x)
    except ZeroDivisionError:
      return Fraction(0, 1)
  return 1/f

def cf2cvg(cf):
  '''
  Continued faction to convergents
  '''
  for i in range(1,len(cf)+1):
      yield cf2f(cf[:i])

def weiner(N,e):
  for c in cf2cvg(f2cf(e,N)):
    k = c.numerator
    if k == 0:
      continue
    d = c.denominator
    phi = (e*d - 1) / k
    b = N - phi + 1
    det = b*b - 4*N
    if det < 0: 
      continue
    root = long(g.sqrt(det))
    if root * root == det and not (b + root) & 1:
      p = g.mpz((b + root) / 2)
      q = g.mpz((b - root) / 2)
      d = g.mpz(d)
      if checkFactors(g.mpz(p),g.mpz(q),g.mpz(N)):
        return (p,q,d)
      raise Exception("Invalid result generated")

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
  P,Q,D = weiner(N,e)
  phi = g.mul( g.sub(P,1), g.sub(Q,1) ) 
  checkD(e,D,phi)
  return (P,Q,D)

if __name__ == '__main__':
  N = g.mpz("9C2F6505899120906E5AFBD755C92FEC429FBA194466F06AAE484FA33CABA720205E94CE9B\
      F5AA527224916D1852AE07915FBC6A3A52045857E0A1224C72A360C01C0CEF388F1693A746D5AFBF318C0AB\
      F027661ACAB54E0290DFA21C3616A498210E2578121D7C23877429331D428D756B957EB41ECAB1EAAD87018\
      C6EA3445",16)
  e = g.mpz("466A169E8C14AC89F39B5B0357EFFC3E2139F9B19E28C1E299F18B54952A07A932BA5CA9F4\
      B93B3EAA5A12C4856981EE1A31A5B47A0068FF081FA3C8C2C546FEAA3619FD6EC7DD71C9A2E75F1301EC935\
      F7A5B744A73DF34D21C47592E149074A3CCEF749ECE475E3B6B0C8EECAC7C55290FF148E9A29DB8480CFE2A\
      57801275",16)

  P,Q,D = breakKey(long(N),long(e))
  print "P = " + str(long(P))
  print "Q = " + str(long(Q))
  print "D = " + str(D)
