
Day_8 = ""

current_pos = "aaa"
turn_counter = 0

def file_to_list():
    return_list = []
    data = open("./2023 Advent Calender/Day 8/data.txt")
    #data = open("./2023 Advent Calender/Day 8/test.txt")
    for line in data:
        clean_data = filter(None,line.lower().replace("(","").replace(")","").replace(",","").split("\n"))
        return_list += clean_data

    return return_list


data = file_to_list()


def lr_map(data):
    map = []
    for line in data:
        for char in line:
            map.append(char)
            
        return map

lr = lr_map(data) * 100


while current_pos != "zzz":
    for line in data:
        if current_pos in line:
            line = line.split()
            if current_pos in line[0]:
                if lr[turn_counter] == "l":
                    current_pos = line[2]
                    if current_pos == "zzz":
                        break
                    turn_counter += 1
                else:
                    current_pos = line[3]
                    if current_pos == "zzz":
                        break
                    turn_counter += 1
print(turn_counter + 1)


# Part 2

ghost_pos = []
turn_counter = 0

for line in data:
    line = line.split()
    if "a" == line[0][2]:
        ghost_pos.append(line[0])

print(ghost_pos)

