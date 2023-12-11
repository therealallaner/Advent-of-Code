from utils import time_it
from itertools import combinations

Day_11 = "Cosmic Expansion"

xcol = []
yrow = []
part_2 = 0
galaxies = []
gal_adj = []


def file_to_list():
    return_list = []
    data = open("./2023 Advent Calender/Day 11/data.txt")
    #data = open("./2023 Advent Calender/Day 11/test.txt")
    for line in data:
        clean_data = filter(None,line.split("\n"))
        return_list += clean_data

    return return_list


data = file_to_list()


def greater_than_x(x):
    for i, v in enumerate(xcol):
        if x < v:
            q = x + (i*(1000000-1))
            return q
        elif x > xcol[-1]:
            q = x + (len(xcol)*(1000000-1))
            return q
        
    return x
        
# Idk why it took me so long to figure the error in these two functions
# The number I wanted to multiple by, had to be subtracted by one. Apparently.
# The way I wrote it at least...

def greater_than_y(y):
    for i, v in enumerate(yrow):
        if y < v:
            w = y + (i*(1000000-1))
            return w
        elif y > yrow[-1]:
            w = y + (len(yrow)*(1000000-1))
            return w
    return y


for i, l in enumerate(data):
    if "#" not in l:
        yrow.append(i)



for l in data:
    for i, x in enumerate(l):
        if i not in xcol:
            xcol.append(i)

for l in data:
    for i, x in enumerate(l):
        if i in xcol:
            if x == "#":
                xcol.remove(i)


for y, l in enumerate(data):
    for x, c in enumerate(l):
        if c == "#":
            g = x,y
            galaxies.append(g)


for g in galaxies:
    q = greater_than_x(g[0])
    w = greater_than_y(g[1])
    a = q,w
    print(a)
    gal_adj.append(a)


for combo in combinations(gal_adj, 2):
    x1 = int(combo[0][0])
    y1 = int(combo[0][1])
    x2 = int(combo[1][0])
    y2 = int(combo[1][1])
    part_2 += abs(x1-x2) + abs(y1-y2)

print(part_2)
