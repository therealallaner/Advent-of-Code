Day_2 = "Bathroom Secrutiy"


x = 0
y = 0

currentNumber = 5
targetCode = []

numberCoords = {
    "-1,1":1,
    "0,1":2,
    "1,1":3,
    "-1,0":4,
    "0,0":5,
    "1,0":6,
    "-1,-1":7,
    "0,-1":8,
    "1,-1":9
    }


def file_to_list():
    return_list = []
    data = open("./2016 Advent Calender/Day 2/data.txt")
    #data = open("./2016 Advent Calender/Day 2/test.txt")
    for line in data:
        clean_data = filter(None,line.lower().split("\n"))
        return_list += clean_data

    return return_list


data = file_to_list()


def Get_New_Coords(i,x,y):
    if i == "u":
        y += 1
    if i == "r":
        x += 1
    if i == "d":
        y -= 1
    if i == "l":
        x -= 1

    if x > 1:
        x = 1
    if x < -1:
        x = -1

    if y > 1:
        y = 1
    if y < -1:
        y = -1

    return x,y



for l in data:
    for i in l:
        coords = Get_New_Coords(i,x,y)
        x = coords[0]
        y = coords[1]
    
    coords = f"{x},{y}"
    digit = numberCoords[coords]
    targetCode.append(digit)


print(targetCode)


# Part 2

x = -2
y = 0

targetCode2 = []

numberCoords2 = {
    "0,2":1,
    "-1,1":2,
    "0,1":3,
    "1,1":4,
    "-2,0":5,
    "-1,0":6,
    "0,0":7,
    "1,0":8,
    "2,0":9,
    "-1,-1":'a',
    "0,-1":'b',
    "1,-1":'c',
    "0,-2":'d'
    }


def Get_New_Coords_2(i,x,y,c):
    if i == "u":
        y += 1
    if i == "r":
        x += 1
    if i == "d":
        y -= 1
    if i == "l":
        x -= 1

    # Border for the 1
    if c == 1:
        if y == 2 and x < 0:
            x = 0
        if y == 2 and x > 0:
            x = 0
        if x == 0 and y > 2:
            y = 2

    # Border for the d
    if c == 'd':
        if y == -2 and x < 0:
            x = 0
        if y == -2 and x > 0:
            x = 0
        if x == 0 and y < -2:
            y = -2

    # Border for the 2, 4
    if c == 2 or c == 4:
        if y == 1 and x < -1:
            x = -1
        if x == -1 and y > 1:
            y = 1

        if y == 1 and x > 1:
            x = 1
        if x == 1 and y > 1:
            y = 1

    # Border for the 5
    if c == 5:
        if x == -2 and y > 0:
            y = 0
        if x == -2 and y < 0:
            y = 0
        if y == 0 and x < -2:
            x = -2

    # Border for the 9
    if c == 9:
        if x == 2 and y > 0:
            y = 0
        if x == 2 and y < 0:
            y = 0
        if y == 0 and x > 2:
            x = 2
        
    # Border for the a, c
    if c == 'a' or c == 'c':
        if y == -1 and x < -1:
            x = -1
        if x == -1 and y < -1:
            y = -1

        if y == -1 and x > 1:
            x = 1
        if x == 1 and y < -1:
            y = -1
        
    
    return x,y

for l in data:
    for i in l:
        currNum = currentNumber
        coords = Get_New_Coords_2(i,x,y,currNum)
        x = coords[0]
        y = coords[1]
        coords = f"{x},{y}"
        digit = numberCoords2[coords]
        currentNumber = digit

    
    coords = f"{x},{y}"
    digit = numberCoords2[coords]
    targetCode2.append(digit)


print(targetCode2)