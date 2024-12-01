from utils.decorators import time_it
from utils.mymethods import Data_to_List
import hashlib

Day_14 = "One-Time Pad"
salt = "jlmsuwbz"


test = "abc18"
#print(hashlib.md5(test.encode()).hexdigest())


def Check_Triplets(s):
    for i in s:
        q = str(i) + str(i) + str(i)
        if q in s:
            z = str(i) + str(i) + str(i) + str(i) + str(i)
            return z

def Check_Quintuplets(s, indexes,index):
    for x in indexes:
        if index < (x+1000):
            if indexes[x] in s:
                print(f'{x} {s}')
                print(index)
                return x
            
            
@time_it
def Part_1():
    salt = "abc"
    index = 0
    searching = True
    indexes = {}
    keys = []

    while searching:
        index += 1
        s = salt + str(index)
        hex = hashlib.md5(s.encode()).hexdigest()


        if Check_Triplets(hex):
            indexes[index] = Check_Triplets(hex)
        
        if Check_Quintuplets(hex, indexes, index):
             keys.append(Check_Quintuplets(hex, indexes, index))
             del indexes[keys[-1]]
             print(len(keys),' ',keys[-1])

        #print(hashlib.md5(salt.encode()).hexdigest())
        if len(keys) == 64:
            searching = False

    print(keys)

Part_1()