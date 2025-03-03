# 25deathsaves.py by skeltonking2345

import math
import random

trials = 1000


stable = 0
death = 0
revive = 0

for a in range(trials):
    success = 0
    failure = 0
    insta_revive = False
    #in trials, which happens, insta-revive, stable, die
    while success < 3 and failure < 3 and not insta_revive:
        roll = random.randint(1, 20)
        if roll == 20: insta_revive = True
        elif roll == 1: failure += 2
        elif roll < 10: failure += 1
        else: success += 1
    if insta_revive: revive += 1
    elif failure >= 3: death += 1
    else: stable += 1

print('stables', stable / trials,)
print('deaths', death / trials)
print('revive', revive / trials)



