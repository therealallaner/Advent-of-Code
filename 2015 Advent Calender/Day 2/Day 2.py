

def get_cube_total(l,w,h):
    extra = remove_largest(l,w,h)
    return 2*(l*w) + 2*(w*h) + 2*(h*l) + extra[0] * extra[1]


def remove_largest(l,w,h):
    list = [l,w,h]
    largest = 0
    for int in list:
        if int > largest:
            largest = int
    list.remove(largest)
    return list


    return list[0] * list[1]

def get_l_w_h(string):
    list = string.split("x")
    counter = 0
    for item in list:
        list[counter] = int(item)
        counter += 1
    return list


def file_to_list():
    return_list = []
    data = open("./2015 Advent Calender/Day 2/data.txt")
    for line in data:
        clean_data = line.lower().split()
        return_list += clean_data
    return return_list

def get_bow_length(l,w,h):
    list = remove_largest(l,w,h)
    ribbon_length = 2*list[0] + 2*list[1] + l*w*h
    return ribbon_length


data = file_to_list()

total_area = 0
ribbon_needed = 0

for line in data:
    lwh = get_l_w_h(line)
    l = lwh[0]
    w = lwh[1]
    h = lwh[2]
    total_area += get_cube_total(l,w,h)
    ribbon_needed += get_bow_length(l,w,h)

print(total_area)
print(ribbon_needed)