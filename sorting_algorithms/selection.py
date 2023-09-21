from random import randint

list = [randint(0,130) for _ in range(80)]

#selection sort
for i in range(0, len(list)):
    selectedIndex=i
    for j in range(i, len(list)):
        if list[j]<list[selectedIndex]:
            selectedIndex=j
    list[selectedIndex], list[i] = list[i], list[selectedIndex]

for el in list:
    print("█"*el)