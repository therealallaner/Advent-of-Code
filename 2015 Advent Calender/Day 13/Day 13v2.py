from itertools import permutations

Day_13 = "Knights of the Dinner Table"

guests = []
happy_list = []
total_happiness = 0
function_count = 0

def file_to_list():
    return_list = []
    #data = open("./2015 Advent Calender/Day 13/data.txt")
    data = open("./2015 Advent Calender/Day 13/part 2.txt")
    #data = open("./2015 Advent Calender/Day 13/test.txt")
    for line in data:
        clean_data = filter(None,line.lower().replace(".","").split("\n"))
        return_list += clean_data

    return return_list

data = file_to_list()

def happy_meter(l):
    happiness = 0
    first = False
    second = False

    for i, seat in enumerate(l):

        for line in data:
            line = line.split()

            if i == 0:
                if seat == line[0]:
                    if l[i+1] == line[-1]:
                        if "gain" in line:
                            happiness += int(line[3])
                        if "lose" in line:
                            happiness -= int(line[3])
                    
                    if l[-1] == line[-1]:
                        if "gain" in line:
                            happiness += int(line[3])
                        if "lose" in line:
                            happiness -= int(line[3])

            elif seat == l[-1]:
                if seat == line[0]:
                    if l[i-1] == line[-1]:
                        if "gain" in line:
                            happiness += int(line[3])
                            first = True
                        if "lose" in line:
                            happiness -= int(line[3])
                            first = True
                    
                    if l[0] == line[-1]:
                        if "gain" in line:
                            happiness += int(line[3])
                            second = True
                        if "lose" in line:
                            happiness -= int(line[3])
                            second = True

                    if first and second:
                        return happiness

            else:
                if seat == line[0]:
                    if l[i+1] == line[-1]:
                        if "gain" in line:
                            happiness += int(line[3])
                        if "lose" in line:
                            happiness -= int(line[3])
                    
                    if l[i-1] == line[-1]:
                        if "gain" in line:
                            happiness += int(line[3])
                        if "lose" in line:
                            happiness -= int(line[3])


for line in data:
    line = line.split()
    if line[0] not in guests:
        guests.append(line[0])


for perm_list in permutations(guests):
    happy_list.append(happy_meter(perm_list))


for line in happy_list:
    if line >= total_happiness:
        total_happiness = line
        print(line)