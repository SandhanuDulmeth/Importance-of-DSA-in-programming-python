def detect_and_remove_cycle(self):  
    slow = self.head  
    fast = self.head  
    cycle_found = False  
    # Step 1: Detect cycle  
    while fast and fast.next:  
        slow = slow.next  
        fast = fast.next.next  
        if slow == fast:  
            cycle_found = True  
            break  
    if not cycle_found:  
        return  # No cycle  
    # Step 2: Find cycle start  
    slow = self.head  
    while slow != fast:  
        slow = slow.next  
        fast = fast.next  
    # Step 3: Break cycle  
    prev = None  
    while fast.next != slow:  
        prev = fast  
        fast = fast.next  
    if prev:  
        prev.next = None  # Break the link  