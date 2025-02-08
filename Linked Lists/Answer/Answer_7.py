def remove_by_value(self, data):  
    if self.head is None:  # Step 1: Empty list  
        print("List is empty!")  
        return  
    # Step 2: Head node has the value  
    if self.head.data == data:  
        self.head = self.head.next  
        return  
    current = self.head  
    while current.next:  # Step 3: Traversal  
        if current.next.data == data:  
            # Step 4: Bypass the target node  
            current.next = current.next.next  
            return  
        current = current.next  
    print(f"{data} not found!")  # Step 5: Value missing  