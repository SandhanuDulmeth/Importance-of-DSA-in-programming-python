def delete(root, val):
    if root is None:
        return root
    if val < root.data:
        root.left = delete(root.left, val)
    elif val > root.data:
        root.right = delete(root.right, val)
    else:
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        # Node with two children: Replace with in-order predecessor
        root.data = find_max(root.left)
        root.left = delete(root.left, root.data)
    return root

def find_max(root):
    if root.right is None:
        return root.data
    return find_max(root.right)