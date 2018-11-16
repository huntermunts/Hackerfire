import operator
import itertools

f = open('./sub.txt', 'r').read()

def freq(ciphertext):
    dict = {}
    total = 0

    for c in ciphertext:
        dict[c] = 0

    for c in ciphertext:
        dict[c] = dict[c] + 1
        total+=1

    s_d = reversed(sorted(dict.items(), key=operator.itemgetter(1)))

    [print(x) for x in s_d]

#freq(f)

alphabet =  'abcdefghijklmnopqrstuvwxyz '
key =       'jndeurmzkqlptwfhcgyiasvbx  '
dict = {}

for a, k in zip(alphabet, key):
    dict[k] = a

def replace(code):
    msg = list(code)
    for i in range(len(msg)):
        try:
            msg[i] = dict[msg[i]]
        except Exception:
            pass
    print(''.join(msg))

replace(f)
