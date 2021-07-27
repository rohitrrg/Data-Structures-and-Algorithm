class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.data = key

def peek(stack):
    if len(stack)>0:
        return stack[-1]
    return None

def inorder(root):
    current = root
    stack = []
    done = 0
    while True:
        if current is not None:
            stack.append(current)
            current = current.left
        elif stack:
            current = stack.pop()
            print(current.data, end=' ')
            current = current.right
        else:
            break

def preorder(root):
    if root is None:
        return
    stack = []
    stack.append(root)
    while len(stack):
        node =  stack.pop()
        print(node.data, end=' ')
        if node.right is not None:
            stack.append(node.right)
        if node.left is not None:
            stack.append(node.left)

def postorder(root):
    if root is None:
        return
    
    stack = []
    while True:
        while root:
            if root.right is not None:
                stack.append(root.right)
            stack.append(root)

            root = root.left
        root = stack.pop()

        if root.right is not None and peek(stack)==root.right:
            stack.pop()
            stack.append(root)
            root = root.right
        
        else:
            print(root.data, end=' ')
            root = None
        if len(stack)<=0:
            break
    print()

root = Node(10)
root.left = Node(8)
root.right = Node(2)
root.left.left = Node(3)
root.left.right = Node(5)
root.right.left = Node(2)
 
inorder(root)
print()
preorder(root)
print()
postorder(root)
