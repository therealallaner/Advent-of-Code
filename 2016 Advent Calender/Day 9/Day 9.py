from utils.decorators import time_it
from utils.mymethods import Data_to_List


Day_9 = "Explosives in Cyberspace"

test = "(27x12)(20x12)(13x14)(7x10)(1x12)A"
#xabcabcabcabcabcabcy
data = Data_to_List(2016,9,"data")
data = data[0]

@time_it
def Part_1(data):
    newData = ""
    for x, l in enumerate(data):
        c = ""
        r = ""
        adjustedString = ""
        if l == "(":
            firstNum = True
            foundEnding = False
            for i in data[x:]:
                if not foundEnding:
                    if i == ")":
                        foundEnding = True
                    if i == "x":
                        firstNum = False
                    if i.isnumeric():
                        if firstNum:
                            c += str(i)
                        else:
                            r += str(i)
                else:
                    if len(adjustedString) < int(c):
                        adjustedString += str(i)


        if r:
            for _ in range(int(r)):
                newData += adjustedString

        newData += l            
    
    
    newData = newData.replace("("," ").replace(")"," ").split()
    returnString = ""
    for l in newData:
        #print(l)
        if not l[0].isnumeric():
            returnString += l

    print(returnString)
    return len(returnString)

print(Part_1(test))
#Part_1(data)
