import random
import sys

trials = int(sys.argv[1])
days = int(sys.argv[2])
people = int(sys.argv[3])

success = 0

for i in range(trials):
    birthdays = []
    for i in range(people):
        day = random.randint(1, days)
        birthdays.append(day)
    match = 0
    for p1 in range(people):
        for p2 in range(p1 + 1, people):
            if birthdays[p1] == birthdays[p2]:
                match += 1
    if match >= 1:
        success +=1
print(success / trials)
