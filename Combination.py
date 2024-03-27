from itertools import combinations

comb = combinations([16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96],[40, 48, 56, 64, 72, 80, 88, 96],[32, 36, 40, 44, 48, 52, 56, 60, 64, 68, 72, 76, 80, 84, 88, 92, 96, 100])

for i in list(comb):
    x = sum(i)
    n = 0
    print(i)
    if x == 100:
        n +=1



