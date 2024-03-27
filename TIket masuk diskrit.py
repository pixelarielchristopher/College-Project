n = int(input('n = '))
def funcA(n):
    sum = 0
    for i in range(1, n + 1):
        sum += 1
    return sum

print(funcA(n))

print()

def funcB(n):
    sum = 0
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print("j", j)
            sum += 1
            print("sum",j,  sum)

    return sum

print(funcB(n))
