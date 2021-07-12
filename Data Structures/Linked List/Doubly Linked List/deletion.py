import gc
from typing import Counter

class Node:
    def __init__(self, next=None, prev=None, data=None):
        self.next = next
        self.prev = prev
        self.data = data

class DoublyLinkedList:
    def __init__(self):
        self.head = None
    
    def printLinkedList(self):
        """
        This Function is used to print the elements in list one bye one.
        """
        temp = self.head
        while temp:
            print(temp.data, end=' ')
            temp = temp.next
        print('\r')
    
    def append(self, new_data):

        new_node = Node(data=new_data)
        last = self.head

        new_node.next = None

        if self.head is None:
            new_node.prev = None
            self.head = new_node
            return
        
        while last.next is not None:
            last = last.next
        
        last.next = new_node
        new_node.prev = last
    
    def deleteNode(self, dele):
        """
        This function deletes the given node from the
        given list if its present in the list.
        """
        if self.head is None or dele is None:
            return
        
        if self.head == dele:
            self.head = dele.next
        
        if dele.next is not None:
            dele.next.prev = dele.next
        
        if dele.prev is not None:
            dele.prev.next = dele.next

        gc.collect()
    
    def deleteNodeAtGivenPosition(self, position):
        """
        This function is used to delete the node from the list from given position
        """
        if self.head == None or position<=0:
            return
        
        current = self.head
        i = 1

        while current is not None and i<position:
            current = current.next
            i+=1
        
        if current is None:
            return
        
        DoublyLinkedList.deleteNode(self, current)


if __name__=='__main__':
    dll = DoublyLinkedList()

    dll.append(0)
    dll.append(1)
    dll.append(2)
    dll.append(3)

    dll.deleteNodeAtGivenPosition(2)

    dll.printLinkedList()
            
