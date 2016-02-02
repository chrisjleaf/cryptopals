
def randbytes(k):
  return random.long_to_bytes(random.getrandbits(8*k))

def padPKCS7(x, k):
  ch = k - (len(x) % k)
  return x + bytes([ch] * ch)
