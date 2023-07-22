# Third Exercise
#
# Reversing the content of Stack using recursion
# You can use only one Stack, no other data structures are needed
# You cannot use any iterative loop
#
# HINT: you need 2 recursive functions one to empty the stack one to fill in


from LinearStructures import Stack


def insertBack(st, item):
    if st.isEmpty():
        st.push(item)
    else:
        tmp = st.pop()
        insertBack(st, item)
        st.push(tmp)


def reverseStack(st):
    if st.isEmpty():
        return

    el = st.pop()
    reverseStack(st)
    insertBack(st, el)


if __name__ == "__main__":
    st = Stack()

    for i in range(1, 10):
        st.push(i)

    print(st)
    reverseStack(st)
    print(st)
