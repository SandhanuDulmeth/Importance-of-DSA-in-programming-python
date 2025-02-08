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

1. Create a method insert_values:

    * Define a method that takes a list of values (e.g., ["banana", "mango"]).

2. Check if the input list is empty:

    * If the input list is empty, do nothing.

3. Insert each value one by one:

    * Loop through each value in the input list.

    * For each value, call a helper method like insert_at_end to add it to the list.

[Question 2 Answer](Answer/Answer_2.py)
