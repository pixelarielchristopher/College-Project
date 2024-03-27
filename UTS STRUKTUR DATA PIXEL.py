# MAIN FUNCTION
def hash(data):
    vertical_length = 4
    hash = (ord(data['name'][0]) - 65) % vertical_length
    return hash


def check_duplicates(telephoneBook_array, data):
    vertical_index = hash(data)
    array_inside = telephoneBook_array[vertical_index]

    for i in range(len(array_inside)):
        if array_inside[i] != None:
            if array_inside[i]["name"] == data['name']:
                if array_inside[i]["yob"] == data['yob']:
                    return False
    return True


def append(telephoneBook_array, data):
    vertical_index = hash(data)
    array_inside = telephoneBook_array[vertical_index]

    for i in range(len(array_inside)):
        if array_inside[i] == None:
            array_inside[i] = data
            break
    return telephoneBook_array


def search(telephoneBook_array, data):
    vertical_index = hash(data)
    array_inside = telephoneBook_array[vertical_index]

    for i in range(len(array_inside)):
        if array_inside[i] != None:
            if data['name'] == array_inside[i]["name"]:
                if data['yob'] == array_inside[i]["yob"]:
                    data["phone_no"] = array_inside[i]["phone_no"]
                    return (vertical_index, i), data["phone_no"]
    return (vertical_index, None), '\033[1;31mNot Found!\033[0;0m'


def resize(array_inside, newSize_array):
    newArray_inside = [None] * newSize_array
    for i in range(len(array_inside)):
        newArray_inside[i] = array_inside[i]
    return newArray_inside


def is_full(telephoneBook_array, data):
    vertical_index = hash(data)
    array_inside = telephoneBook_array[vertical_index]
    horizontal_length = len(array_inside)
    newSize_array = horizontal_length * 2

    for i in range(len(array_inside)):
        if array_inside[-1] != None:
            newArray_inside = resize(array_inside, newSize_array)
            telephoneBook_array[vertical_index] = newArray_inside
            return (vertical_index, True)
        else:
            return (vertical_index, False)


##### END
# ^^^
# TEST FUNCTION
def should_return_same_hash():
    data1 = {}
    data1['name'] = 'Andre'

    data2 = {}
    data2['name'] = 'Andi'

    expected_output = 0
    output1 = hash(data1)
    output2 = hash(data2)

    assert output1 == output2, f"Expected {expected_output} and got {output2}."


def should_return_different_hash():
    data1 = {}
    data1['name'] = 'Andre'

    data2 = {}
    data2['name'] = 'Ben'

    output1 = hash(data1)
    output2 = hash(data2)

    assert output1 != output2, f"Expected hash_1: {output1} is different with hash_2: {output2}."


def should_add_new_data():
    temporaryArray = [[None for i in range(4)] for j in range(4)]

    data = {}
    data['name'] = 'Aaron'
    data['yob'] = '2003'
    data['phone_no'] = '08123456789'
    expected_data = [[{
        'name': 'Aaron',
        'yob': '2003',
        'phone_no': '08123456789'
    }, None, None, None], [None, None, None, None], [None, None, None, None],
                     [None, None, None, None]]

    temporaryArray = append(temporaryArray, data)

    assert expected_data == temporaryArray, f"fExpected {expected_data} and got {temporaryArray}."


def should_add_new_data_and_resize():
    temporaryArray = [['Content' for i in range(4)] for j in range(4)]

    data = {}
    data['name'] = 'Aaron'
    data['yob'] = '2003'
    data['phone_no'] = '08123456789'

    expected_data = [[
        'Content', 'Content', 'Content', 'Content', {
            'name': 'Aaron',
            'yob': '2003',
            'phone_no': '08123456789'
        }, None, None, None
    ], ['Content', 'Content', 'Content', 'Content'],
                     ['Content', 'Content', 'Content', 'Content'],
                     ['Content', 'Content', 'Content', 'Content']]

    is_full(temporaryArray, data)
    temporaryArray = append(temporaryArray, data)

    assert expected_data == temporaryArray, f"Expected {expected_data} and got {temporaryArray}."


