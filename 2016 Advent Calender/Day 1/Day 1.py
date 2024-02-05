
Day_1 = "No Time for a Taxicab"

direction = "north"
turnR = ["north","east","south","west","north"]
turnL = ["north","west","south","east","north"]


x = 0
y = 0

def file_to_list():
    return_list = []
    data = open("./2016 Advent Calender/Day 1/data.txt")
    #data = open("./2016 Advent Calender/Day 1/test.txt")
    for line in data:
        clean_data = filter(None,line.lower().replace(",","").split("\n"))
        return_list += clean_data

    return return_list


rawData = file_to_list()
data = []

for l in rawData:
    l = l.split()
    for i in l:
        data.append(i)

for l in data:
    tr = turnR.index(f"{direction}")
    tl = turnL.index(f"{direction}")
    for i in l:
        if i == "l":
            direction = turnL[tl+1]
        if i == "r":
            direction = turnR[tr+1]

    if direction == "north":
        y += int(l[1:])

    if direction == "east":
        x += int(l[1:])

    if direction == "south":
        y -= int(l[1:])

    if direction == "west":
        x -= int(l[1:])


print(x+y)

#   Part 2



direction = "north"

locations = []
firstRepeat = []

x = 0
y = 0


def Check_Coords(x,y):
    if (x,y) not in locations:
        coords = x,y
        locations.append(coords)

    elif len(firstRepeat) == 0:
        coords = x,y
        firstRepeat.append(coords)


for l in data:
    tr = turnR.index(f"{direction}")
    tl = turnL.index(f"{direction}")
    for i in l:
        if i == "l":
            direction = turnL[tl+1]
        if i == "r":
            direction = turnR[tr+1]

    if direction == "north":
        for _ in range(int(l[1:])):
            y += 1
            Check_Coords(x,y)

    if direction == "east":
        for _ in range(int(l[1:])):
            x += 1
            Check_Coords(x,y)

    if direction == "south":
        for _ in range(int(l[1:])):
            y -= 1
            Check_Coords(x,y)

    if direction == "west":
        for _ in range(int(l[1:])):
            x -= 1
            Check_Coords(x,y)


part_2 = abs(firstRepeat[0][0]) + abs(firstRepeat[0][1])

print(part_2)