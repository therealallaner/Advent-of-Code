
Day_10 = "Pipe Maze"
starting_node = "S"
coords = {}
curr = "62 64"

def file_to_list():
    return_list = []
    data = open("./2023 Advent Calender/Day 10/data.txt")
    #data = open("./2023 Advent Calender/Day 10/test.txt")
    for line in data:
        clean_data = filter(None,line.split("\n"))
        return_list += clean_data

    return return_list


data = file_to_list()

def check_pipe(p,curr,c):
    f = curr.split()

    if c == "S":
        return "Nonoivrnoiveveoivve"

    elif p == "North":
        if c == "|":
            r = ["North", f"{f[0]} {int(f[1])+1}"]
            return r

        elif c == "L":
            r = ["West", f"{int(f[0])+1} {f[1]}"]
            return r
        
        elif c == "J":
            r = ["East", f"{int(f[0])-1} {f[1]}"]
            return r

    elif p == "East":
        if c == "-":
            r = ["East", f"{int(f[0])-1} {f[1]}"]
            return r
        elif c == "L":
            r = ["South", f"{f[0]} {int(f[1])-1}"]
            return r
        elif c == "F":
            r = ["North", f"{f[0]} {int(f[1])+1}"]
            return r

    elif p == "South":
        if c == "|":
            r = ["South", f"{f[0]} {int(f[1])-1}"]
            return r
        elif c == "F":
            r = ["West", f"{int(f[0])+1} {f[1]}"]
            return r
        elif c == "7":
            r = ["East", f"{int(f[0])-1} {f[1]}"]
            return r

    elif p == "West":
        if c == "-":
            r = ["West", f"{int(f[0])+1} {f[1]}"]
            return r
        elif c == "7":
            r = ["North", f"{f[0]} {int(f[1])+1}"]
            return r
        elif c == "J":
            r = ["South", f"{f[0]} {int(f[1])-1}"]
            return r

    

for y, l in enumerate(data):
    for x, c in enumerate(l):
        coords[f"{x} {y}"] = True


for y, l in enumerate(data):
    if starting_node in l:
        starting_node = f"{l.index(starting_node)} {y}"
        coords[starting_node] = False


print(starting_node)
prev_dir = "North"
steps = 0
loop = True
while loop:
    c = curr.split()
    for y, l in enumerate(data):
        if y == int(c[1]):
            r = check_pipe(prev_dir,curr,l[int(c[0])])

            print(r,curr,prev_dir, )
            curr = r[1]
            prev_dir = r[0]
            steps += 1

            print(curr,prev_dir, steps//2)