def should_return_data_with_v_and_h_index():
    temporaryArray = [[None, None, None, None], [None, None, None, None],
                      [{
                          'name': 'Chris',
                          'yob': '2003',
                          'phone_no': '08123456789'
                      }, None, None, None], [None, None, None, None]]

    data = {'name': 'Chris', 'yob': '2003'}
    expected_v = 2
    expected_h = 0
    expected_phone_no_taken = '08123456789'

    ((v, h), phone_no_taken) = search(temporaryArray, data)

    assert ((expected_v, expected_h), expected_phone_no_taken) == (
        (v, h), phone_no_taken
    ), f"Expected Phone Number: {expected_phone_no_taken} in Vertical Index: {expected_v}, Horizontal Index: {expected_h} and got {phone_no_taken} in Vertical Index: {v}, Horizontal Index: {h}."


def should_not_return_data():
    temporaryArray = [[None, None, None, None], [None, None, None, None],
                      [None, None, None, None], [None, None, None, None]]

    data = {'name': 'Brandon', 'yob': '2003'}
    expected_v = 1
    expected_h = None
    expected_phone_no_taken = '\033[1;31mNot Found!\033[0;0m'

    ((v, h), phone_no_taken) = search(temporaryArray, data)

    assert ((expected_v, expected_h), expected_phone_no_taken) == (
        (v, h), phone_no_taken
    ), f"Expected Phone Number: {expected_phone_no_taken} in Vertical Index: {expected_v}, Horizontal Index: {expected_h} and got {phone_no_taken} in Vertical Index: {v}, Horizontal Index: {h}."


def should_get_new_horizontal_array_with_new_length_2times_after_insert():
    temporaryArray = [['Content' for i in range(4)] for j in range(4)]

    data = {}
    data['name'] = 'Aaron'
    data['yob'] = '2003'
    data['phone_no'] = '08123456789'

    expected_data = [[
        'Content', 'Content', 'Content', 'Content', {
            'name': 'Aaron',
            'yob': '2003',
            'phone_no': '08123456789'
        }, None, None, None
    ], ['Content', 'Content', 'Content', 'Content'],
                     ['Content', 'Content', 'Content', 'Content'],
                     ['Content', 'Content', 'Content', 'Content']]

    is_full(temporaryArray, data)
    temporaryArray = append(temporaryArray, data)

    assert expected_data[0] == temporaryArray[
        0], f"Expected {expected_data[0]} and got {temporaryArray[0]}."


def after_insert_should_return_telephoneBook_array_with_the_same_length_like_before_insert(
):
    temporaryArray = [[{
        'name': 'Agung',
        'yob': '2003',
        'phone_no': '08123456789'
    }, {
        'name': 'Agung',
        'yob': '2003',
        'phone_no': '08123456789'
    }, {
        'name': 'Agung',
        'yob': '2003',
        'phone_no': '08123456789'
    }, None], [None, None, None, None], [None, None, None, None],
                      [None, None, None, None]]

    data = {}
    data['name'] = 'Abigail'
    data['yob'] = '2003'
    data['phone_no'] = '08911111111'

    expected_data = [[{
        'name': 'Agung',
        'yob': '2003',
        'phone_no': '08123456789'
    }, {
        'name': 'Agung',
        'yob': '2003',
        'phone_no': '08123456789'
    }, {
        'name': 'Agung',
        'yob': '2003',
        'phone_no': '08123456789'
    }, {
        'name': 'Abigail',
        'yob': '2003',
        'phone_no': '08911111111'
    }], [None, None, None, None], [None, None, None, None],
                     [None, None, None, None]]

    is_full(temporaryArray, data)
    temporaryArray = append(temporaryArray, data)

    assert expected_data == temporaryArray, f"Expected {expected_data} and got {temporaryArray}."


