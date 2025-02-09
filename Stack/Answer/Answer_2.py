def reverse_string(s):
    stack = []
    # Step 2: Push all characters onto the stack
    for char in s:
        stack.append(char)
    
    reversed_chars = []
    # Step 3: Pop each character to reverse
    while stack:
        reversed_chars.append(stack.pop())
    
    # Step 4: Join the characters
    return ''.join(reversed_chars)

print(reverse_string("Python"))  # Output: "nohtyP"
