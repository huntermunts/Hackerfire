import sys

f = open('./flag.txt', 'rb')

n = 69783507722178132619820485783352049428969858299739616863075072996637000132109 #0x009a4810d098b1cbff75682a0a9dda84315197eb4daa58186256274c0361dce60d
e = 65537

p = 335445381412686320307419854821396116851
q = 208032399874738495835162222153730872959

phi_n = (p - 1) * (q - 1)


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


d = mulinv(e, phi_n)
print(d)

dp = mulinv(e,(p-1))
dq = mulinv(e,(q-1))
qi = mulinv(q,p)

print(dp)
print(dq)
print(qi)

openssl asn1parse -genconf <path to above file> -out newkey.der
openssl rsa -in newkey.der -inform der -text -check
