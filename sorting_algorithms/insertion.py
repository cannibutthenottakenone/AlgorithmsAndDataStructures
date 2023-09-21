from random import randint

list = [randint(0,110) for _ in range(50)]

#insertion sort
sublistLen=0

while(sublistLen<len(list)-1):
    sublistLen+=1
    selectedIndex=0
    for i in range(0, sublistLen):    
        if list[selectedIndex]<list[sublistLen]:
            selectedIndex+=1
    for i in range(sublistLen, selectedIndex, -1):
        list[i], list[i-1] = list[i-1], list[i]

        
for el in list:
    print("█"*el)