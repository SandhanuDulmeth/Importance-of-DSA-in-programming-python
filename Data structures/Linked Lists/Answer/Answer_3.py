def insert_at_end(self, data):  
    new_node = Node(data)  # Step 1: Create a new node  
    if self.head is None:  # Step 2: List is empty  
        self.head = new_node  
        return  
    current = self.head  # Step 3: Start traversal  
    while current.next:  # Loop until last node is found  
        current = current.next  
    current.next = new_node  # Step 4: Link the new node  