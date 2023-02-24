def gcd(a,b):
  r = b%a
  if r==0:
    return a
  return gcd(r,a)

print(gcd(980,9000))
