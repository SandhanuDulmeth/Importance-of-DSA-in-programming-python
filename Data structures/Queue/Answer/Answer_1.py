# Step 1: Import the deque class from collections.
from collections import deque

# Step 2: Create an empty queue using deque.
queue = deque()

# Step 3: Enqueue items using the append() method.
queue.append(10)
queue.append(20)
queue.append(30)

# Step 4: Dequeue one item using the popleft() method.
removed_item = queue.popleft()

# Step 5: Print the dequeued item and the current state of the queue.
print("Removed item:", removed_item)
print("Current queue:", list(queue))
