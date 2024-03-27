#input
birth = int(input("Your Birth Year : "))
yearsnow = int(input("Years now : "))

#process
if (birth>1940 and birth<2023):
    years = yearsnow - birth
    bar = years //10
    #output
    print(years)
    for i in range(bar):
        print("*",end=" ")
    print()

    if years < 17:
        print("You can't have a driving license!")
    else:
        print("you can have a driving license")
else:
    print("Wrong input")

