# 10demo.py by skeltonking2345 (Steve Ho)

import math

print('hello again') # greeting

print("""
multi_line
 comment
 """) # multi-line comment testing

print(1.5e-2)
print(8 ** 4)
print(5 + 4 ** (4 + 9))
print(abs(-123))
print(pow(98,27))
print(round(17/3, ndigits=4))
print(round(pow(0.999,31), ndigits=7)) # math operator and function testing
print(math.ceil(6.9)) # round up test
print(0.1 * 3) # real numbers test

a = 4
b = 7
c = math.sqrt(a**2 + b**2)
print(c)
print(type(a), type(b), type(c), sep=', ', end='!?!\n') # math imported functions testing

def pythagoaras(a, b): return math.sqrt(a**2 + b**2) # indentation ommited

print(pythagoaras(3, 4)) # function after deleting c and hyp

# area practice
def circle_area(r): return math.pi * r**2
def rectangle_area(w, h): return w * h
def square_area(s): return s * s
def sphere_volume(r): return (4/3) * math.pi * r**3


print(sphere_volume(2))
hw = 'hello world'
print(hw) # i didn't add the type part, im not sure what it did

a = 0.3
b = 0.1 * 3
if a == b:
    print('a equals b')
if a != b:
    print('a is not b') # if conditionals

def is_even(x):
    if x % 2 ==0: return True
    return False
print(is_even(2))
print(is_even(3)) # conditional practice

c = a == b
print(c)
print(type(c)) # bool sounds pretty funny BOOL!

print('a and b relation')
if a < b: print('a < b')
elif a > b: print('a > b')
else: print('a == b')

if a < b: print('a < b')
elif a <= b: print('a <= b')
elif a == b: print('if this prints you have fucked up') # redundant elif test

if a < b or a > b: print('a and b are not equality')
if a < b and a > b: print('aw hell nah something is wrong')
if not False: print(True) # chaining

print(abs(a - b)) # very low number
if abs(a - b) < 1e-9: print('close enough a = b')

if math.isclose(a, b): print('math close enough a and b are equal')

s1 = 'A'
s2 = "B"
s3 = 'a'
s4 = "b"
if s1 < s2: print('A < B')
if s2 < s3: print('B < a')
if s3 > s4: print('a > b')
elif s3 < s4: print('a < b elif')


def silly(m, x, b):
    y = m * x + b
print(silly(2, 3, 4))

# practice 
def f_to_c(t): return 9/5 * t + 32
def c_to_f(t): return 5/9 * (t - 32)

print(f_to_c(50))
print(c_to_f(50))

def mph_to_kph(s, h): return (s * 1.6) / h

print(mph_to_kph(100, 5))

def mean3a(a, b, c): return (a + b + c) / 3

print(mean3a(2, 4, 6))

def mean3g(a, b, c): return math.pow((a * b * c), 1/3)

print(mean3g(2, 4, 6))

def mean3h(a, b, c): return 3 / (1/a + 1/b + 1/c)

print(mean3h(2, 4, 6))

def dna_conc(m): return m * 50

print(dna_conc(5)) 
print('per ml or whatever')

def between_points(a, b, c, d): return math.sqrt((a - c)**2 + (b - d)**2)
print(between_points(2, 3, 5, 4))

def greatest_3(a, b, c):
    if a >= b >= c: return a
    elif a >= c >= b: return a
    elif c >= a >= b: return c
    elif c >= b >= a: return c
    elif b >= c >= a: return b
    elif b >= a >= c: return b

print(greatest_3(4, 9, 9))

#postive and negative practice

print('''
a = TP
b = FP
c = TN
d = FN''')
def sens(a, b, c, d): return a / (a + d)
def spec(a, b, c, d): return c / (c + b)
def pres(a, b, c, d): return a / (a + b)
def f1sc(a, b, c, d): 
    f1scnum = (pres(a, b, c, d) * sens(a, b, c, d))
    f1scden = (pres(a, b, c, d) + sens(a, b, c, d))
    return 2 * (f1scnum / f1scden)
print(f1sc(1, 2, 3, 4))

# nucleotide practice

def shanuc(a, c, g, t):
    pa = a / (a + c + g + t)
    if pa > 0: pa2 = pa * math.log2(pa)
    else: pa2 = 0
    pc = c / (a + c + g + t)
    if pc > 0: pc2 = pc * math.log2(pc)
    else: pc2 = 0
    pg = g / (a + c + g + t)
    if pg > 0: pg2 = pg * math.log2(pg)
    else: pg2 = 0
    pt = t / (a + c + g + t)
    if pt > 0: pt2 = pt * math.log2(pt)
    else: pt2 = 0
    s = -(pa2 + pc2 + pg2 + pt2)
    return s

print(shanuc(3, 5, 0, 9))