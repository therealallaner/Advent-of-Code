from utils.mymethods import Data_to_List, Dynamic_Keys
from utils.decorators import time_it


Day_24 = "It Hangs in the Balance"


data = Data_to_List(2015,24,'data')


def Group_Permutation(data,groups,current=[]):
    if len(current) == len(data):
        # If all weights have been assigned to groups, yield the current combination
        yield current
    else:
        # Try assigning the next weight to each group recursively
        for i in range(groups):
            # Create a new list with the current combination plus the next weight assigned to group i
            newCurrent = current + [(i, data[len(current)])]
            # Recursively generate combinations with the new_current list
            yield from Group_Permutation(data, groups, newCurrent)


@time_it
def Main(data): 
    quantumEntanglements = {}
    equalGroups = []
    smallestGroup1 = []

    
    allPermutations = list(Group_Permutation(data,3))


    for l in allPermutations:
        group1 = []
        group2 = []
        group3 = []

        for i in l:
            if i[0] == 0:
                group1.append(int(i[1]))
            if i[0] == 1:
                group2.append(int(i[1]))
            if i[0] == 2:
                group3.append(int(i[1]))

        if sum(group1) == sum(group2) and sum(group1) == sum(group3):
            if l not in equalGroups:
                groups = [group1,group2,group3]
                equalGroups.append(groups)


    for l in equalGroups:
        if not smallestGroup1:
            smallestGroup1 = l
        if len(l[0]) <= len(smallestGroup1[0]):
            smallestGroup1 = l

    print(smallestGroup1)

    for _, l in enumerate(smallestGroup1):
        x = _+1
        #Dynamically_Nested_Lists(quantumEntanglements,'set',x)
        s = Dynamic_Keys('set',x)
        #s = f"set{x}"
        qe = 1
        for i in l:
            qe *= i
        quantumEntanglements[s] = l,qe


    print(quantumEntanglements)


Main(data)