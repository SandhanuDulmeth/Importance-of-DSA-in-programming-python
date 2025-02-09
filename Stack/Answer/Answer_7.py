def evaluate_postfix(expression):
    tokens = expression.split()
    stack = []
    
    # Step 2 & 3: Process each token
    for token in tokens:
        if token.isdigit():
            stack.append(int(token))
        else:
            # Pop two operands
            right = stack.pop()
            left = stack.pop()
            if token == '+':
                result = left + right
            elif token == '-':
                result = left - right
            elif token == '*':
                result = left * right
            elif token == '/':
                result = left / right  # assuming float division
            stack.append(result)
    # Step 4: Final result
    return stack.pop()

# Example usage:
expr = "3 4 + 2 * 7 /"  # ((3+4)*2)/7
print(evaluate_postfix(expr))  # Output will be a float result
