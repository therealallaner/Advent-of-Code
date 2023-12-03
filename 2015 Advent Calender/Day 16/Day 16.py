
Day_16 = "Aunt Sue"\

matches = []

children = 3
cats = 7
samoyeds = 2
pomeranians = 3
akitas = 0
vizslas = 0
goldfish = 5
trees = 3
cars = 2
perfumes = 1


def file_to_list():
    return_list = []
    data = open("./2015 Advent Calender/Day 16/data.txt")
    #data = open("./2015 Advent Calender/Day 16/test.txt")
    for line in data:
        clean_data = filter(None,line.lower().replace(",","").replace(":","").split("\n"))
        return_list += clean_data

    return return_list


data = file_to_list()

for line in data:
    line = line.split()

    match = 0
    first = line[2]
    second = line[4]
    third = line[6]

    if "children" in line:
        if "children" == first:
            if children == int(line[3]):
                match += 1
        if "children" == second:
            if children == int(line[5]):
                match += 1
        if "children" == third:
            if children == int(line[7]):
                match += 1
                
    if "cats" in line:
        if "cats" == first:
            if cats < int(line[3]):
                match += 1
        if "cats" == second:
            if cats < int(line[5]):
                match += 1
        if "cats" == third:
            if cats < int(line[7]):
                match += 1

    if "samoyeds" in line:
        if "samoyeds" == first:
            if samoyeds == int(line[3]):
                match += 1
        if "samoyeds" == second:
            if samoyeds == int(line[5]):
                match += 1
        if "samoyeds" == third:
            if samoyeds == int(line[7]):
                match += 1

    if "pomeranians" in line:
        if "pomeranians" == first:
            if pomeranians > int(line[3]):
                match += 1
        if "pomeranians" == second:
            if pomeranians > int(line[5]):
                match += 1
        if "pomeranians" == third:
            if pomeranians > int(line[7]):
                match += 1
                
    if "akitas" in line:
        if "akitas" == first:
            if akitas == int(line[3]):
                match += 1
        if "akitas" == second:
            if akitas == int(line[5]):
                match += 1
        if "akitas" == third:
            if akitas == int(line[7]):
                match += 1

    if "vizslas" in line:
        if "vizslas" == first:
            if vizslas == int(line[3]):
                match += 1
        if "vizslas" == second:
            if vizslas == int(line[5]):
                match += 1
        if "vizslas" == third:
            if vizslas == int(line[7]):
                match += 1

    if "goldfish" in line:
        if "goldfish" == first:
            if goldfish > int(line[3]):
                match += 1
        if "goldfish" == second:
            if goldfish > int(line[5]):
                match += 1
        if "goldfish" == third:
            if goldfish > int(line[7]):
                match += 1

    # I got the right answer after only adding these variables in, but ima add the rest anyway.
    # for part 2 i gotta change = into < or > for specific variables.
    
    if "trees" in line:
        if "trees" == first:
            if trees < int(line[3]):
                match += 1
        if "trees" == second:
            if trees < int(line[5]):
                match += 1
        if "trees" == third:
            if trees < int(line[7]):
                match += 1
                
    if "cars" in line:
        if "cars" == first:
            if cars == int(line[3]):
                match += 1
        if "cars" == second:
            if cars == int(line[5]):
                match += 1
        if "cars" == third:
            if cars == int(line[7]):
                match += 1
                
    if "perfumes" in line:
        if "perfumes" == first:
            if perfumes == int(line[3]):
                match += 1
        if "perfumes" == second:
            if perfumes == int(line[5]):
                match += 1
        if "perfumes" == third:
            if perfumes == int(line[7]):
                match += 1

    if match >= 3:
        matches.append(line[1])

print(matches)

for line in data:
    if "213" in line:
        print(line)
    if "323" in line:
        print(line)