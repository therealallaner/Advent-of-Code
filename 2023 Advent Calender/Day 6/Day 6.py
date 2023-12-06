
Day_6 = "Wait For It"


def file_to_list():
    return_list = []
    data = open("./2023 Advent Calender/Day 6/data.txt")
    #data = open("./2023 Advent Calender/Day 6/test.txt")
    for line in data:
        clean_data = filter(None,line.lower().split("\n"))
        return_list += clean_data

    return return_list


data = file_to_list()

# For part 1 I need to...
    # Find number of different ways I can beat the record
    # Multiple them together to get the answer

def get_times(data):
    times = []
    for line in data:
        line = line.split()

        for item in line:
            if item.isnumeric():
                if int(item) < 100:
                    times.append(item)

        return times
    

def get_distances(data):
    distances = []

    for l, line in enumerate(data):
        if l == 1:
            line = line.split()

            for item in line:
                if item.isnumeric():
                    if int(item) < 10000:
                        distances.append(item)

    return distances

def time_dist(data):
    time = get_times(data)
    dist = get_distances(data)
    records = {}

    for i, item in enumerate(time):
        records[item] = dist[i]

    return records


def find_better_times(data):
    records = time_dist(data)
    better_times = []

    for item in records:
        p = []
        b = []
        time = int(item)
        t = int(item)
        distance = int(records[item])

        while time > 0:
            p.append((t-time)*time)
            time -= 1
        
        for i in p:
            if i > distance:
                b.append(i)

        better_times.append(len(b))


    return better_times


def products(data):
    better = find_better_times(data)
    product = 1

    for num in better:
        product *= num

    return product


product = products(data)


print("Part 1 =", product)


# Part 2
# For Part 2 I may need to make it way more efficient since the number is so large!


def get_times2(data):
    times = []
    for line in data:
        line = line.split()

        for item in line:
            if item.isnumeric():
                if int(item) > 100:
                    times.append(item)

        return times
    

def get_distances2(data):
    distances = []

    for l, line in enumerate(data):
        if l == 1:
            line = line.split()

            for item in line:
                if item.isnumeric():
                    if int(item) > 10000:
                        distances.append(item)

    return distances

def time_dist(data):
    time = get_times2(data)
    dist = get_distances2(data)
    records = {}

    for i, item in enumerate(time):
        records[item] = dist[i]

    return records


def find_better_times2(data):
    records = time_dist(data)
    p = 0

    for item in records:
        time = int(item)/2 + .5
        t = int(item)
        distance = int(records[item])

        while ((t-time)*time) > distance:
            p += 1
            time += 1


        time = int(item)/2 - .5
        while ((t-time)*time) > distance:
            p += 1
            time -= 1

    return p

print("Part 2 =", find_better_times2(data))