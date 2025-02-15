# Step 1: Create a list of numbers from 1 to 10
numbers = list(range(1, 11))
print("Original list:", numbers)

# Step 2: Slice the list to get elements from index 2 to 5 (inclusive of index 2, exclusive of 6)
slice1 = numbers[2:6]
print("Elements from index 2 to 5:", slice1)
# Expected Output: [3, 4, 5, 6]

# Step 3: Extract the first half of the list
mid_index = len(numbers) // 2
first_half = numbers[:mid_index]
print("First half of the list:", first_half)
# Expected Output: [1, 2, 3, 4, 5]

# Step 4: Get every second element using step
every_second = numbers[::2]
print("Every second element:", every_second)
# Expected Output: [1, 3, 5, 7, 9]

# Step 5: Use negative slicing to reverse the list
reversed_list = numbers[::-1]
print("Reversed list:", reversed_list)