def should_return_true_when_array_is_full():
    temporaryArray = [['Content' for i in range(4)] for j in range(4)]

    data = {}
    data['name'] = 'Aaron'
    data['yob'] = '2003'
    data['phone_no'] = '08123456789'

    expected_condition = True

    (v, condition) = is_full(temporaryArray, data)

    assert expected_condition == condition, f"Expected {expected_condition} and got {condition}."


def should_return_false_when_array_is_not_full():
    temporaryArray = [[None for i in range(4)] for j in range(4)]

    data = {}
    data['name'] = 'Aaron'
    data['yob'] = '2003'
    data['phone_no'] = '08123456789'

    expected_condition = False

    (v, condition) = is_full(temporaryArray, data)

    assert expected_condition == condition, f"Expected {expected_condition} and got {condition}."


##### END


def test():
    should_return_same_hash()
    should_return_different_hash()
    should_add_new_data()
    should_add_new_data_and_resize()
    should_return_data_with_v_and_h_index()
    should_not_return_data()
    should_get_new_horizontal_array_with_new_length_2times_after_insert()
    after_insert_should_return_telephoneBook_array_with_the_same_length_like_before_insert(
    )
    should_return_true_when_array_is_full()
    should_return_false_when_array_is_not_full()


#^^^
def main():
    telephoneBook_array = [[None for i in range(4)] for j in range(4)]
    while True:
        print("\n------------------")
        choise = input(
            " Mein Telefonbuch\n\n 1. Add new number\n 2. Search by name\n 3. Exit\n\n Choise? \t"
        ).replace(" ", "")
        print("------------------")
        if choise == '1':
            while True:
                data = {}
                print("\n------------------\nAdd new data\n")
                data['name'] = input("Name          : ").title()
                data['yob'] = input("Year of Birth : ")
                if len(data['name']) != 0 and len(
                        data['yob']) != 0 and data['yob'].isdigit():
                    check = check_duplicates(telephoneBook_array, data)
                    if check == True:
                        data['phone_no'] = input("Phone Number  : ")
                        if len(data['phone_no']
                               ) != 0 and data['phone_no'].isdigit():
                            (v, condition) = is_full(telephoneBook_array, data)
                            telephoneBook_array = append(
                                telephoneBook_array, data)
                            break
                        else:
                            print(
                                "\n\033[1;31mSome attribute missing/\nmistakenly written!\033[0;0m"
                            )
                    if check == False:
                        print(
                            "Phone Number  : \033[1;31mData Already Exists!\033[0;0m"
                        )
                        print("------------------")
                        break
                else:
                    data['phone_no'] = input("Phone Number  : ")
                    if len(data['name']) == 0 and len(
                            data['yob']) == 0 and len(data['phone_no']) == 0:
                        break
                    print(
                        "\n\033[1;31mSome attribute missing/\nmistakenly written!\033[0;0m"
                    )
        elif choise == '2':
            while True:
                data = {}
                print("\n------------------\nSearch by name\n")
                data['name'] = input("Name          : ").title()
                data['yob'] = (input("Year of Birth : "))
                if len(data['name']) != 0 and len(
                        data['yob']) != 0 and data['yob'].isdigit():
                    ((v, h), data) = search(telephoneBook_array, data)
                    print(f"Phone Number  : {data}")
                    print("------------------")
                    break
                elif len(data['name']) == 0 and len(data['yob']) == 0:
                    break
                else:
                    print(
                        "\n\n\033[1;31mSome attribute missing/\nmistakenly written!\033[0;0m"
                    )
        elif choise == '3':
            print("\n\033[1;32m--------------------------------------")
            print("Tschüss! bis wir uns wieder treffen...")
            print("--------------------------------------\n\033[0;0m")
            break
        else:
            print("\033[1;31m Invalid input...\n Please try again! \033[0;0m")


# MAIN PROGRAM
if __name__ == '__main__':
    test()
    main()
