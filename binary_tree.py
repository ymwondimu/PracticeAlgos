class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.value)



class Tree:
    def __init__(self):
        self.root = None

    """def __init__(self, node):
        self.root = node"""

    def insert(self, node):
        self.insert_at_node(self.root, node)

    def insert_at_node(self, root, node):
        if root is None:
            self.root = node
        else:
            if node.value < root.value:
                if root.left is None:
                    root.left = node
                else:
                    self.insert_at_node(root.left, node)
            else:
                if root.right is None:
                    root.right = node
                else:
                    self.insert_at_node(root.right, node)


def main():
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n5 = Node(5)
    n6 = Node(6)

    t = Tree()
    t.insert(n4)
    t.insert(n6)
    t.insert(n5)
    t.insert(n2)
    t.insert(n3)
    t.insert(n1)

    in_order(t.root)

def in_order(root):
    if root == None:
        return None
    else:
        in_order(root.left)
        print (root.value)
        in_order(root.right)



if __name__ == "__main__":
    main()

