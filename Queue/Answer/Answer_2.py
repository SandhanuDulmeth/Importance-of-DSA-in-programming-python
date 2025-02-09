# Step 1: Import deque from collections.
from collections import deque

# Step 2: Create an empty queue.
queue = deque()

# Step 3: Check if the queue is empty and print a message.
if not queue:
    print("The queue is empty.")

# Step 4: Enqueue an item.
queue.append("First Item")

# Step 5: Check again and print that the queue is not empty, along with its content.
if queue:
    print("The queue is not empty:", list(queue))
