def insert_at_bottom(stack, item):
    # Base condition: if stack is empty, insert item at bottom
    if not stack:
        stack.append(item)
    else:
        # Remove top, recurse, then insert the item
        temp = stack.pop()
        insert_at_bottom(stack, item)
        stack.append(temp)

def reverse_stack(stack):
    # Step 1: Base case
    if not stack:
        return
    # Step 2: Pop the top element
    item = stack.pop()
    # Step 3: Reverse the remaining stack recursively
    reverse_stack(stack)
    # Step 4: Insert the popped element at the bottom
    insert_at_bottom(stack, item)

# Example usage:
stack = [1, 2, 3, 4]
reverse_stack(stack)
print(stack)  # Output: [4, 3, 2, 1]
