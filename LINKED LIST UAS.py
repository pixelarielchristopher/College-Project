##################################### PROGRAM CLASSES & FUNCTIONS #####################################
class linkedList:
   def __init__(self):
      self.head = None
      self.tail = None

class Node:
   def __init__(self):
      self.data = None
      self.priority = None
      self.next = None
      self.prev = None

def print_ll(linked_list):
   output = []
   current = linked_list.head
   while current.next != None:
      output.append(f"{current.data}({current.priority})")
      current = current.next
   output.append(f"{current.data}({current.priority})")
   return output

def append(node):
   front = linked_list.head
   back = linked_list.tail
   if front == None:
      front = node
      front.next = None
      linked_list.head = node
      linked_list.tail = node
      front = None
      back = None
   else:
      if node.priority < front.priority:
         node.next = front
         front.prev = node
         linked_list.head = node
         front = None
         back = None
      elif node.priority >= back.priority:
         node.prev = back
         node.next = None
         back.next = node
         linked_list.tail = node
         front = None
         back = None
      else:
         current = linked_list.head
         while current.next.priority != None:
            if node.priority < current.next.priority:
               before = current
               after = current.next
               before.next = node
               node.next = after
               after.prev = node
               node.prev = before
               current = None
               before = None
               after = None
               break
            current = current.next

def pop():
   current = linked_list.head
   if current == None:
      print("None")
   elif current.next != None:
      after = current.next
      linked_list.head = after
      after.prev = None
      current.next = None
      current = None
      after = None
      output = print_ll(linked_list)
      print(output)
   else:
      linked_list.head = None
      current = None
      print("None")
########################################### END ###########################################


##################################### TEST FUNCTIONS #####################################
def should_append_at_the_first_based_on_priority():
   global linked_list
   linked_list = linkedList()
   node_1 = Node()
   node_1.data = 'Jeremy'
   node_1.priority = 3
   append(node_1)

   node_2 = Node()
   node_2.data = 'Andre'
   node_2.priority = 1

   expected_output = ['Andre(1)', 'Jeremy(3)']
   append(node_2)
   output = print_ll(linked_list)

   assert expected_output == output, f"Expected {expected_output} and got {output}."

def should_append_at_the_middle_based_on_priority():
   global linked_list
   linked_list = linkedList()
   node_1 = Node()
   node_1.data = 'Jeremy'
   node_1.priority = 3
   append(node_1)

   node_2 = Node()
   node_2.data = 'Andre'
   node_2.priority = 1
   append(node_2)

   node_3 = Node()
   node_3.data = 'Brandon'
   node_3.priority = 2

   expected_output = ['Andre(1)', 'Brandon(2)', 'Jeremy(3)']
   append(node_3)
   output = print_ll(linked_list)

   assert expected_output == output, f"Expected {expected_output} and got {output}."

def should_append_at_the_last_based_on_priority():
   global linked_list
   linked_list = linkedList()
   node_1 = Node()
   node_1.data = 'Andre'
   node_1.priority = 1
   append(node_1)

   node_2 = Node()
   node_2.data = 'Jeremy'
   node_2.priority = 4

   expected_output = ['Andre(1)', 'Jeremy(4)']
   append(node_2)
   output = print_ll(linked_list)

   assert expected_output == output, f"Expected {expected_output} and got {output}."
########################################### END ###########################################


def test():
   should_append_at_the_first_based_on_priority()
   should_append_at_the_middle_based_on_priority()
   should_append_at_the_last_based_on_priority()

def main():
   global linked_list
   linked_list = linkedList()
   linked_list.head = None
   linked_list.tail = None

   while True:
      print()
      choice = input("EinGetroffen Krankenhaus\n\n 1. Insert\n 2. Remove\n\n Choice? \t").replace(" ","")
      print()
      if choice == '1':
         # INPUT
         name = input("Input name: ").title()
         while True:
            try:
               priority = int(input("Input priority: "))
               break
            except ValueError:
               print()
               print("Invalid input...\nPlease try again!\n")
         # NEW NODE
         node = Node()
         node.data = name
         node.priority = priority
         # APPEND
         append(node)
         print()
         print(print_ll(linked_list))
      elif choice == '2':
         # POP
         pop()
      else:
         print()
         print("Invalid input...\nPlease try again!")


########################################### MAIN ###########################################
if __name__ == '__main__':
   test()
   main()