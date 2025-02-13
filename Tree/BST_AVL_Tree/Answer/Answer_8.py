def find_lca(root, n1, n2):
    if root is None:
        return None
    if root.data > n1 and root.data > n2:
        return find_lca(root.left, n1, n2)
    if root.data < n1 and root.data < n2:
        return find_lca(root.right, n1, n2)
    return root.data