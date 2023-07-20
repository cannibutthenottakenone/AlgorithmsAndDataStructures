from random import randint

def createRandomList(N: int, R: int):
    """Returns a list of N random integers from 0 to R"""
    l=[]
    for i in range(N):
        l.append(randint(0,R))
    return l

    #alternative code l=[randint(0,R) for i in range(N)]

def countEvenOdd(l: list):
    """given a list of numbers returns a disctionary explicitating the number of odd and even numbers"""
    d = {"even":0, "odd":0}
    for i in l:
        if type(i) != int:
            raise TypeError("the function only accepts a list of numbers")
            return

        if i%2==0:
            d["even"]+=1
        else:
            d["odd"]+=1
    
    return d

def splitEvenOdd(l: list):
    """given a list of numbers returns a disctionary containing two lists, one with all odd numbers from l and one with all evens"""
    d={"even":[], "odd":[]}

    for i in l:
        if type(i) != int:
            raise TypeError("the function only accepts a list of numbers")
            return

        if i%2==0:
            d["even"].append(i)
        else:
            d["odd"].append(i)

    return d

list = createRandomList(100, 100)
print(countEvenOdd(list))
print(splitEvenOdd(list))