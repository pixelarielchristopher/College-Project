'''
kelebihan list mampu menyimpan data walaupun letaknya berantakan
namun 1 data memerlukan 2 tempat yakni tempat asal dan tujuan alamat

current awal menunjuk data yang ditunjuk oleh head

untuk menghilangkan data tanpa data leak kita harus memguat sebuah data menunjuk none

current.next == panah

Class User:
    def __init__(self):
        self.name = None
        self.age = None


'''

'''
class User:
    def __init__(self):
        self.name = None
        self.age = None

if __name__ == '__main__':
    andy = {
        "name" : "andi",
        "age" : 17,
    }
    
    pixel = {
        "name" : "Pixel",
        "age" : 18
    }
    andy = User()
    andy.name = "Andy"
    andy.age = 17
    pixel = User()
    pixel.name =

    print(f"{andy.name}, {andy.age}")
    
'''

class LinkedList:
    def __init__(self):
        self.head = None
            
class Node:
    def __init__(self):
        self.data = None
        self.next = None
        
#bikin fungsi print linked list

def print_linked_list(linked_list):
    current = linked_list.head
    while True:
        if current != None:
            print(current.data, end=" -> ")
            current = current.next
        else:
            print(None , end="\n\n")
            break


def append_data(linked_list):
    index = int(input("want to put data where ? "))
    data = int(input("data : "))
    current = linked_list.head
    current2 = linked_list.head
    n = 4
    while True:
        for i in range (n+1):
            if current != None:
                current = current.next
                if i == index:
                    current2.next = None
                    current2.data = data
                    current2.next = current
                    current2 = None
            else:
                break

        print_linked_list(linked_list)








if __name__ == '__main__':
    node_4 = Node()
    node_4.data = 16

    node_3 = Node()
    node_3.data = 9

    node_2 = Node()
    node_2.data = 4

    node_1 = Node()
    node_1.data = 1

    node_1.next = node_2
    node_2.next = node_3
    node_3.next = node_4

    linked_list = LinkedList()
    linked_list.head = node_1

    while True:
        choice = int(input('Choice (1) Print Linked List (2) Append -> '))
        if choice == 1:
            print_linked_list(linked_list)
        elif choice == 2:
            append_data(linked_list)
    
    



