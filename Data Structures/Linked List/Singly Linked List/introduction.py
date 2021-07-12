# Node class
class Node:

    # Function to initialize node object
    def __init__(self, data):
        self.data = data    # Assign data
        self.next = None    # Initialize next as null

class LinkedList:

    # Function to initialize the Linked List object
    def __init__(self):
        self.head = None
    
    # This function prints contents of linked list starting from head.
    def printList(self):
        temp = self.head
        while temp:
            print(temp.data, end=' ')
            temp = temp.next

if __name__ == '__main__':

    # start with an empty list
    llist = LinkedList()
    llist.head = Node(1)
    second = Node(2)
    third = Node(3)
    fourth = Node(4)

    llist.head.next = second
    second.next = third 
    third.next = fourth
    fourth.next = None


    llist.printList()
    import sys
    print('size:', sys.getsizeof(llist))