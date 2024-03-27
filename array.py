def calculate_hash(data, array_length):
    calculated_hash = data % array_length - 1
    return calculated_hash


def add(array_2d, array_dimension):
    data = int(input("Insert number to add : "))
    vertical_index = calculate_hash(data, array_dimension)
    vertical_shelve = array_2d[vertical_index]
    if vertical_shelve[len(vertical_shelve) - 1] == None:
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
    return array_2d

def remove(array_2d, array_dimension):
    while True:
        removedata = int(input("Insert number to remove : "))
        vertical_index = calculate_hash(removedata, array_dimension)
        vertical_shelve = array_2d[vertical_index]
        for vertical_shelve_index in range(0, len(vertical_shelve)):
            vertical_shelve_content = vertical_shelve[vertical_shelve_index]
            if vertical_shelve_content == removedata:
                vertical_shelve[vertical_shelve_index] = None
                break
            else:
                return -1
        return array_2d, removedata

def search(array_2d, array_dimension):
    while True:
        search_data = int(input("Insert number to remove : "))
        vertical_index = calculate_hash(search_data, array_dimension)
        vertical_shelve = array_2d[vertical_index]
        for vertical_shelve_index in range(0, len(vertical_shelve)):
            vertical_shelve_content = vertical_shelve[vertical_shelve_index]
            if vertical_shelve_content == search_data:
                return
            else:
                return -1


if __name__ == '__main__':
    array_2d = [
        [None, None, None],
        [None, None, None],
        [None, None, None]
    ]
    array_dimension = 3
    while True:
        print('''
(1) Add Data
(2) Remove Data
(3) Search Data
            ''')
        print()
        menu = int(input("Please choose a number = "))
        if menu == 1:
            added_data = add(array_2d, array_dimension)
            print()
            print(added_data)
        elif menu == 2:
            removed_data = remove(array_2d, array_dimension)
            print()
            if removed_data == -1:
                print("Data not found")
            else:
                print(removed_data)
        elif menu == 3:
            search_data = search(array_2d, array_dimension)
            print()
            if search_data == -1:
                print("False")
            else:
                print("True")





