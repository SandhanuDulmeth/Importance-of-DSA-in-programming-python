# Step 1: Define the function to remove duplicates
def remove_duplicates(input_list):
    # Step 2: Create an empty set to store seen elements
    seen = set()
    # Step 3: Create a new list to store unique elements
    unique_list = []
    
    # Step 4: Iterate over each element in the input list
    for item in input_list:
        # Step 5: If the item has not been seen, add it to both 'seen' and 'unique_list'
        if item not in seen:
            seen.add(item)
            unique_list.append(item)
    # Step 6: Return the list of unique elements
    return unique_list

# Step 7: Test the function with a list containing duplicates
original_list = [1, 2, 3, 2, 4, 1, 5, 3, 6]
print("Original list:", original_list)
print("List after removing duplicates:", remove_duplicates(original_list))
# Expected Output: [1, 2, 3, 4, 5, 6]
