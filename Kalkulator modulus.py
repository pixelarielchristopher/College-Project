number = int(input("Number = "))
modulus = int(input("Modulus = "))
result = int(input("Result from modulus = "))

result_i = []
for i in range(10**10):

    if (number * i) % modulus == result % modulus:
        print()
        print(f"{number} x {i} = {result} (mod {modulus})")
        print(f"{(number * i)} % {modulus} = {result} % {modulus}")
        print("\nfound in index", i)
        result_i.append(i)
        break


    else:
        print("not found in in index", i)


print(result_i)