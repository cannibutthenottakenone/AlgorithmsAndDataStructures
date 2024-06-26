# Given a binary tree, verify if, for every node, the key value of the node is equal
# to the sum of the key values of its left and right children.
# Leaf nodes always satisfy this property
#
# This tree satisfy the property
#      10
#     /  \
#    8 	  2
#   / \    \
#  3   5    2
#
# This tree does not satisfy the property
#
#      10
#     /  \
#    8 	  2
#   / \    \
#  3   3    2


# Basic binary tree
class Node:
    def __init__(self, key):
        self.key = key
        self.leftChild = None
        self.rightChild = None


def isChildrenSum(node):
    # BASE CASE: if node is None, or it is a leaf node then return True
    if node is None or (node.leftChild is None and node.rightChild is None):
        return True

    if node.leftChild is None:
        return node.key==node.rightChild.key
    if node.rightChild is None:
        return node.key==node.leftChild.key

    return node.key==node.leftChild.key+node.rightChild.key and isChildrenSum(node.leftChild) and isChildrenSum(node.rightChild)


# Auxiliary method to print the result
def sumPropertySatisfied(rootNode):
    if isChildrenSum(rootNode):
        print("The tree SATISFIES the children sum property")
    else:
        print("The tree DOES NOT SATISFY the children sum property")


# Test Code
if __name__ == '__main__':
    root1 = Node(10)
    root1.leftChild = Node(8)
    root1.rightChild = Node(2)
    root1.leftChild.leftChild = Node(3)
    root1.leftChild.rightChild = Node(5)
    root1.rightChild.rightChild = Node(2)

    sumPropertySatisfied(root1)  # Expected result: SATISFIED

    root2 = Node(10)
    root2.leftChild = Node(8)
    root2.rightChild = Node(2)
    root2.leftChild.leftChild = Node(3)
    root2.leftChild.rightChild = Node(3)
    root2.rightChild.rightChild = Node(2)

    sumPropertySatisfied(root2)  # Expected result: NOT SATISFIED
