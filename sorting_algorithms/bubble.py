from random import randint

list = [randint(0,110) for _ in range(50)]

#bubble sort
switched=True
while switched:
    switched=False
    for i in range(0, len(list)-1):
        if list[i]>list[i+1]:
            list[i], list[i+1] = list[i+1], list[i]
            switched=True

for el in list:
    print("█"*el)