
Day_12 = "JSAbacusFramework.io"

line_count = 0
sum = 0

def file_to_list():
    return_list = []
    data = open("./2015 Advent Calender/Day 12/data.txt")
    #data = open("./2015 Advent Calender/Day 12/test.txt")
    for line in data:
        clean_data = filter(None,line.lower().split(","))
        return_list += clean_data

    return return_list


data = file_to_list()



for o, line in enumerate(data):
    number_list = []
    negative_list = []

    if "red" in line:
        pass
        #print(data[o-1], line, data[o+1])

    for i, char in enumerate(line):

        if char == "-":
            negative_list.append(char)
            for char in line[i+1:]:
                if char.isnumeric():
                    negative_list.append(char)
        
        if "-" not in line:
            if char.isnumeric():
                number_list.append(char)

    if negative_list:
        numbers = ''.join(map(str,negative_list[1:]))
        #print(numbers)
        sum -= int(numbers)

    if number_list:
        numbers = ''.join(map(str,number_list[0:]))
        #print(numbers)
        sum += int(numbers)


print(sum)
# I might have to completely rewrite this to get part 2...