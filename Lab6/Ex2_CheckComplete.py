# Check if a binary tree is complete or not
#


class Node:
    # WARNING: DO NOT MODIFY THIS INITIALIZATION METHOD!
    def __init__(self, key):
        self.key = key
        self.leftChild = None
        self.rightChild = None


def verifyComplete(root: Node):
    return checkRightChildren(root) and checkLeftChildren(root.leftChild, root.rightChild)

#checks wheter the children on the right always have their mandatory sibling
def checkRightChildren(root: Node):
    if root.rightChild is None:
        return True

    return root.leftChild is not None and checkRightChildren(root.leftChild) and checkRightChildren(root.rightChild)


#check height of both sides (on the left)
def checkLeftChildren(sideA: Node, sideB: Node):
    aChildren, bChildren = 0, 0
    node=sideA
    while(node.leftChild is not None):
        if node.rightChild is None and node.leftChild.leftChild is not None:
            return False
        node=node.leftChild
        aChildren+=1
    node=sideB
    while(node.leftChild is not None):
        if node.rightChild is None and node.leftChild.leftChild is not None:
            return False
        node=node.leftChild
        bChildren+=1

    deltaChildren=aChildren-bChildren
    return deltaChildren<=1 and deltaChildren>=0

# Test code
if __name__ == '__main__':

    # WARNING: DO NOT MODIFY THE TREE STRUCTURE!
    root1 = Node("A")
    root1.leftChild = Node("B")
    root1.leftChild.leftChild = Node("D")
    root1.leftChild.leftChild.leftChild = Node("H")
    root1.leftChild.leftChild.rightChild = Node("I")
    root1.leftChild.rightChild = Node("E")
    root1.rightChild = Node("C")
    root1.rightChild.leftChild = Node("F")
    root1.rightChild.rightChild = Node("G")

    # WARNING: DO NOT MODIFY THE TREE STRUCTURE!
    root2 = Node("A")
    root2.leftChild = Node("B")
    root2.leftChild.leftChild = Node("D")
    root2.leftChild.rightChild = Node("E")
    root2.rightChild = Node("C")
    root2.rightChild.rightChild = Node("G")

    # WARNING: DO NOT MODIFY THE TREE STRUCTURE!
    root3 = Node("A")
    root3.leftChild = Node("B")
    root3.leftChild.leftChild = Node("D")
    root3.leftChild.leftChild.leftChild = Node("H")
    root3.leftChild.leftChild.rightChild = Node("I")
    root3.leftChild.rightChild = Node("E")
    root3.rightChild = Node("C")

    # Expected result TRUE
    print(verifyComplete(root1))

    # Expected result FALSE
    print(verifyComplete(root2))

    # Expected result FALSE
    print(verifyComplete(root3))

