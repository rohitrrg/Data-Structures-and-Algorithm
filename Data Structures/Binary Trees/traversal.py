class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.data = key

def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=' ')
        inorder(root.right)

def preorder(root):
    if root:
        print(root.data, end=' ')
        preorder(root.left)
        preorder(root.right)

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end=' ')

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
print ("Preorder traversal of binary tree is")
preorder(root)
print()
 
print ("\nInorder traversal of binary tree is")
inorder(root)
print()
 
print ("\nPostorder traversal of binary tree is")
postorder(root)
print()