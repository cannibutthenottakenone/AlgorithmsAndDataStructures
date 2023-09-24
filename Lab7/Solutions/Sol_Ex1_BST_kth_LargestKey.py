# Given a BST and a number k, find the node with k'th largest key and print its content (key, value)
#
# E.g. With the following tree if k=1 the node is 22, since it is the largest key
#                              if k=2 the node is 12, since it is the second largest key
#      10
#     /  \
#    8 	  12
#   / \     \
#  3   9    22
#


from Lab7.BST import BST
from LinearStructures import Stack


# recursive solution using an inverted inorder traversal
def __kthLargest(root, k, c):
    if root is None or c[0] >= k:
        return

    __kthLargest(root.rightChild, k, c)

    c[0] += 1
    if c[0] == k:
        print(root.key, root.value)
        return

    __kthLargest(root.leftChild, k, c)


def get_kthLargest(root, k):
    # we use a list of one element as a counter instead of a variable to avoid
    # unwanted wrong increments during recursion
    c = [0]
    __kthLargest(root, k, c)


# iterative inorder solution (COMPLEX)
def get_kthLargest_iter(root, k):
    if root is None:
        return

    current = root
    st = Stack()

    index = 0

    while not st.isEmpty() or current is not None:

        if current is not None:
            st.push(current)
            current = current.rightChild

        elif not st.isEmpty():
            current = st.pop()
            index += 1

            if index == k:
                print(current.key, current.value)
                return

            current = current.leftChild


if __name__ == "__main__":
    myTree = BST()
    myTree[10] = "A"
    myTree[8] = "B"
    myTree[12] = "C"
    myTree[3] = "D"
    myTree[9] = "E"
    myTree[22] = "F"

    k = 1  # expected result 22, F
    get_kthLargest(myTree.root, k)
    get_kthLargest_iter(myTree.root, k)

    k = 2  # expected result 12, C
    get_kthLargest(myTree.root, k)
    get_kthLargest_iter(myTree.root, k)

