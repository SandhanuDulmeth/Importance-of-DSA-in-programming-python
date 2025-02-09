# Step 1: Import deque.
from collections import deque

# Step 2: Create a queue with initial items.
queue = deque(["apple", "banana", "cherry"])

# Step 3: Access the front element without removing it.
front_item = queue[0]

# Step 4: Print the front element.
print("Front item:", front_item)

# Step 5: Print the entire queue to show it remains unchanged.
print("Queue:", list(queue))
