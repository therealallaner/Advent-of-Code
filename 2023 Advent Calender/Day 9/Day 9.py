
Day_9 = "Mirage Maintenance"

values = []
values2 = []

def file_to_list():
    return_list = []
    data = open("./2023 Advent Calender/Day 9/data.txt")
    #data = open("./2023 Advent Calender/Day 9/test.txt")
    for line in data:
        clean_data = filter(None,line.lower().split("\n"))
        return_list += clean_data

    return return_list


data = file_to_list()


def next_line(line):
    new_line = []

    for i, num in enumerate(line):
        if i != 0:
            new_line.append(int(num) - int(line[i-1]))

    return new_line


def history(line):
    lines = []
    zeros = False
    line = line.split()
    lines.append(line)


#    while sum(next_line(lines[-1])) != 0:
#        lines.append(next_line(lines[-1]))

    while not zeros:
        if all(value == 0 for value in lines[-1]):
            zeros = True
        if not zeros:
            lines.append(next_line(lines[-1]))

    return lines


def next_value(line):
    hist = history(line)
    #print(hist)
    new_num = 0

    for l in reversed(hist):
        new_num += int(l[-1])

    return new_num


for i, line in enumerate(data):
    #print("This is history number:", f"{i+1}", line)
    values.append(next_value(line))

print("Part 1 =", sum(values))


# Part two
    # just do the same thing but on the front end instead of the back? 
    # maybe i can just use reversed and not do much changing of my code...



def next_line2(line):
    new_line = []

    for i, num in enumerate(line):
        if i != 0:
            new_line.append(int(num) - int(line[i-1]))

    return new_line


def history2(line):
    lines = []
    zeros = False
    line = line.split()
    lines.append(line)


#    while sum(next_line(lines[-1])) != 0:
#        lines.append(next_line(lines[-1]))

    while not zeros:
        if all(value == 0 for value in lines[-1]):
            zeros = True
        if not zeros:
            lines.append(next_line2(lines[-1]))

    return lines


def next_value2(line):
    hist = history2(line)
    #print(hist)
    new_num = 0

    for l in reversed(hist):
        r = l[::-1]
        new_num = int(r[-1]) - new_num

    return new_num


for i, line in enumerate(data):
    #print("This is history number:", f"{i+1}", line)
    values2.append(next_value2(line))

print("Part 2 =", sum(values2))