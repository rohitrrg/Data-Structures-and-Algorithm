class Queue:
    def __init__(self, capacity):
        self.front = self.size = 0
        self.rear = capacity-1
        self.Q = [None]*capacity
        self.capacity = capacity

    # Queue is full when size become equal to capacity
    def isFull(self):
        return self.size == self.capacity

    # Queue is Empty when size is equal to 0
    def isEmpty(self):
        return self.size == 0

    # Function to add an item to the queue
    # it chages rear and size
    def EnQueue(self, item):
        if self.isFull():
            print('Queue is Full..')
            return
        self.rear = (self.rear+1)%(self.capacity)
        self.Q[self.rear] = item
        self.size = self.size + 1
        print('%s enqueued to the queue'%str(item))

    # Function to remove an item from queue
    # it changes front and size
    def DeQueue(self):
        if self.isEmpty():
            print('Queue is Empty')
            return

        print('%s is dequeued from Queue.' %str(self.Q[self.front]))
        self.front = (self.front + 1) % (self.capacity)
        self.size = self.size - 1

    # Function to get front of the queue
    def que_front(self):
        if self.isEmpty():
            print('Queue is Empty')
            return
        return self.Q[self.front]

    # Function to get rear of the queue
    def que_rear(self):
        if self.isEmpty():
            print('Queue is Empty.')
            return
        return self.Q[self.rear]


if __name__=='__main__':
    q = Queue(30)
    q.EnQueue(1)
    q.EnQueue(2)
    q.EnQueue(3)
    q.EnQueue(4)

    import sys
    print('size:', sys.getsizeof(q))

    q.DeQueue()
    print('Front item is %s' %str(q.que_front()))
    print('Rear item is %s' %str(q.que_rear()))
