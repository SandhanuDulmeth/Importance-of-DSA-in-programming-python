class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Dequeue from empty queue")
        return self.items.pop(0)

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        if self.is_empty():
            return None
        return self.items[0]

def merge_sorted_queues(q1, q2):
    result = Queue()
    while not q1.is_empty() and not q2.is_empty():
        if q1.peek() < q2.peek():
            result.enqueue(q1.dequeue())
        else:
            result.enqueue(q2.dequeue())
    # Enqueue remaining elements from q1
    while not q1.is_empty():
        result.enqueue(q1.dequeue())
    # Enqueue remaining elements from q2
    while not q2.is_empty():
        result.enqueue(q2.dequeue())
    return result

# Test
q1 = Queue()
q1.enqueue(1)
q1.enqueue(3)
q1.enqueue(5)

q2 = Queue()
q2.enqueue(2)
q2.enqueue(4)
q2.enqueue(6)

merged = merge_sorted_queues(q1, q2)
print(merged.items)  # Output: [1, 2, 3, 4, 5, 6]