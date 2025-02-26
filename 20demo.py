# 20demo.py by skeltonking2345

import math
import random

t = 1, 2
print(t)
print(type(t))

person = 'Steve', 21, 57891.50
print(person)

def midpoint(x1, y1, x2, y2):
    x = (x1 + x2) / 2
    y = (y1 + y2) / 2
    z = x1 + x2 + y1 + y2
    return x, y, z

print(midpoint(1, 2, 3, 4))

m = midpoint(1, 2, 3, 4)
mx, my, mz= midpoint(1, 2, 3, 4)
print(mx, my, mz)
print(m[0], m[1], m[2])

i = 0
while i < 50:
    print(i)
    i = i + 5
    print('final value of i is', i)

for b in range(0, 5):
    print (b)

for i in range(5):
    print(i)

for i in range(10, -4, -1): print(i)

basket = 'milk', 'eggs', 'bread'
for things in basket: print(things)
print(basket)

for i in range(len(basket)):
    print(i, basket[i])

for i in range(7):
    if i % 2 == 0: print(i, 'is even')
    else:          print(i, 'is odd')

for i in range (1, 101):
    if (i % 5 == 0) and (i % 3 == 0): print('fizzbuzz')
    elif i % 3 == 0:   print('fizz')
    elif i % 5 == 0: print('buzz')
    else: print(i)
    
# triangular number calc
def triangular(a):
    c = 0
    for i in range(a + 1):
        c = c + i
    return c
print(triangular(9))

def factorial(a):
    if a == 0: return 1
    ftk = 1
    for i in range(1, a + 1):
        ftk = ftk * i
    return ftk
print(factorial(5))

def poisson(n, k):
    ftk = 1
    for i in range(1, k + 1):
        ftk = ftk * i
    poi = (((n ** k) * (math.e ** -n)) / ftk)
    return poi
print(poisson(5, 8))

def choose(n, k):
    if k > n: return 'dont do that'
    ftn = 1
    for i in range(1, n + 1):
        ftn = ftn * i
    ftk = 1
    for i in range(1, k + 1):
        ftk = ftk * i
    ftnk = 1
    for i in range(1, (n-k) + 1):
        ftnk = ftnk * i
    chu = ftn / (ftk * ftnk)
    return chu
print(choose(9, 7))
print(choose(9, 9))
print(choose(6, 9))

# i am stupid why did i just not use the factorial function

def inter(a):
    eul = 0
    for i in range (a + 1):
        eul = eul + 1 / factorial(i)
    return eul
print(inter(8))

def isprime(a):
    for i in range (2, round(math.sqrt(a))):
        if a % i == 0: return False
        else: return True
print(isprime(31))
print(isprime(8))
def pie(a):
    p = 3
    for i in range (1, a + 1):
        pi = 2 * i
        pi2 = pi * (pi + 1) * (pi + 2)
        if i % 2 == 0: p = p - 4 / pi2
        else: p = p + 4 / pi2
    return p
print(pie(9))

for i in range(5):
    print(random.random())

for i in range(5):
    print(random.randint(1, 6))

random.seed(1)
print(random.random())
print(random.random())
random.seed(2)
print(random.random())
print(random.random())
random.seed(1)
print(random.random())
print(random.random())

i = 0
t = 0
while i <2 :
    d = math.sqrt((random.random() ** 2) + (random.random() ** 2))
    
    if d < 1:
        i += 1
    t += 1
    paigh = 4 * i/t
    
def averstat3d6(a):
    stat = 0
    for i in range(a):
        stat += random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6)
    av = stat / a
    return av
print(averstat3d6(600))

def averstat3d6r1(a):
    stat = 0
    for i in range(a):
        roll1 = random.randint(1, 6)
        if roll1 == 1:
            roll1 = random.randint(1, 6)
            while roll1 == 1:
                roll1 = random.randint(1, 6)
        roll2 = random.randint(1, 6)
        if roll2 == 1:
            roll2 = random.randint(1, 6)
            while roll2 == 1:
                roll2 = random.randint(1, 6)
        roll3 = random.randint(1, 6)
        if roll3 == 1:
            roll3 = random.randint(1, 6)
            while roll3 == 1:
                roll3 = random.randint(1, 6)
        stat += roll1 + roll2 + roll3
    av = stat / a
    return av
print(averstat3d6r1(700))

def averstat3d6x2(a):
    stat = 0
    for i in range(a):
        roll1a = random.randint(1, 6)
        roll1b = random.randint(1, 6)
        if roll1a >= roll1b:
            true1 = roll1a
        else: true1 = roll1b
        roll2a = random.randint(1, 6)
        roll2b = random.randint(1, 6)
        if roll2a >= roll2b:
            true2 = roll2a
        else: true2 = roll2b
        roll3a = random.randint(1, 6)
        roll3b = random.randint(1, 6)
        if roll3a >= roll3b:
            true3 = roll3a
        else: true3 = roll3b
        stat += true1 + true2 + true3
    av = stat / a
    return av
print(averstat3d6x2(600))

def averstat4d6d1(a):
    stat = 0
    for i in range(a):
        r1 = random.randint(1, 6)
        r2 = random.randint(1, 6)
        r3 = random.randint(1, 6)
        r4 = random.randint(1, 6)
        if r1 <= r2 and r1 <= r3 and r1 <= r4:
            stat += r2 + r3 + r4
        elif r2 <= r1 and r2 <= r3 and r2 <= r4:
            stat += r1 + r3 + r4
        elif r3 <= r1 and r3 <= r2 and r3 <= r4:
            stat += r1 + r2 + r4
        else: stat += r1 + r2 + r3
    av = stat / a
    return av
print(averstat4d6d1(600))