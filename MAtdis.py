def dec2bin(n):
    if n > 0:
        print("work1")
        return dec2bin(n//2) + str(n%2)
    print("work2")
    return""

while True:
    n = int(input("n = "))
    print("result from return", dec2bin(n))