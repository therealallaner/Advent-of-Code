from utils.decorators import time_it
from utils.mymethods import Data_to_List


Day_18 = "Like a GIF For Your Yard"


data = Data_to_List(2015,18,"data")
test = Data_to_List(2015,18,"test")

# count the number of neighbors that are on
def Count_Neighbors(x,y,d):
    count = 0
    badNumbers = [-1,100]

    n = y-1
    e = x+1
    s = y+1
    w = x-1

    north = (x,n)
    east = (e,y)
    south = (x,s)
    west = (w,y)
    northeast = (e,n)
    northwest = (w,n)
    southeast = (e,s)
    southwest = (w,s)

    compass = [northwest,north,northeast,east,southeast,south,southwest,west]
    
    for dir in compass:
        a = dir[0]
        b = dir[1]

        if a in badNumbers:
            pass
        elif b in badNumbers:
            pass
        elif d[b][a] == "#":
            count += 1

    return count

# if off check for 3 on neighbors
# if on check for 2 or 3 neighbors
def Check_Neighbors(i,c):

    #print(f"This should be the count - {c}")

    if c == 3:
        return True
    
    if c == 2:
        if i == "#":
            return True

def Check_For_Corner(x,y):
    corners = [0,99]

    if x in corners:
        if y in corners:
            return True


# if Check_Neighbors() is true: add a #, else: .
def Animate_Grid(d):
    new_data = []

    for y, l in enumerate(d):
        new_line = ""
        for x, i in enumerate(l):
#            if Check_For_Corner(x,y):
#                new_line += "#"
            if Check_Neighbors(i,Count_Neighbors(x,y,d)):
                new_line += "#"
            else:
                new_line += "."

        new_data.append(new_line)

    return new_data


@time_it
def Part_1(data):
    count = 0
    for x in range(100):
        data = Animate_Grid(data)
        #print("")
        #for l in data:
        #    print(l)
        #print("")

    for l in data:
        for i in l:
            if i == "#":
                count += 1

    print(count)



Part_1(data)