import sys


class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
        
    def __repr__(self):
        return f'Node({self.data}, {repr(self.left)}, {repr(self.right)})'
    
class BSTree:
    def __init__(self, root=None):
        self.root = root
        
    def __repr__(self):
        return f'BSTree({repr(self.root)})'
    
def insert(tree, data):
    tree.root = insert_rec(tree.root, data)
    
def insert_rec(node, data):
    if node is None:
        return Node(data)
    
    if data < node.data:
        node.left = insert_rec(node.left, data)
    else:
        node.right = insert_rec(node.right, data)
        
    return node


def change_recursion(num):
    sys.setrecursionlimit(num)

def make_tree():
    try:
        tree = BSTree()
        filename = 'american-english'
        for line in open(filename):
            for word in line.split():
                insert(tree, [word.strip()])
    except RecursionError:
        print("Maximum recursion depth exceeded\n")



change_recursion(10000)
print("\nRecursion limit: " + str(sys.getrecursionlimit()))
make_tree()

