from utils.decorators import time_it
from utils.mymethods import Data_to_List, Dynamic_Dictionaries, Dynamically_Nested_Lists
from collections import Counter

Day_6 = "Signals and Noise"

columns = {}
Part_1 = ""
Part_2 = ""

def file_to_list():
    return_list = []
    data = open("./2016 Advent Calender/Day 6/data.txt")
    #data = open("./2016 Advent Calender/Day 6/test.txt")
    for line in data:
        clean_data = filter(None,line.lower().split("\n"))
        return_list += clean_data

    return return_list


#data = file_to_list()

data = Data_to_List(2016,6,'data')

def Counting_Letters(l):
    string = ''.join(l)
    letterCounts = Counter(string)
    desiredLetter = letterCounts.most_common(1)[0][0]
    leastCommonSorted = sorted(letterCounts.items(), key=lambda x: x[1])
    leastCommonLetter = leastCommonSorted[0][0]

    return desiredLetter,leastCommonLetter


for _, i in enumerate(data[0]):
    x = _+1

    d = Dynamically_Nested_Lists(columns,'column',x)
    
#    columnNum = f"column{x}"
#    letterList = []
#    columns[columnNum] = letterList


for p, l in enumerate(data):
    for _, i in enumerate(l):
        x = _+1
        columnNum = f"column{x}"
        columns[columnNum].append(i)

for l in columns:
    returnValues = Counting_Letters(columns[l])
    Part_1 += returnValues[0]
    Part_2 += returnValues[1]


print(f"Part 1 is: {Part_1} and Part 2 is: {Part_2}")