from collections import deque

# Using a list as a stack
list_stack = []
list_stack.append(10)  # Push
print("List pop:", list_stack.pop())  # Pop

# Using collections.deque as a stack
deque_stack = deque()
deque_stack.append(20)  # Push
print("Deque pop:", deque_stack.pop())  # Pop

# Step 3: Explanation (in comments)
# Both structures offer O(1) operations for push/pop.
# However, deque is optimized for operations on both ends,
# making it a better choice if you later need queue-like operations.
