# Step 1: Create a list of numbers
numbers = [1, 2, 3]

# Step 2: Append an element (4) to the end of the list
numbers.append(4)
print("After append:", numbers)
# Output: [1, 2, 3, 4]

# Step 3: Insert an element (1.5) at index 1
numbers.insert(1, 1.5)
print("After insert at index 1:", numbers)
# Output: [1, 1.5, 2, 3, 4]

# Step 4: Remove an element by index using pop() (remove element at index 2)
removed = numbers.pop(2)
print("Popped element:", removed)
print("After pop:", numbers)
# Expected: Popped element: 2, After pop: [1, 1.5, 3, 4]

# Step 5: Remove an element by value using remove() (remove the first occurrence of 1.5)
numbers.remove(1.5)
print("After remove:", numbers)
# Expected Output: [1, 3, 4]
