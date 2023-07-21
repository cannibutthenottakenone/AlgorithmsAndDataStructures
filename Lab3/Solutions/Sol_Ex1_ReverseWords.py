# Reverse each word in a string using a Stack
# Words must stay in the same initial position
# E.g., "Algorithm and Data Structures" will become "mhtiroglA dna ataD serutcurtS"

import sys, os
sys.path.append(os.path.join(sys.path[0], "..", "..", "modules"))

from LinearStructures import Stack


# Reverses each words of a string maintaining their position
def reverserWords(input_string):
    st = Stack()
    revString = ""

    # Split the string in words
    words = input_string.split()

    for word in words:

        # Traverse given word and push all characters into the stack
        for character in word:
            st.push(character)

        # Pop all the element in the stack
        while not st.isEmpty():
            revString += st.pop()

        # add a space between words
        revString += " "

    return revString


# Test Code
if __name__ == "__main__":
    myString = "Algorithm and Data Structures"
    print(reverserWords(myString))