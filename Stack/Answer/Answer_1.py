# Step 1: Initialize the stack
stack = []

# Step 2: Push elements onto the stack
stack.append(1)
stack.append(2)
stack.append(3)

# Step 3: Pop the top element
top_element = stack.pop()  # Returns 3

# Step 4: Check if the stack is empty
if not stack:
    print("Stack is empty")
else:
    print("Stack is not empty", stack)
