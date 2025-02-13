# Binary Trees, Binary Search Trees (BST), and AVL Trees. 

## Q1. : How do you create a simple binary tree node in Python?
### Steps:

* Define a class for the binary tree node.

* Initialize the node with data, left, and right attributes.


[Question 1 Answer](Answer/Answer_1.py)

## Q2: How do you perform an in-order traversal of a binary tree?
### Steps:

* Traverse the left subtree.

* Visit the root node.

* Traverse the right subtree.

[Question 2 Answer](Answer/Answer_2.py)

## Q3: How do you insert a value into a Binary Search Tree (BST)?
### Steps:

* If the value is less than the current node, move to the left subtree.

* If the value is greater, move to the right subtree.

* Insert the value as a child if the subtree is empty.

[Question 3 Answer](Answer/Answer_3.py)

## Q4: How do you find the minimum value in a BST?
### Steps:

* Traverse the left subtree until you reach a node with no left child.

* Return the value of that node.

[Question 4 Answer](Answer/Answer_4.py)

## Q5: How do you check if a binary tree is a valid BST?
### Steps:

* Ensure every node’s value lies within valid min and max bounds.

* Recursively validate the left and right subtrees with updated bounds.

[Question 5 Answer](Answer/Answer_5.py)

## Q6: How do you delete a node with two children from a BST?
### Steps:

* Locate the node to delete.

* Replace the node’s value with the maximum value from its left subtree (in-order predecessor).

* Recursively delete the predecessor node from the left subtree.

[Question 6 Answer](Answer/Answer_6.py)

## Q7: How do you balance a BST using AVL tree rotations?
### Steps:

* Calculate the balance factor of a node.

* Perform rotations (LL, RR, LR, RL) based on the balance factor.

[Question 7 Answer](Answer/Answer_7.py)


## Q8: How do you find the lowest common ancestor (LCA) of two nodes in a BST?
### Steps:

* If both nodes are smaller than the current node, move to the left subtree.

* If both nodes are larger, move to the right subtree.

* Otherwise, the current node is the LCA.

[Question 8 Answer](Answer/Answer_8.py)


## Q9: How do you convert a sorted array to a balanced BST?
### Steps:

* Find the middle element of the array and make it the root.

* Recursively build the left and right subtrees using the left and right halves of the array.

[Question 9 Answer](Answer/Answer_9.py)


## Q10: How do you check if two binary trees are identical?
### Steps:

* Check if both trees are empty.

* Check if the current nodes’ data is equal.

* Recursively check the left and right subtrees.

[Question 10 Answer](Answer/Answer_10.py)