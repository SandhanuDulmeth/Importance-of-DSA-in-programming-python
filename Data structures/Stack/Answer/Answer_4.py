from collections import deque

# Stack implementation (LIFO)
stack = []
stack.append('a')  # Push
stack.append('b')
print(stack.pop())  # Pop: outputs 'b'

# Queue implementation (FIFO) using deque
queue = deque()
queue.append('a')  # Enqueue
queue.append('b')
print(queue.popleft())  # Dequeue: outputs 'a'
