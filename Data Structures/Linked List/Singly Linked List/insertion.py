# Node class
class Node:

    # Function tp initialize node object
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    
    # Function to initialize the Linked List object
    def __init__(self):
        self.head = None

    def PrintList(self):
        temp = self.head
        while temp:
            print(temp.data, end=' ') 
            temp = temp.next
        print('\r')

    def push(self, new_data):

        # allocate the Node and put in the data
        new_node = Node(new_data)

        # make next of new Node as head
        new_node.next = self.head

        # move the head to point to new Node
        self.head = new_node

    def append(self, new_data):

        new_node = Node(new_data)
        
        if self.head is None:
            self.head = new_node
            return

        n = self.head
        while n.next is not None:
            n = n.next
        
        n.next = new_node
    
    def insert_after(self, prev_node, new_data):

        n = self.head
        while n is not None:
            if n.data == prev_node:
                break
            n = n.next

        # check if given prev_node is exist
        if prev_node is None:
            print('Error: The given previous node must in Linked List')
            return

        # create new node and put in data
        new_node = Node(new_data)

        # make next of new Node as next of prev_node
        new_node.next = n.next

        # make next of prev_node as new_node
        n.next = new_node

    def insert_before(self, next_node, new_data):
        if self.head is None:
            print("Error: The List is Empty !")
            return

        if self.head.data == next_node:
            new_node = Node(new_data)
            new_node.next = self.head
            self.head = new_node
            return
        
        n = self.head
        while n.next is not None:
            if n.next.data == next_node:
                break
            n = n.next
        if n.next is None:
            print('Item not in the list')
        else:
            new_node = Node(new_data)
            new_node.next = n.next
            n.next = new_node
    
    def insert_at_position(self):
        pass
    
if __name__ == '__main__':

    # start with empty list
    llist = LinkedList()
    llist.head = Node(1)
    second = Node(2)
    third = Node(3)

    llist.head.next = second
    second.next = third

    print('Given Linked List is: ', end='')
    llist.PrintList()

    # push new data 0 at the beginning of linked list
    llist.push(0)

    print('The new linked list after push is: ', end='')
    llist.PrintList()

    # append new data at the end of the Linked List
    llist.append(4)

    print('The new Linked List after append new data: ', end='')
    llist.PrintList()

    # insert new data after given item in Linked List
    llist.insert_after(2, -2)

    print('The new Linked List after inserting data is: ', end='')
    llist.PrintList()

    # insert new data before given item in Linked List
    llist.insert_before(2, -1)

    print('The new Linked List after inserting data is: ', end='')
    llist.PrintList()