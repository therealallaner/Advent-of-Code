string_count = 0
raw_str_count = 0

test1 = "" "abc" "aaa\"aaa" "\x27"


def file_to_str():
    return_list = []
    #data = open("./2015 Advent Calender/Day 8/data.txt")
    data = open("./2015 Advent Calender/Day 8/test.txt")
    for line in data:
        clean_data = filter(None,line.lower().split("\n"))
        return_list += clean_data

    return return_list

def file_to_raw():
    return_list = []
    #data = open("./2015 Advent Calender/Day 8/data.txt")
    data = open("./2015 Advent Calender/Day 8/test.txt")
    for line in data:
        clean_data = filter(None,line.lower().split("\n"))
        return_list += clean_data


    return return_list


data_str = file_to_str()
data_raw = file_to_raw()


for line in data_str:
    #print(line)
    for char in line:
        string_count += 1

for line in data_raw:
    #print(line)
    for char in line:
        raw_str_count += 1


print(string_count, raw_str_count)