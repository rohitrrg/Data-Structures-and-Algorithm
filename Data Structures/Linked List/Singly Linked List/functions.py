class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def printList(self):
        temp = self.head
        while temp:
            print(temp.data, end=' ') 
            temp = temp.next
        print('\r')

    def append(self, new_data):

        new_node = Node(new_data)
        
        if self.head is None:
            self.head = new_node
            return

        n = self.head
        while n.next is not None:
            n = n.next
        
        n.next = new_node
    
    def len(self):
        if self.head is None:
            print('Error: List is empty.')
            return

        count = 0
        temp = self.head
        while temp is not None:
            temp = temp.next
            count += 1
        return count
    
    def search(self, x):
        current = self.head
        while current != None:
            if current == x:
                return True
            current = current.next
        return False
    
    def getNth(self, index):
        current = self.head
        count = 0
        while current != None:
            if count == index:
                return current.data
            count += 1
            current = current.next
        assert(False)
        return 0

if __name__ =='__main__':

    llist = LinkedList()
    llist.append(0)
    llist.append(1)
    llist.append(2)
    llist.append(3)

    llist.printList()

    print('The lenght of the Linked List is: ', llist.len())

    if llist.search(3):
        print('The element is present in the LinkedList.')
    else:
        print('The element is present in Linked List.')
    
    print('The element present at given index is:',llist.getNth(3))