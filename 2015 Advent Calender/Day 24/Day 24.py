from utils.mymethods import Data_to_List, List_to_Int
from utils.decorators import time_it
from itertools import combinations


Day_24 = "It Hangs in the Balance"


data = Data_to_List(2015,24,'data')


data = List_to_Int(data)


@time_it
def Find_Bucket_1(data,numberOfbuckets):
    dataAve = sum(data)/numberOfbuckets

    for l in range(len(data)):
        for j in combinations(data, l):
            if sum(j) == dataAve:
                QE = 1
                for i in j:
                    QE = QE * i
                return QE,j
            

Part_1 = Find_Bucket_1(data,3)
Part_2 = Find_Bucket_1(data,4)

print(f"This is Part 1 QE: {Part_1[0]} and bucket 1: {Part_1[1]}")
print(f"This is Part 2 QE: {Part_2[0]} and bucket 1: {Part_2[1]}")