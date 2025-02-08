# 10 Questions on Python Linked Lists (Last 5 are Hard)

 ## 1 Question: How do you create a LinkedList class with a Node structure?
 ### Steps:

1. Define the Node class:

    * Create a class named Node.

    * Add an __init__ method that initializes data (value of the node) and next (pointer to the next node).

    * Set next to None by default (since a new node isn’t linked to anything yet).

    * Define the LinkedList class:

2. Create a class named LinkedList.

    * Add an __init__ method that initializes head (the starting node of the list).

    * Set head to None (empty list by default).

[Question 1 Answer](Answer/Answer_1.py)


## 2 Question: How do you insert multiple values into a linked list at once?
### Steps:

1. Create a method __insert_values__:

    * Define a method that takes a list of values (e.g., __["banana", "mango"]__).

2. Check if the input list is empty:

    * If the input list is empty, do nothing.

3. Insert each value one by one:

    * Loop through each value in the input list.

    * For each value, call a helper method like __insert_at_end__ to add it to the list.

[Question 2 Answer](Answer/Answer_2.py)


## 3.Question: How do you insert a node at the end of a linked list?
### Steps:

1. Create a new node with the given data.

2. Check if the list is empty:

    * If __head__ is __None__, set __head__ to the new node.

3. Traverse to the last node:

    * Start at the __head__ node.

    * Use a loop to move to the next node until you reach a node where __next__ is __None__ (last node).

4. Link the last node to the new node:

    * Set the __next__ pointer of the last node to the new node

[Question 3 Answer](Answer/Answer_3.py)


## 4.Question: How do you print all elements of a linked list?
### Steps:

1. Check if the list is empty:

    * If __head__ is __None__, print "None".

2. Traverse the list:

    * Start at the __head__ node.

    * Use a loop to move to the next node until you reach None.

    * Print each node’s __data__ during traversal.

3. Format the output:

    * Use arrows (__->__) between values and end with "None".

[Question 4 Answer](Answer/Answer_4.py)


## 5.Question: How do you check if a linked list is empty?
### Steps:

1. Check the __head__ attribute:

    * If __head__ is __None__, the list has no nodes.

2. Return a boolean:

    * Return __True__ if empty, __False__ otherwise.

[Question 5 Answer](Answer/Answer_5.py)


## 6.Question: How do you insert a node after the first occurrence of a specific value?
### Steps:

1. Check if the list is empty:

    * If empty, print an error message.

2. Traverse the list to find the target value:

    * Start at the __head__ node.

    * Loop through nodes until you find a node with data equal to data_after.

3. Insert the new node:

    * Create a new node with data_to_insert.

    * Link the new node’s next to the target node’s next.

    * Update the target node’s next to the new node.

4. Handle value not found:

    * If the loop ends without finding the value, print an error.

[Question 6 Answer](Answer/Answer_6.py)


## 7.Question: How do you remove the first node containing a specific value?
### Steps:

1. Check if the list is empty:

    * If empty, print an error.

2. Handle the head node case:

    * If the __head__ node contains the value, update __head__ to __head.next__.

3. Traverse the list to find the value:

    * Loop through nodes, checking if the next node has the value.

4. Bypass the node to delete:

    * If found, link the current node’s __next__ to the node after the target.

5. Handle value not found:

    * If the loop ends without finding the value, print an error.

[Question 7 Answer](Answer/Answer_7.py)


## 8.Question: How do you implement a doubly linked list with prev pointers?
### Steps:

1. Update the __Node__ class:

    * Add a __prev__ attribute to track the previous node.

2. Modify insertion methods (e.g., __insert_at_end__):

    * For a new node, set its __prev__ to the current last node.

3. Modify deletion methods:

    * When deleting a node, update the __prev__ pointer of the next node (if any).

[Question 8 Answer](Answer/Answer_8.py)


## 9.Question: How do you print a doubly linked list backward using prev?
### Steps:

1. Check if the list is empty.

2. Start at the __tail__ node (if tracked).

3. Traverse backward using __prev__:

    * Loop from the tail to the head.

    * Print each node’s __data__.

4. Format the output with arrows __(<-)__.

[Question 9 Answer](Answer/Answer_9.py)


## 10.Question: How do you detect and remove a cycle in a linked list?
### Steps:

1. Detect the cycle with Floyd’s algorithm:

    * Use __slow__ (moves 1 step) and __fast__ (moves 2 steps) pointers.

    * If they meet, a cycle exists.

2. Find the start of the cycle:

    * Reset __slow__ to the head.

    * Move both __slow__ and __fast__ 1 step until they meet again.

3. Break the cycle:

    * Traverse from the meeting point to the last node in the cycle.

    * Set its __next__ to __None__.

[Question 10 Answer](Answer/Answer_10.py)