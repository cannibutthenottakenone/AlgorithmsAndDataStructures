# Verify if a given binary tree is a BST or not
#
# E.g.:
#               20              FALSE
#            /     \            18 < 20 in the right subtree
#          15       40          30 > 20 in the left subtree
#        /   \     /  \
#       10   30   18  50
#
#
#               20              TRUE
#            /     \
#          15       40
#        /   \     /  \
#       10   18   30  50
#


import sys
from LinearStructures import Stack

# Basic binary tree
class Node:
    def __init__(self, key):
        self.key = key
        self.leftChild = None
        self.rightChild = None


# Auxiliary method to find max key in a binary tree
def maxValue(root):
    # Base case
    if root is None:
        return -sys.maxsize  # set to -infinity

    # Return maximum value of all the subtree
    res = root.key
    lres = maxValue(root.leftChild)
    rres = maxValue(root.rightChild)
    if lres > res:
        res = lres
    if rres > res:
        res = rres
    return res


# Auxiliary method to find min key in a binary tree
def minValue(root):
    # Base case
    if root is None:
        return sys.maxsize  # set to +infinity

    # Return minimum value of all the subtree
    res = root.key
    lres = minValue(root.leftChild)
    rres = minValue(root.rightChild)
    if lres < res:
        res = lres
    if rres < res:
        res = rres
    return res


# Verify if the tree is a BST by checking if max value in left subtree is smaller than the node
# and min value in right subtree greater than the node
# Very inefficient
def isBST(node):
    if node is None:
        return True

    # false if the max of the left subtree is > than the key of the current root1 node
    if node.leftChild is not None and maxValue(node.leftChild) >= node.key:
        return False

    # false if the min of the right subtree is < than the key of the current root1 node
    if node.rightChild is not None and minValue(node.rightChild) <= node.key:
        return False

    # false if, recursively, the left and/or right subtree is not a BST
    if not isBST(node.leftChild) or not isBST(node.rightChild):
        return False

    return isBST(node.leftChild) or isBST(node.rightChild)


# Verify if the tree is a BST by keeping a valid range (starting from [-INFINITY, INFINITY])
# and keep shrinking it down for each node as we go down recursively
def isBST_preorder(node, minKey, maxKey):
    # base case
    if node is None:
        return True

    # if the node's value falls outside the valid range
    if node.key < minKey or node.key > maxKey:
        return False

    # recursively check left and right subtrees with an updated range
    return isBST_preorder(node.leftChild, minKey, node.key) and isBST_preorder(node.rightChild, node.key, maxKey)


# Verify if the tree is a BST using an inorder traversal
def isBst_inorder(root, prev_key):
    # base case: empty tree is a BST
    if root is None:
        return True

    left = isBst_inorder(root.leftChild, prev_key)

    if root.key < prev_key:
        return False

    prev_key = root.key

    right = isBst_inorder(root.rightChild, prev_key)

    return left and right


# Verify if the tree is a BST using an iterative inorder traversal
def isBst_inorder_iterative(root):

    # base case: empty tree is a BST
    if root is None:
        return True

    current = root
    st = Stack()
    prev_key = - sys.maxsize

    while not st.isEmpty() or current is not None:

        if current is not None:
            st.push(current)
            current = current.leftChild

        elif not st.isEmpty():
            current = st.pop()

            if current.key < prev_key:
                return False

            prev_key = current.key

            current = current.rightChild

    return True


# Test code
if __name__ == "__main__":

    # WARNING: DO NOT MODIFY THE TREE STRUCTURE!
    root1 = Node(20)
    root1.leftChild = Node(15)
    root1.leftChild.leftChild = Node(10)
    root1.leftChild.rightChild = Node(30)
    root1.rightChild = Node(40)
    root1.rightChild.leftChild = Node(18)
    root1.rightChild.rightChild = Node(50)

    # WARNING: DO NOT MODIFY THE TREE STRUCTURE!
    root2 = Node(20)
    root2.leftChild = Node(15)
    root2.leftChild.leftChild = Node(10)
    root2.leftChild.rightChild = Node(18)
    root2.rightChild = Node(40)
    root2.rightChild.leftChild = Node(30)
    root2.rightChild.rightChild = Node(50)

    # Expected result: FALSE
    print(isBST(root1))
    print(isBST_preorder(root1, -sys.maxsize, sys.maxsize))
    print(isBst_inorder(root1, root1.key))
    print(isBst_inorder_iterative(root1))

    # Expected result: TRUE
    print(isBST(root2))
    print(isBST_preorder(root2, -sys.maxsize, sys.maxsize))
    print(isBst_inorder(root2, -sys.maxsize))
    print(isBst_inorder_iterative(root2))
