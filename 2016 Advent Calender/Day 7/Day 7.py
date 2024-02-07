from utils.mymethods import Data_to_List
from utils.decorators import time_it

Day_7 = "Internet Protocol Version 7"

data = Data_to_List(2016,7,'data')


def Check_Strings(d):
    currChar = ""
    prevChar = ""

    for l in d:
        for i in l:
            prevChar = currChar
            currChar = i

            if prevChar != currChar:
                abba = f"{prevChar}{currChar}{currChar}{prevChar}"
                if len(abba) == 4 and abba in l:
                    return True

    return False


def Split_Strings(l):
    l = l.replace('[',' ').replace(']',' ').split()
    switch = True
    notinBrackets = []
    inBrackets = []


    for i in l:
        if switch:
            notinBrackets.append(i)
        if not switch:
            inBrackets.append(i)

        switch = not switch

    if not Check_Strings(inBrackets):
        if Check_Strings(notinBrackets):
            return True

@time_it
def Part_1(data):
    TLSCounter = 0

    for l in data:
        if Split_Strings(l):
            TLSCounter += 1

    return f"Part 1: {TLSCounter}"




#   Part 2


def Check_Aba(d):
    currChar = ""
    prevChar = ""
    babList = []
    for l in d:
        for i in l:
            prevChar = currChar
            currChar = i

            if prevChar != currChar:
                aba = f"{prevChar}{currChar}{prevChar}"
                if len(aba) == 3 and aba in l:
                    bab = f"{currChar}{prevChar}{currChar}"
                    babList.append(bab)
    
    return babList



def Check_Bab(d,b):
    bab = b
    for b in bab:
        for l in d:
            if b in l:
                return True
                


def Split_Strings_2(l):
    l = l.replace('[',' ').replace(']',' ').split()
    switch = True
    notinBrackets = []
    inBrackets = []


    for i in l:
        if switch:
            notinBrackets.append(i)
        if not switch:
            inBrackets.append(i)

        switch = not switch

    if Check_Aba(notinBrackets):
        aba = Check_Aba(notinBrackets)
        if Check_Bab(inBrackets,aba):
            return True

@time_it
def Part_2(data):
    SSLCounter = 0

    for l in data:
        if Split_Strings_2(l):
            SSLCounter += 1

    return f"Part 1: {SSLCounter}"


print(Part_1(data))
print(Part_2(data))