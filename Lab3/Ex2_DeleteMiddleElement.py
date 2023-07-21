# Second Exercise: Delete the middle element of Stack
#
# Write a script to remove the middle element of a Stack
# E.g.: input [1, 2, 3, 4, 5]
#       output [1, 2, 4, 5]
#
# NOTE: you can solve the problem using an auxiliary stack or using recursion

import os, sys
sys.path.append(os.path.join(sys.path[0], "..", "modules"))

from LinearStructures import Stack


def deleteMidElem(st: Stack):
    support = Stack()
    iterations = int(st.size()/2 - 0.5)

    if st.size()%2==0:
        raise Exception("stack has no middle element")
    else:
        for i in range(iterations):
            support.push(st.pop())
        st.pop()
        for i in range(iterations):
            st.push(support.pop())



# Test Code
if __name__ == "__main__":
    st = Stack()

    for i in range(1, 10):
        st.push(i)

    print(st)
    deleteMidElem(st)
    print(st)
