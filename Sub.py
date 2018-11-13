import operator

f = open('./sub.txt', 'r').read()

def freq(ciphertext):
    dict = {}
    total = 0

    for c in ciphertext:
        dict[c] = 0

    for c in ciphertext:
        dict[c] = dict[c] + 1
        total+=1

    for c in ciphertext:
        dict[c] = dict[c]

    s_d = reversed(sorted(dict.items(), key=operator.itemgetter(1)))

    [print(x) for x in s_d]

#freq(f)

alphabet =  'abcdefghijklmnopqrstuvwxyz'
key =       '    u  z           i     '
alphakey = {}

for i in range(26):
    alphakey[key[i]] = alphabet[i]
print(alphakey)

def replace(code, alphakey):
    msg = list(code)
    for i in range(len(msg)):
        try:
            msg[i] = alphakey[msg[i]]
        except Exception:
            msg[i] = ' '

    return ''.join(msg)

print(replace(f, alphakey))
