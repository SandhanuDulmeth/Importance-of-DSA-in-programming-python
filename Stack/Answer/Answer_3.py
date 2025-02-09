def is_balanced(expr):
    stack = []
    # Step 1: Iterate through each character
    for char in expr:
        # Step 2: Push opening parentheses
        if char == '(':
            stack.append(char)
        # Step 3: Check closing parentheses
        elif char == ')':
            if not stack:  # No matching opening
                return False
            stack.pop()
    # Step 4: Final check for balance
    return len(stack) == 0

print(is_balanced("(a + b) * (c + d)"))  # True
print(is_balanced("(a + b) * (c + d"))   # False
