from utils.decorators import time_it
from utils.mymethods import Data_to_List


Day_9 = "Explosives in Cyberspace"

test = "(27x100)(20x12)(13x14)(7x10)(1x120)A"
test2 = "X(8x2)(3x3)ABCY"
data = Data_to_List(2016,9,"data")
data = data[0]


@time_it
def Part_1(data):
    isCounting = False
    isMarker = False
    crSwitch = False
    returnString = ""
    replaceString = ""
    c = ""
    r = ""

    for l in data:
        l = str(l)
        if isCounting:
            if int(c) > 1:
                replaceString += l
                c = int(c) - 1
            else:
                replaceString += l
                c = int(c) - 1
                returnString += replaceString * int(r)
                replaceString = ""
                isCounting = False
        else:
            if l == "(":
                isMarker = True
                c = ""
                r = ""


            elif isMarker:
                if crSwitch:
                    if l.isnumeric():
                        r += l
                else:
                    if l.isnumeric():
                        c += l

                if l == "x":
                    crSwitch = True
                if l == ")":
                    isCounting = True
                    crSwitch = False
                    isMarker = False

                
            else:
                returnString += l

    return returnString

print(len(Part_1(data)))
part2 = Part_1(data)



@time_it
def Part_2(data):
    while ")" in data:
        data = Part_1(data)

    return len(data)


print(Part_2(data))