# Reverse the content of a Queue using Recursion
# You can use only one Queue, no other data structures are needed
# You cannot use any iterative loop

from LinearStructures import Queue


def reverseQueue(q):
    if q.isEmpty():
        return

    elem = q.dequeue()
    reverseQueue(q)
    q.enqueue(elem)


if __name__ == "__main__":
    q = Queue()

    for i in range(1, 10):
        q.enqueue(i)

    print(q)
    reverseQueue(q)
    print(q)