from random import randint

def quickSort(list:list):
    if(len(list)<=1):
        return list

    pivot=0
    for i in range(len(list)):
        if list[i]<list[pivot]:
            list[pivot], list[pivot+1], list[i] = list[i], list[pivot], list[pivot+1]

    partA = quickSort(list[:pivot])
    partB = quickSort(list[pivot+1:])

    return partA + [list[pivot]] + partB

list = [randint(0,110) for _ in range(110)]

list = quickSort(list)

for el in list:
    print("█"*el)