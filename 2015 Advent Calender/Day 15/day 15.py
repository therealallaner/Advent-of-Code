from utils.decorators import time_it
from utils.mymethods import Partition_Func
from itertools import permutations, combinations

Day_15 = "Science for Hungry People"

#Sprinkles: capacity 2, durability 0, flavor -2, texture 0, calories 3
#Butterscotch: capacity 0, durability 5, flavor -3, texture 0, calories 3
#Chocolate: capacity 0, durability 0, flavor 5, texture -1, calories 8
#Candy: capacity 0, durability -1, flavor 0, texture 5, calories 8

sprinkles = [2,0,-2,0,3]
butterScotch = [0,5,-3,0,3]
chocolate = [0,0,5,-1,8]
candy = [0,-1,0,5,8]

table = {
    "sprinkles": sprinkles,
    "butterScotch": butterScotch,
    "chocolate": chocolate,
    "candy": candy,
}

ingredients = list(table.keys())


def Score(r,x,t):
    prop = [0, 0, 0, 0, 0]
    for i, amount in enumerate(r):
        ing = x[i]
        for j in range(5):
            prop[j] += amount * t[ing][j]
    
    score = 1
    for x in prop[:4]:
        score *= max(0, x)

    return score


def Score_2(r,x,t):
    prop = [0, 0, 0, 0, 0]
    for i, amount in enumerate(r):
        ing = x[i]
        for j in range(5):
            prop[j] += amount * t[ing][j]
    
    if prop[-1] != 500:
        return 0
    
    score = 1
    for x in prop[:4]:
        score *= max(0, x)

    return score


@time_it
def Part_1():

    best = 0
    for p in Partition_Func(100,4,0):
        for r in permutations(p):
            best = max(best, Score(r,ingredients,table))


    print(best)


@time_it
def Part_2():

    best = 0
    for p in Partition_Func(100,4,0):
        for r in permutations(p):
            best = max(best, Score_2(r,ingredients,table))


    print(best)




Part_1()
Part_2()