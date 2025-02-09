from collections import deque

class Queue:
    def __init__(self):
        self.items = deque()

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Dequeue from empty queue")
        return self.items.popleft()

    def is_empty(self):
        return len(self.items) == 0

    def reverse_first_k(self, k):
        if k > len(self.items):
            raise ValueError("k exceeds queue size")
        temp = [self.dequeue() for _ in range(k)]
        temp.reverse()
        for item in temp:
            self.enqueue(item)
        for _ in range(len(self.items) - k):
            self.enqueue(self.dequeue())

# Test
q = Queue()
for i in [1, 2, 3, 4, 5]:
    q.enqueue(i)
q.reverse_first_k(3)
print(list(q.items))  # Output: [3, 2, 1, 4, 5]