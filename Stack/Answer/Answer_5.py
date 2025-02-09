def get_max(stack):
    # Step 2 & 3: Iterate and track maximum
    if not stack:
        return None  # Empty stack case
    max_element = stack[0]
    for item in stack:
        if item > max_element:
            max_element = item
    # Step 4: Return the maximum element
    return max_element

stack = [3, 5, 2, 9, 1]
print(get_max(stack))  # Output: 9
