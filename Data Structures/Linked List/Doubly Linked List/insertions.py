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
    
    def push(self, new_data):
        new_node = Node(data=new_data)
        new_node.next = self.head
        new_node.prev = Node
        if self.head is not None:
            self.head.prev = new_node
        self.head = new_node
    
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
    
    def insertAfter(self, prev_node, new_data):
        
        temp = self.head
        while temp is not None:
            if temp.data == prev_node:
                break
            temp = temp.next
        
        if prev_node is None:
            print('Node is not present in DLL')
            return
        
        new_node = Node(data=new_data)

        new_node.next = temp.next
        temp.next = new_node
        new_node.prev = temp
        if new_node.next is not None:
            new_node.next.prev = new_node
    
    def insertBefore(self, node, new_data):
        temp = self.head
        while temp.next:
            if temp.next.data == node:
                break
            temp = temp.next

        if temp.next is None:
            print('Node is not present in DLL')
            return

        new_node = Node(data=new_data)

        new_node.next = temp.next
        temp.next = new_node
        new_node.prev = temp
        if new_node.next is not None:
            new_node.next.prev = new_node
    
    def insertAtIndex(self, pos, new_data):
        if pos == 0:
            new_node = Node(data=new_data)
            new_node.next = self.head
            self.head = new_node
            new_node.prev = None
            if self.head is not None:
                self.head.prev = new_node
            self.head = new_node
        
        else:
            index = 0
            temp = self.head
            while temp:
                if index+1 == pos:
                    break
                index += 1
                temp = temp.next
            new_node = Node(data=new_data)
            new_node.next = temp.next
            temp.next = new_node
            new_node.prev = temp
            if new_node.next is not None:
                new_node.next.prev = new_node

if __name__=="__main__":
    dll = DoublyLinkedList()
    
    # add node on first position
    dll.push(0)

    # add node at last position
    dll.append(4)

    # add node after node
    dll.insertAfter(0,1)

    # add node before node
    dll.insertBefore(4,3)

    # add node on index
    dll.insertAtIndex(2,2)

    # print linked list
    dll.printLinkedList()