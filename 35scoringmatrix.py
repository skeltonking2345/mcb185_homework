#scoringmatrix.py by skeltonking2345

import sys

alphabet = sys.argv[1]
match = sys.argv[2]
mismatch = sys.argv[3]

#line 1
aas = list(alphabet)
for i, letter in enumerate(aas):
    if i == 0:
        print(f'{letter:>4}', end='  ')
    else:
        print(letter, end='  ')
print()

def matormis(a, b):
    if a == b:
        return match
    else:
        return mismatch

for i in range(len(alphabet)):
    row = f'{alphabet[i]}'
    for j in range(len(alphabet)):
        out = matormis(alphabet[i], alphabet[j])
        row += f' {out}'
    print(row, sep=' ')

