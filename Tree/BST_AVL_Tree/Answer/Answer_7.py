class AVLNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1

def get_height(node):
    if node is None:
        return 0
    return node.height

def get_balance(node):
    if node is None:
        return 0
    return get_height(node.left) - get_height(node.right)

def left_rotate(z):
    y = z.right
    T2 = y.left
    y.left = z
    z.right = T2
    z.height = 1 + max(get_height(z.left), get_height(z.right))
    y.height = 1 + max(get_height(y.left), get_height(y.right))
    return y

def right_rotate(z):
    y = z.left
    T3 = y.right
    y.right = z
    z.left = T3
    z.height = 1 + max(get_height(z.left), get_height(z.right))
    y.height = 1 + max(get_height(y.left), get_height(y.right))
    return y

def insert_avl(root, data):
    if root is None:
        return AVLNode(data)
    if data < root.data:
        root.left = insert_avl(root.left, data)
    else:
        root.right = insert_avl(root.right, data)
    root.height = 1 + max(get_height(root.left), get_height(root.right))
    balance = get_balance(root)
    # Left Left Case
    if balance > 1 and data < root.left.data:
        return right_rotate(root)
    # Right Right Case
    if balance < -1 and data > root.right.data:
        return left_rotate(root)
    # Left Right Case
    if balance > 1 and data > root.left.data:
        root.left = left_rotate(root.left)
        return right_rotate(root)
    # Right Left Case
    if balance < -1 and data < root.right.data:
        root.right = right_rotate(root.right)
        return left_rotate(root)
    return root