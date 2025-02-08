def insert_after_value(self, data_after, data_to_insert):  
    if self.head is None:  # Step 1: Empty list  
        print("List is empty!")  
        return  
    current = self.head  
    while current:  # Step 2: Traversal  
        if current.data == data_after:  
            # Step 3: Insert new node  
            new_node = Node(data_to_insert)  
            new_node.next = current.next  
            current.next = new_node  
            return  
        current = current.next  
    print(f"{data_after} not found!")  # Step 4: Value missing  