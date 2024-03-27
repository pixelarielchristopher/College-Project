def calculate_hash(__data, _array_length):
    calculated_hash = __data % _array_length
    return calculated_hash


# cari vertikal indeks

#  buka array 2d nya

# cari lokasi horizontal

# kembalikan array 2d, data

def get(array2ds, data___, get_array_length):
    vertical_index = calculate_hash(data___, get_array_length)

    horizontal_array = array2ds[vertical_index]
    for index in range(0, array_length):

        if horizontal_array[index] == data___:
            found_data = horizontal_array[index]
            horizontal_array[index] = None

    return (array2ds, found_data)


def search(array2dx, data_x, search_array):
    vertical_index = calculate_hash(data_x, search_array)

    vertical_shelve = array2dx[vertical_index]

    for index in range(0, array_length):

        if vertical_shelve[index] == data_x:
            print("True")
            break
        else:
            print("False")
            break


# if vertical_shelve[index] == data_x:

# print lokasi data_x


# if vertical_shelve[index] == angka yang kita cari

# ambil keluar angka tersebut
def append(_array_2d, _data, _array_length):
    _vertical_index = calculate_hash(_data, _array_length)

    _vertical_shelve = _array_2d[_vertical_index]

    for index in range(0, array_length):

        if _vertical_shelve[index] is None:
            if _data in _vertical_shelve == _data:
                pass
            _vertical_shelve[index] = _data
            print(_vertical_shelve)
            return array_2d
        else:
            print("hash content")
    return _array_2d


def test():
    def should_return_4():
        append(array_2d, 4, array_length)
        print(array_2d)

    return should_return_4()

    def should_return_none():
        append(array_2d, 4, array_length)
        print(array_2d)
        get(array_2d, 4, array_length)
        print(array_2d)

    return should_return_none()




# array kosong, dimasukan data 4 dan get data 4
# array yang berisi 4,



if __name__ == '__main__':
    array_2d = [
        [None, None, None],
        [None, None, None],
        [None, None, None]]
    data = 10
    data = 20
    array_length = len(array_2d)

while True:
    # buat pilihan antara mau input atau get

    inputan = str(input("input/ get/ search: "))
    if inputan == "input":
        input_input = int(input("Input shoe number: "))
        updated_array = append(array_2d, input_input, array_length)
    elif inputan == "get":
        get_get = int(input("Take shoe number: "))
        updated_array, data = get(array_2d, get_get, array_length)
    elif inputan == "search":
        search_search = int(input("Search shoe number: "))
        search(array_2d, search_search, array_length)
    elif inputan == "test":
        test()
    print(array_2d)