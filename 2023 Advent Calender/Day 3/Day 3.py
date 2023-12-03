
Day_3 = ""

def file_to_list():
    return_list = []
    data = open("./2023 Advent Calender/Day 3/data.txt")
    #data = open("./2023 Advent Calender/Day 3/test.txt")
    for line in data:
        clean_data = filter(None,line.lower().split("\n"))
        return_list += clean_data

    return return_list


data = file_to_list()


print(data)