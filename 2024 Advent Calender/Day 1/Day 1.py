from utils.decorators import time_it
from utils.mymethods import Data_to_List


Day_1 = "Historian Hysteria"

data = Data_to_List(2024,1,'data')


def Part_1(d):
    list1 = []
    list2 = []
    pairs = []
    distance = 0

    for l in d:
        l = l.split()
        x = l[0]
        y = l[1]
        list1.append(x)
        list2.append(y)
        
    while len(list1) > 0:
        x = min(list1)
        y = min(list2)
        z = (x,y)
        pairs.append(z)
        list1.remove(x)
        list2.remove(y)

    for l in pairs:
        x = int(max(l))
        y = int(min(l))
        distance += (x-y)


    return distance


def Part_2(d):
    list1 = []
    list2 = []
    simScore = 0

    for l in d:
        l = l.split()
        x = l[0]
        y = l[1]
        list1.append(x)
        list2.append(y)

    for x in list1:
        c=list2.count(x)
        simScore += (int(x)*c)


    return simScore

x = Part_1(data)
y = Part_2(data)


print(f'The answer to Part 1 is: {x}')
print(f'The answer to part 2 is: {y}')