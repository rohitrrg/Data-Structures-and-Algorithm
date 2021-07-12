class Node:
    def __init__(self, next=None, prev=None, data=None):
        self.next = next
        self.prev = prev
        self.data = data

class DoublyLinkedList:
    def __init__(self):
        self.head = None
    
    def printList(self):
        current = self.head
        while current:
            print(current.data, end=' ')
            current = current.next
        print('\r')
    
    def append(self, new_data):
        new_node = Node(data=new_data)
        temp = self.head

        if self.head is None:
            new_node.prev = None
            self.head = new_node
            return

        while temp.next:
            temp = temp.next

        temp.next = new_node
        new_node.prev = temp
        new_node.next = None
    
    def reverse(self):
        temp = None
        current = self.head

        while current:
            temp = current.prev
            current.prev = current.next
            current.next = temp
            current = current.prev
        
        if temp is not None:
            self.head = temp.prev
    
if __name__=='__main__':
    dll = DoublyLinkedList()

    dll.append(0)
    dll.append(1)
    dll.append(2)
    dll.append(3)

    print('Original List:', end=' ')
    dll.printList()

    print('Reversed List: ', end=' ')
    dll.printList()
