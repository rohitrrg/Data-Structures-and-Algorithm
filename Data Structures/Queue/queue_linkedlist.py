class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class Queue:
    def __init__(self):
        self.front = self.rear = None
    
    def isEmpty(self):
        return self.rear == None
    
    def EnQueue(self, item):
        temp = Node(item)
        
        print('%s is queued to the Queue' %str(item))
        if self.rear == None:
            self.front = self.rear = temp
            return
        self.rear.next = temp
        self.rear = temp
        
    
    def DeQueue(self):
        if self.isEmpty():
            print('Queue is Empty')
            return
        
        print('%s is dequeued from the Queue.' %str(self.front.data))
        temp = self.front
        self.front = temp.next

        if self.front == None:
            self.rear == None

    def que_front(self):
        return self.front.data

    def que_rear(self):
        return self.rear.data

if __name__=='__main__':
    q = Queue()
    q.EnQueue(1)
    q.EnQueue(2)
    q.EnQueue(3)
    q.EnQueue(4)
    q.EnQueue(5)

    import sys
    print('size:', sys.getsizeof(q), 'bytes')

    q.DeQueue()
    print('Front item is %s' %str(q.que_front()))
    print('Rear item is %s' %str(q.que_rear()))