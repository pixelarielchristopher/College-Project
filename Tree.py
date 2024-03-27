class Node:
   def __init__(self):
      self.left = None
      self.right = None
      self.data = None

   def PrintTree(self):
      print(self.data)

class Tree:
    def __init__(self):
        self.root = None

def visit(node,temp):
    if node == None:
        return temp
    temp.append(node.data)
    visit(node.left, temp)
    visit(node.right, temp)


def from_tree_to_list(root):
    temp = []
    visit(root, temp)
    return temp

def should_return_tree_in_list():
    node_50 = Node()
    node_50.data = 50

    node_30 = Node()
    node_30.data = 30

    node_60 = Node()
    node_60.data = 60

    node_20 = Node()
    node_20.data = 20

    node_60.left = node_50
    node_50.left = node_30
    node_30.left = node_20

    root = node_60
    new_root = normalized_left_left(root)
    temp = from_tree_to_list(new_root)
    print(temp)
    expected_output = [50, 30, 20, 60]
    assert expected_output == temp


def normalized_left_left(old_root):
    new_root = old_root.left
    right_arm = new_root.right
    old_root.left = None
    new_root.right = old_root
    old_root.left = right_arm
    old_root = None
    return new_root

def height(node, temp):
    if node == None:
        return temp
    temp.append(node.data)
    visit(node.left, temp)
    visit(node.right, temp)

if __name__ == "__main__":

    node_50 = Node()
    node_50.data = 50

    node_30 = Node()
    node_30.data = 30

    node_60 = Node()
    node_60.data = 60

    node_60.left = node_50
    node_50.left = node_30

    root = node_60

    root2 = normalized_left_left(root)
    should_return_tree_in_list()

    print(from_tree_to_list(root2))



