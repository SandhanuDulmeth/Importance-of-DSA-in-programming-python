def merge_sorted_queues(q1, q2):
    result = Queue()
    while not q1.is_empty() and not q2.is_empty():
        if q1.items[0] < q2.items[0]:
            result.enqueue(q1.dequeue())
        else:
            result.enqueue(q2.dequeue())
    while not q1.is_empty():
        result.enqueue(q1.dequeue())
    while not q2.is_empty():
        result.enqueue(q2.dequeue())
    return result

# Test
q1 = Queue()
q1.enqueue(1)
q1.enqueue(3)
q2 = Queue()
q2.enqueue(2)
q2.enqueue(4)
merged = merge_sorted_queues(q1, q2)
print(merged.items)  # Output: [1, 2, 3, 4]