from utils.mymethods import Data_to_List
from utils.decorators import time_it

Day_15 = "Lens Library"


data = Data_to_List(2023,15,'data')
data = data[0].replace(","," ").split()


def Sum_Lines(l):
    returnSum = 0
    for i in l:
        returnSum += i

    return returnSum

@time_it
def Part_1(data):
    lineValues = []
    for l in data:
        lineValue = 0
        for i in l:
            asciiValue = 0
            asciiValue += ord(i)
            asciiValue += lineValue
            asciiValue = asciiValue * 17
            asciiValue = asciiValue % 256
            lineValue = asciiValue
        
        lineValues.append(lineValue)

    sumLines = Sum_Lines(lineValues)

    return sumLines


print(Part_1(data))


#   Part 2


def Part_2(data):
    pass