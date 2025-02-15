#  10 Questions on Python Stacks (Last 5 are Hard)

## 1. Implement a Simple Stack Using a Python List
### Steps:

1. Initialize the Stack: Create an empty list to represent the stack.

2. Push Operation: Use the __append()__ method to add elements.

3. Pop Operation: Use the __pop()__ method to remove the top element.

4. Check if Empty: Use __len(stack)__ or a conditional check to verify if the stack is empty.

[Question 1 Answer](Answer/Answer_1.py)


## 2.Reverse a String Using a Stack
### Steps:

1. Input String: Start with a given string.

2. Push Characters: Iterate over the string and push each character onto the stack (a list).

3. Pop Characters: Pop each character from the stack (which gives them in reverse order).

4. Join Characters: Concatenate the popped characters to form the reversed string.

[Question 2 Answer](Answer/Answer_2.py)


## 3. Check for Balanced Parentheses Using a Stack
### Steps:

1. Iterate Over the String: Loop through each character in the expression.

2. Push Opening Brackets: If you see an opening parenthesis __'('__, push it onto the stack.

3. Match Closing Brackets: When you encounter a closing parenthesis __')'__, pop from the stack and check if it matches.

4. Final Check: After processing the string, if the stack is empty then the parentheses are balanced.

[Question 3 Answer](Answer/Answer_3.py)


## 4. Differentiate Between a Stack and a Queue in Python
### Steps:

1. Define the Data Structures: Explain that a stack is Last-In-First-Out (LIFO) while a queue is First-In-First-Out (FIFO).

2. Implement a Stack: Use a Python list with append() and pop().

3. Implement a Queue: Use collections.deque for efficient FIFO operations.

4. Compare Complexities: Briefly discuss that both operations are generally O(1) but note that lists can be inefficient for queue operations due to O(n) pops from the front.

[Question 4 Answer](Answer/Answer_4.py)


## 5. Find the Maximum Element in a Stack Without Removing Elements
### Steps:

1. Initialize the Stack: Assume the stack is implemented as a list.

2. Iterate Over Elements: Traverse through the list to check every element.

3. Track the Maximum: Use a variable to store the current maximum value as you iterate.

4. Return the Result: After iterating, return the maximum element found.

[Question 5 Answer](Answer/Answer_5.py)

## 6. Reverse a Stack Using Recursion
### Steps:

1. Define the Base Case: If the stack is empty, return.

2. Pop the Top Element: Remove the top element from the stack.

3. Recursively Reverse the Remaining Stack: Call the reverse function on the smaller stack.

4. Insert the Popped Element at the Bottom: Write an auxiliary function to insert an element at the bottom of the stack, then use it.

[Question 6 Answer](Answer/Answer_6.py)

## 7. Evaluate a Postfix Expression Using a Stack
### Steps:

1. Tokenize the Expression: Split the input string into tokens (operands and operators).

2. Push Operands: For every number encountered, push it onto the stack.

3. Apply Operators: When an operator is found, pop the required number of operands, perform the operation, then push the result back.

4. Final Result: After processing all tokens, the result is the only element left in the stack.


[Question 7 Answer](Answer/Answer_7.py)


## 8. Design a Stack That Supports getMin() in O(1) Time
### Steps:

1. Use Two Stacks: One for the main data and another for tracking the minimum element.

2. Push Operation: When pushing, add the element to the main stack and, if it is smaller than or equal to the current minimum, also push it to the min stack.

3. Pop Operation: When popping, if the popped element is equal to the top of the min stack, pop it from the min stack as well.

4. Get Minimum: Simply return the top element of the min stack.

[Question 8 Answer](Answer/Answer_8.py)

## 9. Compare Using a Python List vs. collections.deque for Stack Operations
### Steps:

1. Implement a Stack with a List: Use __append()__ and __pop()__, and note that these are O(1) average operations.

2. Implement a Stack with __collections.deque__: Use its __append()__ and __pop()__ methods, which are also O(1) operations.

3. Discuss Memory and Performance: Compare internal implementations—lists are dynamic arrays while deques are optimized for fast appends and pops from both ends.

4. Show Code Examples: Illustrate both implementations to compare usage and performance.

[Question 9 Answer](Answer/Answer_9.py)


## 10. Design a Complex Stack Class Using collections.deque with Extended Operations
### Steps:

1. Import and Initialize: Import collections.deque and initialize it in your custom stack class.

2. Implement Basic Operations: Write methods for push(), pop(), peek(), is_empty(), and size().

3. Implement Multi-pop: Create a method that accepts an integer n and pops n elements from the stack, returning them in order.

4. Explain Each Step: Comment on the purpose of each method and its internal operation, especially highlighting how deque improves performance for stack operations.

5. Test the Class: Provide a sample usage of the class to demonstrate all operations.

[Question 10 Answer](Answer/Answer_10.py)