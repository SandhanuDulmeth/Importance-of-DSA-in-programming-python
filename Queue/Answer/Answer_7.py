# Step 1: Import deque.
from collections import deque

# Step 2: Create two separate queues with different items.
queue1 = deque([1, 2, 3])
queue2 = deque([4, 5, 6])

# Step 3: Merge the second queue into the first using extend().
queue1.extend(queue2)

# Step 4: Print the merged queue.
print("Merged queue:", list(queue1))
