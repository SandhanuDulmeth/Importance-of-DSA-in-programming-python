import queue

pq = queue.PriorityQueue()
pq.put((3, "Low priority"))
pq.put((1, "High priority"))
pq.put((2, "Medium priority"))

while not pq.empty():
    print(pq.get()[1])  # Output: High priority, Medium priority, Low priority