# 12phred.py by skeltonking2345

import math

def char_to_prob(a):
    x = ord(a) - 33
    y = 10 ** -(x / 10)
    
    return y

def prob_to_char(a):
    x = -10 * math.log10(a)
    y = round(x) + 33
    if 0 <= y <= 127:
        z = chr(y) 
    else:
        z = 'none'
    return z

print(char_to_prob('A'))
print(char_to_prob('C'))
print(char_to_prob('8'))
print(chr(65))
print(prob_to_char(0.001))
print(prob_to_char(.0000000000000000000000000003))
print(prob_to_char(1))