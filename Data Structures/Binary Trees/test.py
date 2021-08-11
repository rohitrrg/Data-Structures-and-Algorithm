class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.data = val


def inorder(root):
    if root:
        inorder(root.left)
        inorder_ls.append(root.data)
        inorder(root.right)


root = Node(10)
root.left = Node(8)
root.right = Node(2)
root.left.left = Node(3)
root.left.right = Node(5)
root.right.left = Node(2)

inorder_ls = []
inorder(root)
print(inorder_ls)