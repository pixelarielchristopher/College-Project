'''
nama notelpon umur
sort
'''
def calculate_hash(data, array_length):
    calculated_hash = (data % array_length) - 1
    return calculated_hash


def add(array_2d, array_dimension):

    data = int(input("Insert number to add : "))
    vertical_index = calculate_hash(data, array_dimension)
    print("vertical index = ", vertical_index)
    vertical_shelve = array_2d[vertical_index]
    print("array2d = ", array_2d)
    print("vertical shelve = ", vertical_shelve)

    if vertical_shelve[len(vertical_shelve) - 1] == None:
        for vertical_shelve_index in range(0, len(vertical_shelve)):
            vertical_shelve_content = vertical_shelve[vertical_shelve_index]
            print("vertical shelve content = ", vertical_shelve_content)
            if vertical_shelve_content == None:
                vertical_shelve[vertical_shelve_index] = data
                break
    elif vertical_shelve[len(vertical_shelve) - 1] != None:
        print("work")
        vertical_shelve_extended = [None] * len(vertical_shelve) * 2
        print("vertical shelve extend", vertical_shelve_extended)
        for vertical_shelve_index in range(0, len(vertical_shelve)):
            vertical_shelve_extended[vertical_shelve_index] = vertical_shelve[vertical_shelve_index]
        print("try to append old array", vertical_shelve_extended)
        for vertical_shelve_index in range(len(vertical_shelve), len(vertical_shelve_extended)):
            print("work 2")
            vertical_shelve_extended[vertical_shelve_index] = vertical_shelve_extended[vertical_shelve_index]
            if vertical_shelve_extended[vertical_shelve_index] == None:
                vertical_shelve_extended[vertical_shelve_index] = data
                break
        array_2d[vertical_index] = vertical_shelve_extended
    return array_2d








if __name__ == '__main__':
    array_2d = [
        [None, None, None],
        [None, None, None],
        [None, None, None]
    ]
    data = 10
    array_dimension = 3
    print('''
(1) Add Data
(2) Remove Data
(3) Search Data
    ''')
    while True:
        print()
        menu = int(input("Please choose a number = "))
        if menu == 1:
            added_data = add(array_2d, array_dimension)
            print("\n", added_data)
        elif menu == 2:
            removed_data = remove(array_2d, array_dimension)
            if removed_data == -1:
                print("Data not found")
            else:
                print("\n", removed_data)

        elif menu == 3:
            search_data = search(array_2d, array_dimension)
            if search_data == -1:
                print("False")
            else:
                print("True")
