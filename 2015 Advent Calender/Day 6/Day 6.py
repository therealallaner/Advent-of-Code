coords = {}
val = 0

def file_to_list():
    return_list = []
    data = open("./2015 Advent Calender/Day 6/data.txt")
    for line in data:
        clean_data = filter(None,line.lower().split("\n"))
        return_list += clean_data

    return return_list


Data = file_to_list()

for x in range(1000):
    for y in range(1000):
        coords[f"{x},{y}"] = 0

def turn_on(list):
    xy1 = list[2].split(",")
    xy2 = list[-1].split(",")

    for x in xy1:
        xy1[xy1.index(x)] = int(x)

    for x in xy2:
        xy2[xy2.index(x)] = int(x)

    for x in range(xy1[0],xy2[0]+1):
        for y in range(xy1[1],xy2[1]+1):
            coords[f"{x},{y}"] += 1

def turn_off(list):
    xy1 = list[2].split(",")
    xy2 = list[-1].split(",")

    for x in xy1:
        xy1[xy1.index(x)] = int(x)

    for x in xy2:
        xy2[xy2.index(x)] = int(x)

    for x in range(xy1[0],xy2[0]+1):
        for y in range(xy1[1],xy2[1]+1):
            if coords[f"{x},{y}"] > 0:
                coords[f"{x},{y}"] -= 1

def toggle(list):
    xy1 = list[1].split(",")
    xy2 = list[-1].split(",")

    for x in xy1:
        xy1[xy1.index(x)] = int(x)

    for x in xy2:
        xy2[xy2.index(x)] = int(x)

        
    for x in range(xy1[0],xy2[0]+1):
        for y in range(xy1[1],xy2[1]+1):
            coords[f"{x},{y}"] += 2


for line in Data:

    line = line.split()

    if "toggle" in line:
        toggle(line)

    if "on" in line:
        turn_on(line)

    if "off" in line:
        turn_off(line)



for x in coords.values():
    val += x
    

print("The first answer is 543903")
print(val)


