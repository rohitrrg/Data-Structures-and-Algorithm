class Stack:
    def __init__(self, capacity):
        self.size = 0
        self.top = capacity-1
        self.Stack = [None]*capacity
        self.capacity = capacity
    
    def isFull(self):
        return self.size==self.capacity
    
    def isEmpty(self):
        return self.size==0
    
    def push(self, x):
        if self.isFull():
            print('Stack is Full.')
            return
        self.top = (self.top+1)%(self.capacity)
        self.Stack[self.top] = x
        self.size +=1
        print('%s pushed to the stack' %str(x))
    
    def pop(self):
        if self.isEmpty():
            print('Stack is Empty.')
            return
        x = self.Stack[self.top]
        self.top = (self.top-1)%(self.capacity)
        