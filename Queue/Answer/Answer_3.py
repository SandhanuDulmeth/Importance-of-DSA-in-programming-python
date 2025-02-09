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

def reverse_queue(queue):
    stack = []
    while not queue.is_empty():
        stack.append(queue.dequeue())
    while stack:
        queue.enqueue(stack.pop())

# Test
q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
reverse_queue(q)
print(q.items)  # Output: [3, 2, 1]