# Third Exercise
#
# Reversing the content of Stack using recursion
# You can use only one Stack, no other data structures are needed
# You cannot use any iterative loop
#
# HINT: you need TWO recursive functions one to empty the stack one to fill in

import os, sys
sys.path.append(os.path.join(sys.path[0], "..", "modules"))

from LinearStructures import Stack


def reverseStack(st: Stack):
    if st.isEmpty():
        return
    it=st.pop()
    reverseStack(st)
    reverseStackAux(st, it)
    

def reverseStackAux(st: Stack, it):
    if st.isEmpty():
        st.push(it)
    else:
        it2=st.pop()
        reverseStackAux(st, it)
        st.push(it2)


if __name__ == "__main__":
    st = Stack()

    for i in range(1, 900):
        st.push(i)

    print(st)
    reverseStack(st)
    print(st)
