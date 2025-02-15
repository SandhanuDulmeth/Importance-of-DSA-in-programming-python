def print_backward(self):  
    if self.tail is None:  # Empty list  
        print("None")  
        return  
    current = self.tail  
    while current:  
        print(current.data, end=" <- ")  
        current = current.prev  # Move backward  
    print("None")  