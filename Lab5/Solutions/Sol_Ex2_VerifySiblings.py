# Given a binary Tree and the two nodes A and B determine whether A and B are siblings or not
#
# E.g.
#              35                     A=2 and B=12 are siblings
# 	        /      \                  A=40 and B=7 are siblings
# 	      18 	   10                 A=7 and B=21 are NOT siblings
#  	    /   \     /   \               A=18 and B=1 are NOT siblings
#      3     5   7    40
#    /  \            /   \
#   2   12         21     1
#


from LinearStructures import Stack
from LinearStructures import Queue


# Basic binary tree
class Node:
    def __init__(self, key):
        self.key = key
        self.leftChild = None
        self.rightChild = None


# Recursive solution using a preorder traversal
def _areSiblings(root, nodeA, nodeB):
    if root is None or root.leftChild is None or root.rightChild is None:
        return False

    left_key = root.leftChild.key
    right_key = root.rightChild.key

    # return true is A and B are the children of the current node
    if (left_key == nodeA and right_key == nodeB) or (left_key == nodeB and right_key == nodeA):
        return True

    return _areSiblings(root.leftChild, nodeA, nodeB) or _areSiblings(root.rightChild, nodeA, nodeB)


# Iterative solution using a preorder traversal
def _areSiblings_stack(root, nodeA, nodeB):
    if root is None:
        return False

    st = Stack()
    st.push(root)

    while st.size() > 0:

        current_node = st.pop()

        if current_node.leftChild is not None and current_node.rightChild is not None:
            left_key = current_node.leftChild.key
            right_key = current_node.rightChild.key

            if (left_key == nodeA and right_key == nodeB) or (left_key == nodeB and right_key == nodeA):
                return True

        if current_node.rightChild is not None:
            st.push(current_node.rightChild)
        if current_node.leftChild is not None:
            st.push(current_node.leftChild)

    return False


# Iterative solution using a level order traversal
def _areSiblings_queue(root, nodeA, nodeB):
    if root is None:
        return False

    q = Queue()
    q.enqueue(root)

    while q.size() > 0:

        current_node = q.dequeue()

        if current_node.leftChild is not None and current_node.rightChild is not None:
            left_key = current_node.leftChild.key
            right_key = current_node.rightChild.key

            if (left_key == nodeA and right_key == nodeB) or (left_key == nodeB and right_key == nodeA):
                return True

        if current_node.leftChild:
            q.enqueue(current_node.leftChild)
        if current_node.rightChild:
            q.enqueue(current_node.rightChild)

    return False


def areSiblings(root, nodeA, nodeB):
    if root is None or nodeA is None or nodeB is None:
        return False

    # return _areSiblings(root, nodeA, nodeB)
    # return _areSiblings_stack(root, nodeA, nodeB)
    return _areSiblings_queue(root, nodeA, nodeB)


# Test code
if __name__ == '__main__':
    root1 = Node(35)
    root1.leftChild = Node(18)
    root1.leftChild.leftChild = Node(3)
    root1.leftChild.leftChild.leftChild = Node(2)
    root1.leftChild.leftChild.rightChild = Node(12)
    root1.leftChild.rightChild = Node(5)
    root1.rightChild = Node(10)
    root1.rightChild.leftChild = Node(7)
    root1.rightChild.rightChild = Node(40)
    root1.rightChild.rightChild.leftChild = Node(21)
    root1.rightChild.rightChild.rightChild = Node(1)

    print(areSiblings(root1, 2, 12))  # Expected result: TRUE
    print(areSiblings(root1, 40, 7))  # Expected result: TRUE
    print(areSiblings(root1, 7, 21))  # Expected result: FALSE
    print(areSiblings(root1, 18, 1))  # Expected result: FALSE

