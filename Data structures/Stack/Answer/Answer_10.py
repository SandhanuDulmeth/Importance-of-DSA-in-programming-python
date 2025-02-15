from collections import deque

class AdvancedStack:
    def __init__(self):
        # Step 1: Initialize using collections.deque
        self.stack = deque()

    def push(self, item):
        # Step 2: Push operation using deque.append()
        self.stack.append(item)

    def pop(self):
        # Step 2: Pop operation using deque.pop()
        if not self.is_empty():
            return self.stack.pop()
        raise IndexError("Pop from an empty stack")

    def peek(self):
        # Step 2: Peek at the top element
        if not self.is_empty():
            return self.stack[-1]
        raise IndexError("Peek from an empty stack")

    def is_empty(self):
        # Step 2: Check if the stack is empty
        return len(self.stack) == 0

    def size(self):
        # Step 2: Return the current size of the stack
        return len(self.stack)

    def multi_pop(self, n):
        # Step 3: Pop n elements from the stack
        popped_items = []
        for _ in range(min(n, self.size())):
            popped_items.append(self.pop())
        return popped_items

# Step 5: Testing the AdvancedStack class
if __name__ == "__main__":
    adv_stack = AdvancedStack()
    adv_stack.push(1)
    adv_stack.push(2)
    adv_stack.push(3)
    adv_stack.push(4)
    print("Peek:", adv_stack.peek())      # Should show 4
    print("Size:", adv_stack.size())        # Should be 4
    print("Multi-pop (2 items):", adv_stack.multi_pop(2))  # Should pop 4 and 3
    print("Remaining Stack Size:", adv_stack.size())
