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

    def size(self):
        return len(self.items)

def is_palindrome(queue):
    stack = []
    for _ in range(queue.size()):
        item = queue.dequeue()
        stack.append(item)
        queue.enqueue(item)
    for _ in range(queue.size()):
        item = queue.dequeue()
        if item != stack.pop():
            return False
        queue.enqueue(item)
    return True

# Test
q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(1)
print(is_palindrome(q))  # Output: True