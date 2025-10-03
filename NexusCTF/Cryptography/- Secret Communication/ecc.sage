from random import randint

# Our secret key
secret = randint(2<<109, 2<<110)

# Elliptic curve we agreed upon
p = 3391454550160661115094033672759471
E = EllipticCurve(GF(p), [1,0])

assert p > secret

G = E.gens()[0]

# Our public key, good thing Elliptic Curve is so secure no one could even get our secret key from the public key alone !
Q = secret * G

# Their public key, change with what they give
P = randint(2<<110, 2<<111) * G

# Use this as a proof that we are MPLF
shared_secret = secret*P