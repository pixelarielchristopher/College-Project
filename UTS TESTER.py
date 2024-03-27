def calculate_hash(data_order, array_length):
    calculated_hash = (data_order - 65) % array_length
    return calculated_hash

def check_name_order(name):
    ordered_name = ord(name[0])
    return ordered_name

def check_name_existence(name, year):
    print("def check name existance")
    name_order = check_name_order(name)
    vertical_index = calculate_hash(name_order, array_dimension)
    vertical_shelve = array_2d[vertical_index]
    print("vertical shelve", vertical_shelve)
    for vertical_shelve_index in range(0, len(vertical_shelve)):  # harus cari cara untuk ngecek 1 1 dari setiap kumpulang data dilist
        vertical_shelve_content = vertical_shelve[vertical_shelve_index]
        if vertical_shelve_content[0] == name and vertical_shelve_content[1] == year:
            return 1
        else:
            print()
    return -1



def add_new_number(array_2d, array_dimension):
    print("Add new number")
    while True:
        try:
            name = str(input("Name           : ")).capitalize()
            year = int(input("Birth of year  : "))
            data_check = check_name_existence(name, year)
            number = int(input("number         : "))
            confirm_data = str(input("\nConfirm input (Yes/No) ? ")).lower()
            if confirm_data == 'yes':
                break
            elif confirm_data == 'no':
                print()
        except ValueError:
            print("Wrong input !", '\n')

    data = [None]*3
    data[0] = name
    data[1] = year
    data[2] = number

    name_order = check_name_order(name)
     # harus buat data check jika nama dan tanggal lahir sama maka output data exist
    vertical_index = calculate_hash(name_order, array_dimension)
    vertical_shelve = array_2d[vertical_index]
    if vertical_shelve[len(vertical_shelve) - 1] == None and data_check == -1:
        print("work")
        for vertical_shelve_index in range(0, len(vertical_shelve)):
            vertical_shelve_content = vertical_shelve[vertical_shelve_index]
            if vertical_shelve_content == None:
                vertical_shelve[vertical_shelve_index] = data
                break

    elif vertical_shelve[len(vertical_shelve) - 1] != None:
        vertical_shelve_extended = [None] * len(vertical_shelve) * 2
        for vertical_shelve_index in range(0, len(vertical_shelve)):
            vertical_shelve_extended[vertical_shelve_index] = vertical_shelve[vertical_shelve_index]
        for vertical_shelve_index in range(len(vertical_shelve), len(vertical_shelve_extended)):
            vertical_shelve_extended_content = vertical_shelve_extended[vertical_shelve_index]
            if vertical_shelve_extended_content == None:
                vertical_shelve_extended[vertical_shelve_index] = data
                break
        array_2d[vertical_index] = vertical_shelve_extended

    else:
        print("data exist cant add anymore")

    return

def search_name(array_2d, array_dimension):
    while True:
        try:
            search_name = str(input("Name           : ")).capitalize()
            year = int(input("Birth of year  : "))
            confirm_data = str(input("\nConfirm input (Yes/No) ? ")).lower()
            if confirm_data == 'yes':
                break
            elif confirm_data == 'no':
                print()
        except ValueError:
            print("Wrong input !", '\n')
    name_order = check_name_order(search_name)
    vertical_index = calculate_hash(name_order, array_dimension)
    vertical_shelve = array_2d[vertical_index]

    for vertical_shelve_index in range(0, len(vertical_shelve)): # harus cari cara untuk ngecek 1 1 dari setiap kumpulang data dilist
        print("vertical shelve in for loop", vertical_shelve)
        vertical_shelve_content = vertical_shelve[vertical_shelve_index]
        print('vertical_shelve[vertical_shelve_index]',vertical_shelve[vertical_shelve_index])
        print("vertical_shelve_content[0]",vertical_shelve_content[0])
        print('vertical_shelve_content[1]',vertical_shelve_content[1])
        if vertical_shelve_content[0] == search_name and vertical_shelve_content[1] == year:
            print(vertical_shelve_content)
            return vertical_shelve_content

    return -1 , search_name, year


if __name__ == '__main__':
    array_2d = [
        [['Aron', 2003, 1234],['Aron', 2004, 123456]], #1  A
        [None], #2  B
        [None], #3  C
        [None], #4  D
        [None], #5  E
        [None], #6  F
        [None], #7  G
        [None], #8  H
        [None], #9  I
        [None], #10 J
        [None], #11 K
        [None], #12 L
        [None], #13 M
        [None], #14 N
        [None], #15 O
        [None], #16 P
        [None], #17 Q
        [None], #18 R
        [None], #19 S
        [None], #20 T
        [None], #21 U
        [None], #22 V
        [None], #23 W
        [None], #24 X
        [None], #25 Y
        [None], #26 Z
    ]
    array_dimension = 26 #26 Alphabet

    while True:
        print('''
1. Add new number
2. Search by name
3. Exit
''')
        try:
            choice = int(input(f"Choise ?       "))
            print()
            if choice == 1:
                added_data = add_new_number(array_2d, array_dimension)
                print("Data added !")
            elif choice == 2:
                search_data, search_name, year = search_name(array_2d, array_dimension)
                if search_data == -1 :
                    print(f"Name           : {search_name}")
                    print(f"Birth of year  : {year}")
                    print(f"number         : Data not found !")

                else:
                    print("Data found !",'\n')
                    print(f"Name           : {search_data[0]}")
                    print(f"Birth of year  : {search_data[1]}")
                    print(f"number         : {search_data[2]}")
            elif choice == 3:
                print("Bye - bye")
                break
        except ValueError:
            print()




