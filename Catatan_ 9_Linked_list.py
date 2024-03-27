import time
#problem append when no data
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0


class Node:
    def __init__(self):
        self.data = None
        self.next = None
        self.prev = None


def len(linked_list):
    n = 0
    current = linked_list.head
    while True:
        if current != None:
            current = current.next
            n += 1
        else:
            break
    return n


# bikin fungsi print linked list

def print_linked_list(linked_list):
    current = linked_list.head
    while True:
        if current != None:
            print(current.data, end=" -> ")
            current = current.next
        else:
            print(None, end="\n\n")
            break


def insert_data(linked_list, data, position):
    current2 = Node()
    current2.data = data
    current = linked_list.head
    n = len(linked_list)

    if n == 0:
        linked_list.head = current2
        print_linked_list(linked_list)
        
    for i in range(n):
        if i == position and position == 0:
            linked_list.head = current2
            current2.next = current
            break
        elif i == position - 1:
            next_data = current.next  # current.next awal
            current.next = current2
            current2.next = next_data
        else:
            current = current.next

    print_linked_list(linked_list)


def append_data(linked_list, data):
    current = linked_list.head
    current2 = Node()
    current2.data = data
    while True:
        if current == None:
            linked_list.head = current2
            break
        elif current.next == None:
            current.next = current2
            current = None
            #linked_list.size += 1
            break

    print_linked_list(linked_list)

def append_data_tail(linked_list, data):
    current = linked_list.head
    current2 = Node()
    current2.data = data
    while True:
        if current == None:
            linked_list.head = current2
            break
        elif current.next == None:
            current.next = current2
            current = None
            #linked_list.size += 1
            break
    print_linked_list(linked_list)


def pop_data(linked_list, position):
    current = linked_list.head
    current2 = linked_list.head
    n = len(linked_list)
    if n == 0:
        print("Can't pop anymore, there is no data !")
        return
    for i in range(n):
        if position == 0 and i == 0:
            linked_list.head = current.next
            current.next = linked_list.head
            current = None
            break

        elif i == position - 1:
            next_data = current.next
            first_data = current
            current.next = current2
            current2.next = None
            first_data.next = next_data
            break

        else:
            current = current.next
            current2 = current2.next

    print_linked_list(linked_list)

def find_data(linked_list, data):
    current = linked_list.head
    n = len(linked_list)
    for i in range(n):
        if current != None:
            if current.data == data:
                return i
        else:
            current = current.next

    return -1

def to_list(linked_list):
    current = linked_list.head
    list = []
    while True:
        if current != None:
            list.append(current.data)
            current = current.next
        else:
            break
    
    return list

if __name__ == '__main__':

    linked_list = LinkedList()


    while True:
        time.sleep(1)
        choice = int(input('''
Choice :
(1) Print Linked List 
(2) Insert Data 
(3) Append Data
(4) Append Data From Tail
(5) Pop Data
(6) Find Data
(7) Linked List Length 
(8) Linked List to List
---------------------> '''))
        print()
        if choice == 1:
            print_linked_list(linked_list)
        elif choice == 2:
            data = int(input("data : "))
            position = int(input("Position for data : "))
            insert_data(linked_list, data, position)
        elif choice == 3:
            data = int(input("data : "))
            append_data(linked_list, data)
        elif choice == 4:
            data = int(input("data : "))
            append_data_tail(linked_list, data)
        elif choice == 5:
            position = int(input("Position : "))
            pop_data(linked_list, position)
        elif choice == 6:
            data = int(input("data to find : "))
            i = find_data(linked_list, data)
            if i == -1:
                print("Data does not exist")
            else:
                print(f"Data ({data}) found at index {i}")
        elif choice == 7:
            print()
            print_linked_list(linked_list)
            print(f"Linked List Length : {len(linked_list)}")
        elif choice == 8:
            print(to_list(linked_list))




#queue menggunakan linked list = first in first out (FIFO)
