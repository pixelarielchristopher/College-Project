h = int(input("Total Hobbies = "))
if h != 0:
    for i in range(h):
        hobby = input(f"Hobby {i+1} = ")

elif h == 0:
    print("Please a find a new hobby!")

else:
    print("Please input a correct number!")

