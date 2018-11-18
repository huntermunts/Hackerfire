msgs=[
0x616263,
0x646566,
0x676869,
0x707172,
0x737475,
0x767778
]

key=0x123456

ciphers = [msg^key for msg in msgs]

def getKey(m, g):
    print(g[0] ^ g[1], m[0] ^ m[1])
    print(g[1] ^ g[2], m[1] ^ m[2])
    print(g[2] ^ g[3], m[2] ^ m[3])
    print(g[3] ^ g[4], m[3] ^ m[4])
    print(g[4] ^ g[5], m[4] ^ m[5])

    return 0x123456

print(hex(getKey(msgs, ciphers)))
