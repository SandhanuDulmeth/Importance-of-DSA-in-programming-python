# Step 1: Import deque.
from collections import deque

# Step 2: Create and populate the queue with items.
queue = deque([1, 2, 3, 4, 5])

# Step 3: Dequeue two items using popleft().
first_removed = queue.popleft()
second_removed = queue.popleft()

# Step 4: Enqueue two more items.
queue.append(6)
queue.append(7)

# Step 5: Print the removed items and the updated queue.
print("Removed items:", first_removed, second_removed)
print("Updated queue:", list(queue))
