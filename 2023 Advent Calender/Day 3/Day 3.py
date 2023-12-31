
Day_3 = "Gear Ratios"


symbol_coords = []
hot_spots = []
adjacent_nums = ['0']
sum_num = 0
line_count = 0


def file_to_list():
    return_list = []
    data = open("./2023 Advent Calender/Day 3/data.txt")
    #data = open("./2023 Advent Calender/Day 3/test.txt")
    for line in data:
        clean_data = filter(None,line.lower().split("\n"))
        return_list += clean_data

    return return_list


data = file_to_list()


for line in data:
    line_count += 1
    for i, char in enumerate(line):
        if char != ".":
            if not char.isnumeric():
                symbol_coords.append(f"{i} {line_count}")


for line in symbol_coords:
    line = line.split()
    x = int(line[0])
    y = int(line[-1])
    hot_spots.append(f"{x-1} {y}")
    hot_spots.append(f"{x-1} {y-1}")
    hot_spots.append(f"{x} {y-1}")
    hot_spots.append(f"{x+1} {y-1}")
    hot_spots.append(f"{x+1} {y}")
    hot_spots.append(f"{x+1} {y+1}")
    hot_spots.append(f"{x} {y+1}")
    hot_spots.append(f"{x-1} {y+1}")


line_count = 0


for line in data:
    line_count += 1
    one_ago = ""
    two_ago = ""

    for i, char in enumerate(line):

        if f"{i} {line_count}" in hot_spots:
            if char.isnumeric():

#               (..xxx)
                if line[i+1].isnumeric() and line[i+2].isnumeric():
                    adjacent_nums.append(f"{char}{line[i+1]}{line[i+2]}")

#               (.xxx.)
                if one_ago.isnumeric() and line[i+1].isnumeric():
                    if int(f"{one_ago}{char}{line[i+1]}") != int(adjacent_nums[-1]):
                        adjacent_nums.append(f"{one_ago}{char}{line[i+1]}")

#               (xxx..)
                if two_ago.isnumeric() and one_ago.isnumeric():
                    if int(f"{two_ago}{one_ago}{char}") != int(adjacent_nums[-1]):
                        adjacent_nums.append(f"{two_ago}{one_ago}{char}")

#               (..xx.)
                if not one_ago.isnumeric() and line[i+1].isnumeric() and not line[i+2].isnumeric():
                    adjacent_nums.append(f"{char}{line[i+1]}")

#               (.xx..)
                if not two_ago.isnumeric() and one_ago.isnumeric() and not line[i+1].isnumeric():
                    if int(f"{one_ago}{char}") != int(adjacent_nums[-1]):
                        adjacent_nums.append(f"{one_ago}{char}")

#               (..x..)
                if not one_ago.isnumeric() and not line[i+1].isnumeric():
                    adjacent_nums.append(char)


        two_ago = one_ago
        one_ago = char


for line in adjacent_nums:
    sum_num += int(line)


print("Part 1 =", sum_num)


# for part 2 i need...
    #Find star symbols, check nums around them
    #if exactly 2 numbers, multiply them
    #add all gear ratios together


star_products = []


def find_hotspots(x):
    hot_spots = []
    y = 1

    hot_spots.append(f"{x-1} {y}")
    hot_spots.append(f"{x-1} {y-1}")
    hot_spots.append(f"{x} {y-1}")
    hot_spots.append(f"{x+1} {y-1}")
    hot_spots.append(f"{x+1} {y}")
    hot_spots.append(f"{x+1} {y+1}")
    hot_spots.append(f"{x} {y+1}")
    hot_spots.append(f"{x-1} {y+1}")

    return hot_spots


def check_stars(x,lines):
    hotspots = find_hotspots(x)
    adjacent_nums = ['0']
    #print(x, y, hotspots)

    for l, line in enumerate(lines):
        one_ago = ""
        two_ago = ""

        for i, char in enumerate(line):
            if f"{i} {l}" in hotspots:
                if char.isnumeric():

#                   (..xxx)
                    if line[i+1].isnumeric() and line[i+2].isnumeric():
                        adjacent_nums.append(f"{char}{line[i+1]}{line[i+2]}")

#                   (.xxx.)
                    if one_ago.isnumeric() and line[i+1].isnumeric():
                        if int(f"{one_ago}{char}{line[i+1]}") != int(adjacent_nums[-1]):
                            adjacent_nums.append(f"{one_ago}{char}{line[i+1]}")

#                   (xxx..)
                    if two_ago.isnumeric() and one_ago.isnumeric():
                        if int(f"{two_ago}{one_ago}{char}") != int(adjacent_nums[-1]):
                            adjacent_nums.append(f"{two_ago}{one_ago}{char}")

#                   (..xx.)
                    if not one_ago.isnumeric() and line[i+1].isnumeric() and not line[i+2].isnumeric():
                        adjacent_nums.append(f"{char}{line[i+1]}")

#                   (.xx..)
                    if not two_ago.isnumeric() and one_ago.isnumeric() and not line[i+1].isnumeric():
                        if int(f"{one_ago}{char}") != int(adjacent_nums[-1]):
                            adjacent_nums.append(f"{one_ago}{char}")

#                   (..x..)
                    if not one_ago.isnumeric() and not line[i+1].isnumeric():
                        adjacent_nums.append(char)

            two_ago = one_ago
            one_ago = char

    if len(adjacent_nums) == 3:
        return int(adjacent_nums[1]) * int(adjacent_nums[-1])
    else:
        return 0


for y, line in enumerate(data):

    if line == data[0]:
        line_list = [line,data[y+1]]
    elif line != data[-1]:
        line_list = [data[y-1],line,data[y+1]]
    else:
        line_list = [data[y-1],line]
    
    for x, char in enumerate(line):
        if char == "*":
            star_products.append(check_stars(x,line_list))


print("Part 2 =",sum(star_products))