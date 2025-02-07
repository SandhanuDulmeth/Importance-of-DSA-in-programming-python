# Below are 10 step-by-step questions about Python lists (arrays) with detailed explanations and code examples. The first 5 questions cover fundamental concepts, and the last 5 introduce more challenging topics.


## Question 1: How do you create and print a Python list?
### Steps:

1. Define the List: Choose some elements and enclose them within square brackets [ ].

2. Assign the List to a Variable: Save the list in a variable (e.g., my_list).

3. Print the List: Use the print() function to display the list.

4. Verify the Data Type (Optional): Use type() to confirm that it is a list.

[Question 1 Answer](Answer/Answer_1.py)



## Question 2: How do you access elements in a Python list?
### Steps:

1. Create a List: Define a list with several elements.

2. Access by Index: Use the index (starting at 0) to get an element.

3. Use Negative Indexing: Use negative numbers to access elements from the end.

4. Print Each Element: Display the accessed elements.

[Question 2 Answer](Answer/Answer_2.py)



## Question 3: How do you modify elements in a Python list?
### Steps:

1. Create a List: Start with a list of elements.

2. Select the Element to Modify: Identify the index of the element you want to change.

3. Assign a New Value: Replace the old value with a new one.

4. Print the Modified List: Check that the change has been applied.

[Question 3 Answer](Answer/Answer_3.py)



## Question 4: How do you add and remove elements from a Python list?
### Steps:

1. Create a List: Begin with an initial list.

2. Add an Element with append(): Add a new element to the end.

3. Insert an Element with insert(): Add an element at a specific index.

4. Remove an Element with pop(): Remove an element by its index and capture it if needed.

5. Remove an Element with remove(): Delete the first occurrence of a specific value.

6. Print the List After Each Operation: Verify each modification.

[Question 4 Answer](Answer/Answer_4.py)



## Question 5: How do you iterate through a Python list?
### Steps:

1. Create a List: Define a list with several elements.

2. Set Up a for Loop: Write a loop that goes through each element.

3. Print Each Element Inside the Loop: Display the element.

4. (Optional) Perform an Operation: You might transform the element (e.g., convert to uppercase) before printing.

[Question 5 Answer](Answer/Answer_5.py)



## Question 6 (Hard): How do you slice a Python list and perform advanced indexing?
# Steps:

1. Create a List: Define a list with multiple elements. 

2. Slice the List: Use slicing syntax (list[start:stop:step]) to extract a subset.

3. Extract the First Half: Calculate the midpoint and slice.

4. Extract Elements with a Step: Use the step parameter to get every nth element.

5. Use Negative Slicing: Demonstrate slicing with negative indices.

6. Print Each Result: Verify each slicing operation.

[Question 6 Answer](Answer/Answer_6.py)



## Question 7 (Hard): How do you use list comprehensions to filter and transform a list?
### Steps:

1. Create a List of Numbers: Start with a list that contains several numbers.

2. Filter Even Numbers: Use a list comprehension with a condition to select even numbers.

3. Transform the Numbers: Within the same comprehension, perform an operation (e.g., square each number).

4. Print the Resulting List: Check the output of the list comprehension.

[Question 7 Answer](Answer/Answer_7.py)



## Question 8 (Hard): How do you work with nested lists (multi-dimensional lists)?
### Steps:

1. Create a Nested List: Define a list that contains other lists as elements.

2. Access a Sublist: Use indexing to access one of the inner lists.

3. Access an Element in a Sublist: Combine indices to reach a specific element.

4. Iterate Over the Nested List: Use nested loops to traverse every element.

5. Modify an Element: Change a value inside one of the inner lists.

6. Print the Updated Nested List: Verify the modifications.

[Question 8 Answer](Answer/Answer_8.py)



## Question 9 (Hard): How do you sort a list of dictionaries using a lambda function?
### Steps:

1. Create a List of Dictionaries: Each dictionary should contain similar keys (e.g., 'name' and 'age').

2. Decide on a Sorting Key: Choose which key (e.g., age) you want to sort by.

3. Use the sorted() Function: Apply sorted() with a lambda function that extracts the chosen key.

4. Print the Sorted List: Verify that the list is sorted according to the specified key.

[Question 9 Answer](Answer/Answer_9.py)



## Question 10 (Hard): How do you remove duplicates from a list while preserving the original order?
### Steps:

1. Define a Function: Create a function (e.g., remove_duplicates) that accepts a list.

2. Initialize a Container for Seen Items: Use a set to keep track of items already encountered.

3. Initialize a New List for Unique Elements: This list will store items in their original order.

4. Iterate Over the Original List: For each element, check if it is in the "seen" set.

5. Add Unique Elements: If an element has not been seen, add it to both the set and the new list.

6. Return the List of Unique Elements: After iterating, return the new list.

7. Test the Function: Create a list with duplicate values and apply your function.

[Question 10 Answer](Answer/Answer_10.py)

<!-- ``` ctrl+shift+v -->