import sys

f = open('./flag.txt', 'rb')

n = 0x009a4810d098b1cbff75682a0a9dda84315197eb4daa58186256274c0361dce60d
e = 65537

p,q=0,0

phi_n=(p-1)*(q-1)

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, x, y = egcd(b % a, a)
        return (g, y - (b // a) * x, x)

def mulinv(b, n):
    g, x, _ = egcd(b, n)
    if g == 1:
        return x % n

d = hex(mulinv(e, phi_n))
print(d)
