# DIFFICULT: Check whether or not a valid expression has redundant parentheses

import os, sys
sys.path.append(os.path.join(sys.path[0], "..", "modules"))

from LinearStructures import Stack


# Function to check redundant parentheses in a valid expression
# It returns True is there are duplicate parentheses False otherwise
def checkRedundancy(expression):

    # set of valid operators
    operators = {"+", "-", "/", "*"}

    # create an empty stack
    st = Stack()

    redundant = False

    for ch in expression:
        if ch!=")":
            st.push(ch)

        else:
            pop = ""
            localRedundant=True 
            while pop!="(":                       
                pop = st.pop()
                if pop in operators:
                    localRedundant=False

            redundant = redundant or localRedundant #this double variable aberration could have just been a return true here and return false on line 35 :<

    return redundant


# Function that prints the result
def isRedundant(expression):
    if checkRedundancy(expression) is True:
        print("The expression has redundant parentheses")
    else:
        print("The expression has no redundant parentheses")


# Test code
if __name__ == '__main__':
    exp = "( (a + b) )"  # Redundant
    isRedundant(exp)

    exp = "( a + (b) / c )"  # Redundant
    isRedundant(exp)

    exp = "( a + ( (b + c) ) )"  # Redundant
    isRedundant(exp)

    exp = "(a + b * (c - d) )"  # Not redundant
    isRedundant(exp)
