
Day_20 = "Pulse Propagation"

Pulse = {}

def file_to_list():
    return_list = []
    data = open("./2023 Advent Calender/Day 20/data.txt")
    #data = open("./2023 Advent Calender/Day 20/test.txt")
    for line in data:
        clean_data = filter(None,line.split("\n"))
        return_list += clean_data

    return return_list


data = file_to_list()

for l in data:
    l = l.split()
    if "%" in l[0]:
        Pulse[f"{l[0][1]}{l[0][2]}"] = "off"
    if "&" in l[0]:
        Pulse[f"{l[0][1]}{l[0][2]}"] = "off"


print(Pulse)
