# Step 1: Import deque.
from collections import deque

# Step 2: Create a queue representing a ticket line.
ticket_queue = deque(["Alice", "Bob", "Charlie", "Diana"])

# Step 3: Enqueue a new customer.
ticket_queue.append("Eve")
print("Queue after new customer arrives:", list(ticket_queue))

# Step 4: Serve the first customer by dequeuing.
served_customer = ticket_queue.popleft()
print("Served customer:", served_customer)

# Step 5: Print the remaining queue.
print("Remaining queue:", list(ticket_queue))
