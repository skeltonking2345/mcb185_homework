# 24savingthrows.py

import math
import random 

#1000 trials of saving throws and taking the average, also accounting advantage and disadvantage

trials = 1000
# earlier rendition of 24savingthrows was much longer and messier, this was done with the help of Dr. Korf
for dc in range(5, 16, 5):
    nor = 0
    dis = 0
    adv = 0
    for i in range(trials):
        r1 = random.randint(1, 20)
        r2 = random.randint(1, 20)
        if r1 >= dc: nor += 1
        if r1 >= dc and r2 >= dc: dis += 1
        if r1 >= dc or r2 >= dc: adv += 1
    print("normal", dc, nor / trials)
    print('advantage', dc, adv / trials)
    print('disadvantage', dc, dis / trials)