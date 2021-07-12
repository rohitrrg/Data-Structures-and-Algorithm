class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.root = None
    
    # stack is empty when root/head node is None
    def isEmpty(self):
        if self.root is None:
            return True
        else:
            return False

    # Function to add an item to the stack
    # make new node as root node
    def push(self, item):
        new_node = Node(item)
        new_node.next = self.root
        self.root = new_node
        print(item, 'pushed to the Stack.')

    # Function to remove an item from stack
    def pop(self):
        if self.isEmpty():
            return float("-inf")
        temp = self.root
        self.root = self.root.next
        popped = temp.data
        return popped

    # returns the top items from the stack
    def peek(self):
        if self.isEmpty():
            return float("-inf")
        return self.root.data

if __name__=='__main__':
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)

    import sys
    print('size:', sys.getsizeof(stack))

    print('%d is popped from the stack' %(stack.pop()))
    print('%d is the present at top of the stack.' %(stack.peek()))