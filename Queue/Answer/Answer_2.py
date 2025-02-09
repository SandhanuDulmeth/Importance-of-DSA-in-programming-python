class QueueUnderflowError(Exception):
    pass

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            raise QueueUnderflowError("Queue is empty")
        return self.items.pop(0)

    def is_empty(self):
        return len(self.items) == 0

# Test
q = Queue()
try:
    q.dequeue()
except QueueUnderflowError as e:
    print(e)  # Output: Queue is empty