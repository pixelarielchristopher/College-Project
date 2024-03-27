class _tree:
    def __init__(self):
        self.root = None


class Node:
    def __init__(self):
        self.data = None
        self.left = None
        self.right = None


def get_height(node):
    if node == None:
        return 0
    else:
        return 1 + max(get_height(node.left), get_height(node.right))


def get_balance_factor(node):
    if node == None:
        return 0
    else:
        return get_height(node.left) - get_height(node.right)


# DEPTH SEARCH FIRST
def visit_dsf(node, temp):
    if node == None:
        return
    temp.append(node.data)
    visit_dsf(node.left, temp)
    visit_dsf(node.right, temp)


def tree_to_list_dsf(root):
    temp = []
    visit_dsf(root, temp)
    return temp


# BREADTH SEARCH FIRST
def visit(node, data, queue):
    data.append(node.data)
    if node.left != None:
        queue.append(node.left)
    if node.right != None:
        queue.append(node.right)
    if len(queue) >= 1:
        to_visit = queue[0]
        queue.pop(0)
        visit(to_visit, data, queue)
    return


def tree_to_list_bsf(root):
    queue = []
    data = []
    visit(root, data, queue)
    return data


def find(data):
    list_of_data = tree_to_list_bsf(tree.root)
    if data in list_of_data:
        return True
    else:
        return False


def normalize_right_right(old_root):
    new_root = old_root.right
    orphan = new_root.left
    old_root.right = None
    new_root.left = old_root
    old_root.right = orphan
    old_root = None
    return new_root


def normalize_left_left(old_root):
    new_root = old_root.left
    orphan = new_root.right
    old_root.left = None
    new_root.right = old_root
    old_root.left = orphan
    old_root = None
    return new_root


def normalize_left_right(old_root):
    left_arm = old_root.left
    pivot = left_arm.right
    orphan = pivot.left
    left_arm.right = None
    old_root.left = pivot
    pivot.left = left_arm
    if orphan != None:
        pivot.right = orphan
    return normalize_left_left(old_root)


def normalize_right_left(old_root):
    right_arm = old_root.right
    pivot = right_arm.left
    orphan = pivot.right
    right_arm.left = None
    old_root.right = pivot
    pivot.right = right_arm
    if orphan != None:
        pivot.left = orphan
    return normalize_right_right(old_root)


def rebalance(node):
    balance_factor = get_balance_factor(node)
    if abs(balance_factor) <= 1:
        return node
    elif balance_factor == 2:
        if get_balance_factor(node.left) >= 1:
            return normalize_left_left(node)
        else:
            return normalize_left_right(node)
    elif balance_factor == -2:
        if get_balance_factor(node.right) <= -1:
            return normalize_right_right(node)
        else:
            return normalize_right_left(node)


def append(root, node):
    if root == None:
        root = node
        return root
    elif node.data < root.data:
        root.left = append(root.left, node)
    else:
        root.right = append(root.right, node)
    return rebalance(root)


def should_trigger_single_rotation():
    tree = _tree()


def should_trigger_double_rotation():
    tree = _tree()


def should_not_trigger_any_rotation():
    tree = _tree()
    node_1 = Node()
    node_1.data = 40
    tree.root = append(tree.root, node_1)
    node_2 = Node()
    node_2.data = 35
    tree.root = append(tree.root, node_2)
    node_3 = Node()
    node_3.data = 45
    tree.root = append(tree.root, node_3)

    # [40, 35, 45] -> [40, 35, 45]
    expected_output = [40, 35, 45]
    output = tree_to_list_bsf(tree.root)

    assert expected_output == output, f"Expected {expected_output} and got {output}."


def should_return_list_with_breadth_first_search():
    tree = _tree()
    node_1 = Node()
    node_1.data = 40
    tree.root = append(tree.root, node_1)
    node_2 = Node()
    node_2.data = 35
    tree.root = append(tree.root, node_2)
    node_3 = Node()
    node_3.data = 50
    tree.root = append(tree.root, node_3)
    node_4 = Node()
    node_4.data = 30
    tree.root = append(tree.root, node_4)
    node_5 = Node()
    node_5.data = 36
    tree.root = append(tree.root, node_5)
    node_6 = Node()
    node_6.data = 38
    tree.root = append(tree.root, node_6)

    expected_output = [36, 35, 40, 30, 38, 50]
    output = tree_to_list_bsf(tree.root)

    assert expected_output == output, f"Expected {expected_output} and got {output}."


def test():
    should_trigger_single_rotation()
    should_trigger_double_rotation()
    should_not_trigger_any_rotation()
    should_return_list_with_breadth_first_search()


def main():
    global tree
    tree = _tree()
    while True:
        print()
        choice = input("AVL Tree\n\n 1. Insert\n 2. Find\n\n Choice? \t").replace(" ", "")
        if choice == '1':
            # INPUT
            data = int(input("Input number: "))
            # NEW NODE
            node = Node()
            node.data = data
            # APPEND
            if tree.root == None:
                tree.root = append(tree.root, node)
                print(tree_to_list_bsf(tree.root))
            else:
                tree.root = append(tree.root, node)
                print('root ->', tree.root.data)
                print(tree_to_list_bsf(tree.root))
        elif choice == '2':
            # SEARCH
            data = int(input("Input number to find: "))
            condition = find(data)
            print(condition)
        else:
            print("Invalid input...\n Please try again!")


if __name__ == '__main__':
    test()
    main()

