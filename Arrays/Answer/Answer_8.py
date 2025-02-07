# Step 1: Create a nested list (a list of lists)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print("Original matrix:", matrix)

# Step 2: Access the second row (index 1)
second_row = matrix[1]
print("Second row:", second_row)  # Output: [4, 5, 6]

# Step 3: Access the element '5' in the matrix (row 1, column 1)
element_5 = matrix[1][1]
print("Element at row 1, column 1:", element_5)  # Output: 5

# Step 4: Iterate over each row and then each element in that row
print("All elements in the matrix:")
for row in matrix:
    for element in row:
        print(element, end=" ")
    print()  # for a new line after each row

# Step 5: Modify an element (change the element '9' to '99')
matrix[2][2] = 99

# Step 6: Print the updated matrix
print("Updated matrix:", matrix)
# Expected Updated matrix:
# [
#   [1, 2, 3],
#   [4, 5, 6],
#   [7, 8, 99]
# ]
