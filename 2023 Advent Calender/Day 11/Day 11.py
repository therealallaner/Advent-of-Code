from utils import time_it
from itertools import combinations

Day_11 = "Cosmic Expansion"


x_exp = []
y_exp = []
col = []
g_count = 1
galaxies = []
part_1 = 0


def file_to_list():
    return_list = []
    data = open("./2023 Advent Calender/Day 11/data.txt")
    #data = open("./2023 Advent Calender/Day 11/test.txt")
    for line in data:
        clean_data = filter(None,line.split("\n"))
        return_list += clean_data

    return return_list


data = file_to_list()



for l in data:
    if "#" in l:
        y_exp.append(l)
    else: 
        y_exp.append(l)
        y_exp.append(l)

    for i, x in enumerate(l):
        if i not in col:
            col.append(i)


for l in data:
    for i, x in enumerate(l):
        if i in col:
            if x == "#":
                col.remove(i)


for line in y_exp:
    l = []
    for i, c in enumerate(line):
        l.append(c)

        if i in col:
            l.append(c)

    s = ''.join(map(str, l))
    x_exp.append(s)

data = x_exp

for y, l in enumerate(data):
    for x, c in enumerate(l):
        if c == "#":
            g = x,y
            galaxies.append(g)


for combo in combinations(galaxies, 2):
    x1 = int(combo[0][0])
    y1 = int(combo[0][1])
    x2 = int(combo[1][0])
    y2 = int(combo[1][1])
    part_1 += abs(x1-x2) + abs(y1-y2)
    
print("Part 1 =", part_1)

