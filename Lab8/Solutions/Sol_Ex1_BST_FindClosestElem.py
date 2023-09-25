# Given a BST and a number N, return the node key in the BST that is closest to N,
# i.e. the node key with the minimum absolute difference with B.
#
# E.g.
# Given the following BST and N=7 the closest node is 5, since |7-5| = 2 is the minimum difference
#
#             15
#         /       \
#       10        20
#      /  \     /   \
#    5    12   19   25
#


import sys
from LinearStructures import Stack

# WARNING: DO NOT MODIFY

# BST Node
class Node:
    def __init__(self, val):
        self.key = val
        self.left = None
        self.right = None


# Basic BST implementation
class BST:
    def __init__(self):
        self.root = None

    def add(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            self._addNode(self.root, val)

    def _addNode(self, node, val):
        if val < node.key:
            if node.left is None:
                node.left = Node(val)
            else:
                self._addNode(node.left,val)

        if val > node.key:
            if node.right is None:
                node.right = Node(val)
            else:
                self._addNode(node.right, val)

# END DO NOT MODIFY


# Solution 1, binary search using preorder traversal
def getClosestValue(root, val):
    if root.key == val:
        return val

    # the first element keeps track of the current min difference,
    # the second is the closest value in the tree
    res = [sys.maxsize, None]

    return _getClosestValue_preorder(root, val, res)


# Recursive auxiliary method for Solution 1
def _getClosestValue_preorder(root, val, res):

    if root is None:
        return res[1]

    if root.key == val:
        return root.key

    diff = abs(root.key - val)

    if diff < res[0]:
        res[0] = diff
        res[1] = root.key

    # Traverse the tree exploiting the properties of a BST
    if val < root.key:
        return _getClosestValue_preorder(root.left, val, res)
    else:
        return _getClosestValue_preorder(root.right, val, res)


# Solution 2, iterative implementation of Solution 1, using a Stack
def getClosestValue_iterative(root, val):
    if root is None:
        return

    if root.key == val:
        return val

    st = Stack()
    st.push(root)

    min_diff = sys.maxsize
    result = None

    while not st.isEmpty():
        current = st.pop()
        current_val = current.key

        if current_val == val:
            return val

        diff = abs(current_val - val)

        if diff < min_diff:
            min_diff = diff
            result = current_val

        # Traverse the tree exploiting the properties of a BST
        if val < current_val and current.left:
            st.push(current.left)
        elif val > current_val and current.right:
            st.push(current.right)

    return result


# Solution 3, using a modified in-order traversal exploiting the property of a BST
def getClosestValue_inorder(root, val):
    if root.key == val:
        return val

    # the first element keeps track of the current min difference,
    # the second is the closest value in the tree
    res = [sys.maxsize, None]
    _getClosestValue_inorder(root, val, res)
    return res[1]


def _getClosestValue_inorder(root, val, res):
    if root is None:
        return

    _getClosestValue_inorder(root.left, val, res)

    if root.key == val:
        res[0] = 0
        res[1] = val
        return

    diff = abs(root.key - val)

    if diff < res[0]:
        res[0] = diff
        res[1] = root.key
    else:
        return

    _getClosestValue_inorder(root.right, val, res)


# Test Code
if __name__ == '__main__':

    # Sample BST
    bst1 = BST()
    bst1.add(15)
    bst1.add(10)
    bst1.add(20)
    bst1.add(5)
    bst1.add(12)
    bst1.add(19)
    bst1.add(25)

    # VALUES TO TEST

    N = 7  # expected result 5
    print(getClosestValue(bst1.root, N))
    print(getClosestValue_iterative(bst1.root, N))
    print(getClosestValue_inorder(bst1.root, N))

    N = 14  # expected result 15
    print(getClosestValue(bst1.root, N))
    print(getClosestValue_iterative(bst1.root, N))
    print(getClosestValue_inorder(bst1.root, N))

    N = 20  # expected result 20
    print(getClosestValue(bst1.root, N))
    print(getClosestValue_iterative(bst1.root, N))
    print(getClosestValue_inorder(bst1.root, N))

    N = 13  # expected result 12
    print(getClosestValue(bst1.root, N))
    print(getClosestValue_iterative(bst1.root, N))
    print(getClosestValue_inorder(bst1.root, N))

    N = 18  # expected result 19
    print(getClosestValue(bst1.root, N))
    print(getClosestValue_iterative(bst1.root, N))
    print(getClosestValue_inorder(bst1.root, N))