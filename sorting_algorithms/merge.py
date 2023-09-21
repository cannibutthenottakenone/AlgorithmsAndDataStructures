from random import randint

def mergeSort(list:list):
    print(list)
    if len(list)==1:
        return list

    partA = mergeSort(list[:round(len(list)/2)])
    partB = mergeSort(list[round(len(list)/2):])
    print("partA",partA)
    print("partB",partB)
    sorted, i, j=[], 0, 0
    while i<len(partA) and j<len(partB):
        if partA[i]<partB[j]:
            sorted.append(partA[i])
            i+=1
        else:
            sorted.append(partB[j])
            j+=1
        
        if i==len(partA):
            sorted += partB[j:]
        if j==len(partB):
            sorted += partA[i:]

    return sorted


list = [randint(0,110) for _ in range(110)]

list = mergeSort(list)

for el in list:
    print("█"*el)