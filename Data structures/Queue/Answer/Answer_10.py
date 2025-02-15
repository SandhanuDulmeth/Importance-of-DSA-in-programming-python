# Step 1: Import deque.
from collections import deque

# Step 2: Create a queue with tasks (simulated as strings).
tasks = deque(["Task1", "Task2", "Task3", "Task4"])

# Step 3: Process tasks in a round robin fashion.
for i in range(4):
    # Dequeue the task at the front (simulate processing it).
    current_task = tasks.popleft()
    print(f"Processing {current_task}")
    
    # Step 4: After processing, re-add the task to the end of the queue.
    tasks.append(current_task)
    
    # Step 5: Print the current order of tasks after rotation.
    print("Queue after rotation:", list(tasks))
