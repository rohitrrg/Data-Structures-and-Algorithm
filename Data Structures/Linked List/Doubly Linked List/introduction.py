
class Node:
    def __init__(self, next=None, prev=None, data=None):
        self.next = next
        self.prev = prev
        self.data = data

class DoublyLinkedList:
    def __init__(self):
        self.head = None
    
    def printLinkedList(self):
        temp = self.head
        while temp:
            print(temp.data, end=' ')
            temp = temp.next
        print('\r')
        
if __name__ =='__main__':
    dll = DoublyLinkedList()
    dll.head = Node(data=1)
    second = Node(data=2)
    third = Node(data=3)
    fourth = Node(data=4)

    dll.head.next = second
    second.prev = dll.head
    second.next = third
    third.prev = second
    third.next = fourth
    fourth.prev = third
    fourth.next = None

    dll.printLinkedList()
    import sys
    print('size:', sys.getsizeof(dll))