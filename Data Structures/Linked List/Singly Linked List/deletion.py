class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        if self.head is None:
            print('Error: No List Found.')
        else:    
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

        temp = self.head
        while temp.next is not None:
            temp = temp.next

        temp.next = new_node

    def delete_at_start(self):

        if self.head is None:
            print('Error: The list has no element to delete')
            return
        
        self.head = self.head.next

    def delete_at_end(self):

        if self.head is None:
            print('Error: The list has no element to be deleted.')
            return
        
        temp = self.head
        while temp.next.next is not None:
            temp = temp.next

        temp.next = None
    
    def detele_by_value(self, value):

        if self.head is None:
            print('Error: The list has no element to be deleted.')
            return
        
        if self.head.data == value:
            self.head = self.head.next
            return
        
        temp = self.head
        while temp.next is not None:
            if temp.next.data == value:
                break
            temp = temp.next
        
        if temp.next is None:
            print('Error: This item not found in the list.')
        else:
            temp.next = temp.next.next

    def delete_by_position(self, pos):
        if self.head is None:
            print('Error: The list has no element to be deleted.')
            return

        if pos==0:
            self.head = self.head.next
            return
        
        i = 0
        temp = self.head
        while i < pos-1 and temp is not None:
            temp = temp.next
            i+=1
        if temp is None:
            print("Error: Index out of bound.")
        else:
            temp.next = temp.next.next
    
    def deleteList(self):
        if self.head is None:
            print("Error: There is no list to be deleted.")
            return

        current = self.head
        while current:
            prev = current.next

            del current.data

            current = prev
        print("List deleted.")
        
        # In python, garbage collection collection happens
        # therefore, only 
        # self.head = None
        # would also delete the linked list


if __name__ == '__main__':

    llist = LinkedList()
    llist.head = Node(0)

    llist.append(1)
    llist.append(2)
    llist.append(3)

    print('The Given Linked List is: ', end='')
    llist.printList()

    # delete the node at the beginning of the LinkeList
    llist.delete_at_start()
    print('The new Linked List is: ', end='')
    llist.printList()

    # delete the node at the end of the linked list
    llist.delete_at_end()
    print('The new Linked List is: ', end='')
    llist.printList()

    # deleter the node containing the specific value
    llist.detele_by_value(2)
    print('The new Linked List is: ', end='')
    llist.printList()

    llist.append(4)
    llist.append(6)

    print('New List is: ', end='')
    llist.printList()

    # delete the node of specific index
    llist.delete_by_position(1)

    print('The new LinkedList is: ',end='')
    llist.printList()

    # delete complete linked list
    llist.deleteList()

    