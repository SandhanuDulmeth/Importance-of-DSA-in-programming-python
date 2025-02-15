# Step 1: Create a list of dictionaries with 'name' and 'age'
people = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 35},
    {"name": "Diana", "age": 28}
]
print("Original list of people:")
for person in people:
    print(person)

# Step 2: Choose 'age' as the key for sorting

# Step 3: Sort the list by age using sorted() with a lambda function
sorted_people = sorted(people, key=lambda person: person['age'])

# Step 4: Print the sorted list
print("\nPeople sorted by age:")
for person in sorted_people:
    print(person)
# Expected Output: List of dictionaries sorted in ascending order by the 'age' key.
