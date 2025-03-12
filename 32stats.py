#32stats.py

import sys
import math

data = []
for arg in sys.argv[1:]:
    f = float(arg)
    data.append(f)

def points(a):
    return len(a)
print('data points', points(sys.argv[1:]))

def high(a):
    max = a[-1]
    for a2 in a[-2::-1]:
        if a2 > max : max = a2
    return max

def low(a):
    min = a[0]
    for a1 in a[1:]:
        if a1 < min : min = a1
    return min

print('min', low(sys.argv[1:]))
print('max', high(sys.argv[1:]))

def mean(a):
    return sum(a) / len(a)

print('mean', mean(data))

def standev(a):
    sum = 0
    for i in a:
        sum += (i - mean(a)) ** 2
    sd = math.sqrt(sum / points(a))
    return sd
print('sdev', standev(data))

def median(a):
    data.sort()
    n = points(a)
    if n % 2 == 1:
        return data[n // 2]
    else: 
        return data[n//2], data[n//2-1]
print('median', median(data))
