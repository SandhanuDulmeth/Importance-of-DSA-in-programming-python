class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, x):
        self.stack.append(x)
        # Step 2: Update min stack
        if not self.min_stack or x <= self.min_stack[-1]:
            self.min_stack.append(x)

    def pop(self):
        if self.stack:
            item = self.stack.pop()
            # Step 3: Maintain min stack
            if item == self.min_stack[-1]:
                self.min_stack.pop()
            return item
        return None

    def getMin(self):
        # Step 4: Get current minimum
        return self.min_stack[-1] if self.min_stack else None

# Example usage:
ms = MinStack()
ms.push(5)
ms.push(2)
ms.push(3)
print(ms.getMin())  # Output: 2
ms.pop()
print(ms.getMin())  # Output: 2
