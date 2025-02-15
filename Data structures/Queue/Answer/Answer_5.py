# Step 1: Import deque.
from collections import deque

# Step 2: Create a queue and enqueue several items.
queue = deque(["x", "y", "z"])

# Step 3: Print the initial length of the queue.
print("Initial length:", len(queue))

# Step 4: Dequeue one item.
queue.popleft()

# Step 5: Print the length of the queue after removal.
print("Length after one dequeue:", len(queue))
