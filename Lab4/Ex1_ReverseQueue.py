# Reverse the content of a Queue using Recursion
# You can use only one Queue, no other data structures are needed
# You cannot use any iterative loop
import os, sys
sys.path.append(os.path.join(sys.path[0], "..", "modules"))

from LinearStructures import Queue


def reverseQueue(q: Queue):
    if(q.isEmpty()):
        return
    element=q.dequeue()
    reverseQueue(q)
    q.enqueue(element)

if __name__ == "__main__":
    q = Queue()

    for i in range(1, 10):
        q.enqueue(i)

    print(q)
    reverseQueue(q)
    print(q)