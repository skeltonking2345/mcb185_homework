#34birthday.py

import random
import sys

trials = int(sys.argv[1])
days = int(sys.argv[2])
people = int(sys.argv[3])

success = 0

for i in range(trials):
    calendar = [0] * days
    match = 0
    for b in range(people):
        birthday = random.randint(0, days - 1)
        calendar[birthday] += 1
        if calendar[birthday] == 2:
            match += 1
    if match >= 1: success += 1
        
print(success / trials)