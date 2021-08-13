class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
def insert(root, val):
    if root is None:
        root = Node(val)
    else:
        if root.data == val:
            return root
        elif root.data < val:
            root.right = insert(root.right, val)
        else:
            root.left = insert(root.left, val)
    return root


def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=' ')
        inorder(root.right)


r = Node(50)
r = insert(r, 30)
r = insert(r, 20)
r = insert(r, 40)
r = insert(r, 70)
r = insert(r, 60)
r = insert(r, 80)

inorder(r)