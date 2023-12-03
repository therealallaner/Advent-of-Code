
Day_14 = "Reindeer Olympics"

deers = {}
turn_counter = {}
resting = {}
rest_counter = {}
points = {}

turn = 0

def file_to_list():
    return_list = []
    data = open("./2015 Advent Calender/Day 14/data.txt")
    #data = open("./2015 Advent Calender/Day 14/test.txt")
    for line in data:
        clean_data = filter(None,line.lower().split("\n"))
        return_list += clean_data

    return return_list


data = file_to_list()

def reindeer_turn():

    for line in data:
        line = line.split()

        deer = line[0]
        speed = int(line[3])
        turn = int(line[6])
        rest_time = int(line[-2])


        if not resting[deer]:
            deers[deer] += speed
            turn_counter[deer] -= 1
        else:
            rest_counter[deer] -= 1

        if not resting[deer]:
            if turn_counter[deer] == 0:
                resting[deer] = True
                rest_counter[deer] = rest_time
        if resting[deer]:
            if rest_counter[deer] == 0:
                resting[deer] = False
                turn_counter[deer] = turn





for line in data:
    line = line.split()
    deer = line[0]
    
    deers[deer] = 0
    resting[deer] = False
    turn_counter[deer] = int(line[6])
    rest_counter[deer] = 0
    points[deer] = 0


for _ in range(2503):
    reindeer_turn()
    points[max(deers, key=deers.get)] += 1

print(deers)
print(max(points.values()))
