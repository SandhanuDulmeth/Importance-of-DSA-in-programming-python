def find_min(root):
    if root.left is None:
        return root.data
    return find_min(root.left)