# Second Exercise: Delete the middle element of Stack
#
# Write a script to remove the middle element of a Stack
# E.g.: input [1, 2, 3, 4, 5]
#       output [1, 2, 4, 5]
#
# NOTE: you can solve the problem using an auxiliary stack or using recursion


from LinearStructures import Stack


# recursive solution
def deleteMidElem_rec(st, mid_point, pos):
    if st.isEmpty():
        return

    # Remove current item
    item = st.pop()

    # Recursive call
    deleteMidElem_rec(st, mid_point, pos + 1)

    # Put all items back except middle
    if pos != mid_point:
        st.push(item)


# iterative solution
def deleteMidElem(st):
    if st.isEmpty():
        return

    mid = int(st.size() / 2)

    pos = 0

    st_tmp = Stack()

    # extract all the element until the mid point
    while pos < mid:
        st_tmp.push(st.pop())
        pos += 1

    # delete mid element
    st.pop()

    # push back all the other elements in the stack
    while not st_tmp.isEmpty():
        st.push(st_tmp.pop())


# Test Code
if __name__ == "__main__":
    st = Stack()

    for i in range(1, 10):
        st.push(i)

    print(st)
    deleteMidElem(st)
    # mid_point = int(st.size()/2)
    # deleteMidElem_rec(st, mid_point, 0)
    print(st)
