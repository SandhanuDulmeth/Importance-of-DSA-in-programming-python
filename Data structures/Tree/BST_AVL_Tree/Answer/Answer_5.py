def is_valid_bst(root, min_val=float('-inf'), max_val=float('inf')):
    if root is None:
        return True
    if not (min_val < root.data < max_val):
        return False
    return (is_valid_bst(root.left, min_val, root.data) and
            is_valid_bst(root.right, root.data, max_val))