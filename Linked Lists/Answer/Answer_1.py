class Node:  
    def __init__(self, data):  
        self.data = data  # Store the node's value  
        self.next = None  # Pointer to the next node (default: None)  

class LinkedList:  
    def __init__(self):  
        self.head = None  # Initialize an empty list  