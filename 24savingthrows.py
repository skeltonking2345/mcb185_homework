# 24savingthrows.py

import math
import random 

#1000 trials of saving throws and taking the average, also accounting advantage and disadvantage

trials = 1000
dc5  = 5
dc10 = 10
dc15 = 15
save5  = 0
save10 = 0
save15 = 0
svad5  = 0
svad10 = 0
svad15 = 0
svds5  = 0
svds10 = 0
svds15 = 0
for a in range (trials):
    rollfor5 =  random.randint(1, 20)
    rollfor52 = random.randint(1, 20)
    if rollfor5 >= dc5:
        save5 += 1
    if rollfor5 >= rollfor52: 
        ad5 = rollfor5 
        dis5 = rollfor52
    else:
        ad5 = rollfor52 
        dis5 = rollfor5
    if ad5 >= dc5:
        svad5 += 1
    if dis5 >= dc5:
        svds5 += 1
    rollfor10 = random.randint(1, 20)
    rollfor102 = random.randint(1, 20) 
    if rollfor10 >= dc10:
        save10 += 1
    if rollfor10 >= rollfor102: 
        ad10 = rollfor10 
        dis10 = rollfor102
    else:
        ad10 = rollfor102 
        dis10 = rollfor10
    if ad10 >= dc10:
        svad10 += 1
    if dis10 >= dc10:
        svds10 += 1
    rollfor15 = random.randint(1, 20)
    rollfor152 = random.randint(1, 20)
    if rollfor15 >= dc15:
        save15 += 1
    if rollfor15 >= rollfor152: 
        ad15 = rollfor15 
        dis15 = rollfor152
    else:
        ad15 = rollfor152 
        dis15 = rollfor15
    if ad15 >= dc15:
        svad15 += 1
    if dis15 >= dc15:
        svds15 += 1

dcvalue = '05', '10', '15'
avsucc = (save5 / trials, save10 / trials, save15 / trials)
avscad = (svad5 / trials, svad10 / trials, svad15 / trials)
avscds = (svds5 / trials, svds10 / trials, svds15 / trials)

print('dc', 'succ', ' sucA', ' sucD', sep = ' ')

for i in range(len(dcvalue)):
    print(dcvalue[i], avsucc[i], avscad[i], avscds[i]) 
# final display is follows: dc value, average success d20, average success w/ advantage, average success w/ disadvantage
