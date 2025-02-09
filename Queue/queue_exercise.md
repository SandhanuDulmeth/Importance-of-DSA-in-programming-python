# 10 Questions on Python Queue (Last 5 are Hard)

## 1.Basic Queue Operations
### Steps:

* Import the deque class from the collections module.
* Create an empty queue using deque().
* Enqueue at least three items using the append() method.
* Dequeue one item using the popleft() method.
* Print the removed item and the current state of the queue.

[Question 1 Answer](Answer/Answer_1.py)

## 2.Check if the Queue is Empty
### Steps:

* Import the deque class from the collections module.
* Create an empty queue.
* Check if the queue is empty and print an appropriate message.
* Enqueue one item into the queue.
* Check again to confirm the queue is not empty and print the current queue.

[Question 2 Answer](Answer/Answer_2.py)

## 3.Peek at the Front of the Queue
### Steps:

* Import the deque class from the collections module.
* Create a queue with at least three items.
* Access (peek) the front element without removing it.
* Print the front element.
* Print the entire queue to show it remains unchanged.

[Question 3 Answer](Answer/Answer_3.py)

## 4.Enqueue and Dequeue Multiple Times
### Steps:

* Import the deque class from the collections module.
* Create a queue with at least five items.
* Dequeue two items using the popleft() method.
* Enqueue two new items using the append() method.
* Print the removed items and the updated state of the queue.

[Question 4 Answer](Answer/Answer_4.py)

## 5.Finding the Length of the Queue
### Steps:

* Import the deque class from the collections module.
* Create a queue with several items.
* Print the initial length of the queue using len().
* Dequeue one item from the queue.
* Print the new length of the queue after removal.

[Question 5 Answer](Answer/Answer_5.py)


## 6.Reverse the Queue
### Steps:

* Import the deque class from the collections module.
* Create a queue with at least four items.
* Reverse the queue using the reverse() method.
* Print the reversed queue.

[Question 6 Answer](Answer/Answer_6.py)

## 7.Merge Two Queues
### Steps:

* Import the deque class from the collections module.
* Create two separate queues with different items.
* Merge the second queue into the first using the extend() method.
* Print the merged queue.

[Question 7 Answer](Answer/Answer_7.py)

## 8.Clear All Elements from the Queue
### Steps:

* Import the deque class from the collections module.
* Create a queue and add several items.
* Clear all items from the queue using the clear() method.
* Print the cleared queue and verify that it is empty.

[Question 8 Answer](Answer/Answer_8.py)

## 9.Simulate a Ticketing System Queue
### Steps:

* Import the deque class from the collections module.
* Create a queue representing a line of customers (e.g., names).
* Enqueue a new customer to the end of the queue.
* Dequeue (serve) the first customer using popleft().
* Print the served customer and the remaining queue.

[Question 9 Answer](Answer/Answer_9.py)

## 10.Implement a Round Robin Scheduler
### Steps:

* Import the deque class from the collections module.
* Create a queue with tasks (as strings) for a round robin scheduler.
* Dequeue (process) the task at the front of the queue.
* Enqueue the processed task back to the end of the queue using append().
* Print the current order of tasks after each rotation.

[Question 10 Answer](Answer/Answer_10.py)