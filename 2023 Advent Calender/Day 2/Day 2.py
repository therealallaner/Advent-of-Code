
Day_2 = "Cube Conundrum"

total = 0
power_total = 0

def file_to_list():
    return_list = []
    data = open("./2023 Advent Calender/Day 2/data.txt")
    #data = open("./2023 Advent Calender/Day 2/test.txt")
    for line in data:
        clean_data = filter(None,line.lower().replace(":","").replace(",","").replace(";","").split("\n"))
        return_list += clean_data

    return return_list

data = file_to_list()


class Bag:
    def __init__(self):
        self.red = 12
        self.blue = 14
        self.green = 13

bag = Bag()

for line in data:
    line = line.split()
    possible = True
    for item in line[2:]:
        if possible:
            if item.isnumeric():
                if int(item) >= 15:
                    possible = False
    
    for i, item in enumerate(line):
        if possible:
            if item == "red":
                if int(line[i-1]) > bag.red:
                    possible = False
            if item == "blue":
                if int(line[i-1]) > bag.blue:
                    possible = False
            if item == "green":
                if int(line[i-1]) > bag.green:
                    possible = False

    if possible:
        total += int(line[1])

print("Part 1 =", total)

# Part 2

for line in data:
    line = line.split()
    red = 1
    blue = 1
    green = 1

    for i, item in enumerate(line):
        if item == "red":
            if red <= int(line[i-1]):
                red = int(line[i-1])

        if item == "blue":
            if blue <= int(line[i-1]):
                blue = int(line[i-1])

        if item == "green":
            if green <= int(line[i-1]):
                green = int(line[i-1])

    power = red * blue * green
    power_total += power

print("Part 2 =", power_total)