# 11oligo.py by skeltonking2345

import math

def tm(a, c, g, t):
    if a + c + g + t <= 13: 
        o = (a + t) * 2 + (g + c) * 4
    else:
        o = 64.9 + 41 * ((g + c - 16.4) / (a + c + g + t))

    return o

print(tm(5, 7, 3, 4))
print(tm(1, 3, 5, 0))
print(tm(91, 83, 99, 79))
print(tm(5, 5, 3, 0))