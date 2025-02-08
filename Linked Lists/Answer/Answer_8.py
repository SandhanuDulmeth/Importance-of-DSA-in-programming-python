class Node:  
    def __init__(self, data=None, next=None, prev=None):  
        self.data = data  
        self.next = next  
        self.prev = prev  # Added prev pointer  

class DoublyLinkedList:  
    def __init__(self):  
        self.head = None  
        self.tail = None  # Optional: track the end for faster operations  

    def insert_at_end(self, data):  
        new_node = Node(data)  
        if self.head is None:  # Empty list  
            self.head = new_node  
            self.tail = new_node  
        else:  
            new_node.prev = self.tail  # Set new node's prev  
            self.tail.next = new_node  # Link old tail to new node  
            self.tail = new_node  # Update tail  