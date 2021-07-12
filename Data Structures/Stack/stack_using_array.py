from sys import maxsize

def createStack():
    stack = []
    return stack

def isEmpty(stack):
    return len(stack)==0

def push(stack, item):
    stack.append(item)
    print(str(item)+' pushed in stack.')

def pop(stack):
    if isEmpty(stack):
        return str(-maxsize-1) #return minus infinity
    return stack.pop()

def peek(stack):
    if isEmpty(stack):
        return str(-maxsize-1)
    return stack[len(stack)-1]

stack = createStack()
push(stack, 4)
push(stack, 3)
push(stack, 2)
push(stack, 1)

import sys
print('size:', sys.getsizeof(stack))

print('Top element of stack is', peek(stack))
print(str(pop(stack))+ ' popped from stack.')

