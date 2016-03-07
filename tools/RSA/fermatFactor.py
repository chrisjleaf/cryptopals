import gmpy2 
import binascii

ctx = gmpy2.context(precision=10000000,round=gmpy2.RoundUp)
gmpy2.set_context(ctx)


def FermatFactor(N):
  A = gmpy2.mpz( gmpy2.ceil( gmpy2.sqrt(N) ) )
  B2 = gmpy2.sub( gmpy2.square(A), N )

  while not gmpy2.is_square(B2): 
    A = gmpy2.add( A, gmpy2.mpz("1") )
    B2 = gmpy2.sub( gmpy2.square(A), N )
  
  B = gmpy2.sqrt(B2)
  P = gmpy2.mpz( gmpy2.sub( A, B ) )
  Q = gmpy2.mpz( gmpy2.add( A, B ) )
  if not checkFactors(P,Q,N):
    raise Exception("Bad factors generated")
  return ( P, Q )

def checkFactors(p,q,N):
  x = gmpy2.f_mod( N, p )
  y = gmpy2.f_mod( N, q )
  zero = gmpy2.mpz('0')
  if g.is_prime(p) and g.is_prime(q):
    return N == g.mul(p,q) and x == zero and y == zero
  return False

def checkD(e,d,phi):
  if not gmpy2.f_mod( gmpy2.mul(e,d), phi ) == gmpy2.mpz('1'):
    raise Exception("Bad D generated")

def breakKey(N,e):
  P,Q = FermatFactor(N)

  phi = gmpy2.mul( gmpy2.sub(P,1), gmpy2.sub(Q,1) ) 
  D = gmpy2.invert(e,phi)
  checkD(e,D,phi)
  return (P,Q,D)

if __name__ == '__main__':
  N = gmpy2.mpz("9473874079694384096182353069577870140898775728758349266591973001797384713834\
      551113906459611342243597758385684388700816820200385590670803901348734939057180114140724\
      503901159881054223202963456484879799853487225154966045427733650283818564293763757612153\
      3945369150901808833844341421315429263207612372324026271327")
  e = gmpy2.mpz("65537")

  P,Q,D = breakKey(N,e)
  print "P = " + str(long(P))
  print "Q = " + str(long(Q))
  print "D = " + str(D)
