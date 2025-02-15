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

a = 2
b = 2
if a == b:
    print('a equals b')
if a != b:
    print('its all fucked up') # if conditionals

def is_even(x):
    if x % 2 ==0: return True
    return False
print(is_even(2))
print(is_even(3)) # conditional practice

c = a == b
print(c)
print(type(c))