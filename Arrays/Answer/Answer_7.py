# Step 1: Create a list of numbers from 1 to 10
numbers = list(range(1, 11))
print("Original numbers:", numbers)

# Step 2 & 3: Use list comprehension to filter even numbers and square them
even_squares = [x**2 for x in numbers if x % 2 == 0]
print("Squared even numbers:", even_squares)
# Expected Output: [4, 16, 36, 64, 100]
