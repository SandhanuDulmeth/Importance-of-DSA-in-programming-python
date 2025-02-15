def print(self):  
    if self.head is None:  # Step 1: Empty list  
        print("None")  
        return  
    current = self.head  
    while current:  
        print(current.data, end=" -> ")  # Print with arrow  
        current = current.next  # Move to next node  
    print("None")  # Step 3: End marker  