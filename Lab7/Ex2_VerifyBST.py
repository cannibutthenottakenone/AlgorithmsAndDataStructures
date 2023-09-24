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


# Basic binary tree
class Node:
    def __init__(self, key):
        self.key = key
        self.leftChild = None
        self.rightChild = None

#the easiest way to do so is to turn it into a vector through an inorder traverse and if the traverse is the same as the sorted vector then the tree is a bst
def isBST(root):
    array=inorder(root)
    sortedA= array.copy()
    sortedA.sort()

    print(array)
    print(sortedA)

    return array==sortedA

def inorder(root):
    array=[]

    if root is None:
        return array
    
    array+=inorder(root.leftChild)
    array+=[root.key]
    array+=inorder(root.rightChild)

    return array


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

    # Expected result: TRUE
    print(isBST(root2))
