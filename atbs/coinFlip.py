import random
numberOfStreaks = 0
holdit = []
for experimentNumber in range(10000):
    if random.randint(0, 1) == 0:
        holdit.append("H")
    else:
        holdit.append("T")
