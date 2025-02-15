# Step 1: Import deque.
from collections import deque

# Step 2: Create a queue and add items.
queue = deque([100, 200, 300, 400])

# Step 3: Clear all elements from the queue using clear().
queue.clear()

# Step 4: Print the cleared queue and verify it is empty.
print("Queue after clearing:", list(queue))
print("Is the queue empty?", not queue)
