# Reverse each word in a string using a Stack
# Words must stay in the same initial position
# E.g., "Algorithm and Data Structures" will become "mhtiroglA dna ataD serutcurtS"

import sys, os
sys.path.append(os.path.join(sys.path[0], "..", "modules"))

from LinearStructures import Stack


# Reverse each words of a string maintaining their position
def reverserWords(inString):
    st = Stack()
    revString = ""

    inString+=" "

    for i in range(len(inString)):
        if inString[i]!=" ":
            st.push(inString[i])
        else:
            while not st.isEmpty():
                revString+=st.pop()
            revString+=" "

    # return the reversed string
    return revString[:-1]


# Test Code
if __name__ == "__main__":
    myString = "Apelle figlio di Apollo fec una palla di pelle di pollo. Tutti i pesci venner a galle a vedere la palla di pelle di pollo fatta da Apelle figlio di Apollo"
    print(reverserWords(myString))