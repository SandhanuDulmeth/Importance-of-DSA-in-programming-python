# Step 1: Import deque.
from collections import deque

# Step 2: Create a queue with several items.
queue = deque(["a", "b", "c", "d"])

# Step 3: Reverse the queue using the reverse() method.
queue.reverse()

# Step 4: Print the reversed queue.
print("Reversed queue:", list(queue))
