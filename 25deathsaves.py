# 25deathsaves.py by skeltonking2345

import math
import random

trials = 1000

success = 0
failure = 0
failEX = 0
revive = 0

for a in range(trials):
    rollforsave = random.randint(1, 20)
    if rollforsave == 20:
        revive += 1
        success += 1
    elif rollforsave == 1:
        failEX += 1
        failure += 2
    elif rollforsave >= 10:
        success += 1
    else: 
        failure += 1

titles = 'success', 'failure', 'failex', 'revive'
chances = (success / trials, failure / trials, failEX / trials, revive / trials)

for i in range(len(titles)):
    print(titles[i], chances[i])
