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

# most straightforward way, no heuristics, will turn the bst in an ordered list end iterate
def getClosestValue(root, val):
    keys=inorderTrav(root)
    selectedNode=(-1, float('inf')) #key, difference
    for e in keys:
        diff=abs(val-e)
        if diff==0:
            return val
        if diff<selectedNode[1]:
            selectedNode=(e, diff)

    return selectedNode[0]

    
def inorderTrav(root: Node):
    array=[]

    if root is None:
        return array
    
    array+=inorderTrav(root.left)
    array+=[root.key]
    array+=inorderTrav(root.right)

    return array


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

    N = 14  # expected result 15
    print(getClosestValue(bst1.root, N))

    N = 20  # expected result 20
    print(getClosestValue(bst1.root, N))

    N = 13  # expected result 12
    print(getClosestValue(bst1.root, N))
