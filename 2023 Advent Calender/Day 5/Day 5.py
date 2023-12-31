
Day_5 = "If You Give A Seed A Fertilizer"

soil = False
fertilizer = False
water = False
light = False
temperature = False
humidity = False
location = False

maps = []

s_line = []
f_line = []
w_line = []
l_line = []
t_line = []
h_line = []
loc_line = []


def file_to_list():
    return_list = []
    data = open("./2023 Advent Calender/Day 5/data.txt")
    #data = open("./2023 Advent Calender/Day 5/test.txt")
    for line in data:
        clean_data = filter(None,line.lower().split("\n"))
        return_list += clean_data

    return return_list


data = file_to_list()



# Part 1
    # I need to find seed numbers, and then run them through the maps. 
    # First checking the ranges, iterating through the source number plus the range max
    # and then mapping them to the destination
    # and then repeating for each map line

def find_seeds(data):
    seeds = []
    for line in data:
        line = line.split()
        for num in line:
            if num.isnumeric():
                seeds.append(num)
        
        return seeds


def map(seeds, line):
    inputs = []
    return_seeds = []

    for i in line:
        i = i.split()
        d = int(i[0])
        s = int(i[1])
        r = int(i[-1])
        

        for x in seeds:
            x = int(x)
            if x >= s:
                if x <= s+r:
                    if x not in inputs:
                        return_seeds.append(x+(d-s))
                        inputs.append(x)

    for x in seeds:
        x = int(x)
        if x not in inputs:
            return_seeds.append(x)

    return return_seeds


for i, line in enumerate(data):

    # This elif chain checks which map you are reading.
    if "seed-to-soil" in line:
        soil = True
    elif "soil-to-fertilizer" in line:
        soil = False
        fertilizer = True
    elif "fertilizer-to-water" in line:
        fertilizer = False
        water = True
    elif "water-to-light" in line:
        water = False
        light = True
    elif "light-to-temperature" in line:
        light = False
        temperature = True
    elif "temperature-to-humidity" in line:
        temperature = False
        humidity = True
    elif "humidity-to-location" in line:
        humidity = False
        location = True

    # This elif chain sends the maps to be categorized by type to be used later.
    if soil and len(line.split()) == 3:
        s_line.append(line)
    elif fertilizer and len(line.split()) == 3:
        f_line.append(line)
    elif water and len(line.split()) == 3:
        w_line.append(line)
    elif light and len(line.split()) == 3:
        l_line.append(line)
    elif temperature and len(line.split()) == 3:
        t_line.append(line)
    elif humidity and len(line.split()) == 3:
        h_line.append(line)
    elif location and len(line.split()) == 3:
        loc_line.append(line)


maps.append(s_line)
maps.append(f_line)
maps.append(w_line)
maps.append(l_line)
maps.append(t_line)
maps.append(h_line)
maps.append(loc_line)

seeds = find_seeds(data)
for m in maps:
    seeds = map(seeds, m)

print("Part 1 =",min(seeds))

# Part 2

# For part two i need to calculate the ranges of the seeds rather than all the numbers being seeds.

