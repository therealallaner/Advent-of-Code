from itertools import permutations

Day_13 = "Knights of the Dinner Table"

total_happiness = 0
happiness_list = []
guests = []
function_counter = 0

def file_to_list():
    return_list = []
    data = open("./2015 Advent Calender/Day 13/data.txt")
    #data = open("./2015 Advent Calender/Day 13/test.txt")
    for line in data:
        clean_data = filter(None,line.lower().replace(".","").split("\n"))
        return_list += clean_data

    return return_list

data = file_to_list()

def happy_meter():

    happiness = 0
    guest = 0
    for item in guests:
        first_seat = False
        second_seat = False

        for line in data:
            line = line.split()

            if guests[guest] == guests[0]:
                if guests[guest] == line[0]:
                    if guests[guest+1] == line[-1]:
                        if "gain" in line:
                            happiness += int(line[3])
                            first_seat = True
                        if "lose" in line:
                            print("loser")
                            happiness -= int(line[3])
                            first_seat = True
                
                    if guests[-1] == line[-1]:
                        if "gain" in line:
                            happiness += int(line[3])
                            second_seat = True
                        if "lose" in line:
                            print("loser")
                            happiness -= int(line[3])
                            second_seat = True
                        
                    if first_seat and second_seat:
                        guest += 1

            elif guests[guest] == guests[-1]:
                if guests[guest] == line[0]:
                    if guests[0] == line[-1]:
                        if "gain" in line:
                            happiness += int(line[3])
                            first_seat = True
                        if "lose" in line:
                            print("loser")
                            happiness -= int(line[3])
                            first_seat = True

                    if guests[guest-1] == line[-1]:
                        if "gain" in line:
                            happiness += int(line[3])
                            second_seat = True

                        if "lose" in line:
                            print("loser")
                            happiness -= int(line[3])
                            second_seat = True

                    if first_seat and second_seat:
                        guest += 1
                        return happiness

            elif guests[guest] == line[0]:
                if guests[guest+1] == line[-1]:
                    if "gain" in line:
                        happiness += int(line[3])
                        first_seat = True
                    if "lose" in line:
                        print("loser")
                        happiness -= int(line[3])
                        first_seat = True

                if guests[guest-1] == line[-1]:
                    if "gain" in line:
                        happiness += int(line[3])
                        second_seat = True

                    if "lose" in line:
                        print(guests[guest-1],line)
                        happiness -= int(line[3])
                        second_seat = True

                if first_seat and second_seat:
                    guest += 1
                    #print("Seats checked = ", seats_checked)


for line in data:
    line = line.split()

    if line[0] not in guests:
        guests.append(line[0])

    if line[-1] not in guests:
        guests.append(line[-1])
    

for perm_list in permutations(guests):
    happiness_list.append(happy_meter())
    #if happy_meter() >= 750:
    #    print(guests)
    function_counter += 1
    guests = perm_list

for line in happiness_list:
    if total_happiness == 0:
        total_happiness = line
    if int(line) >= int(total_happiness):
        total_happiness = line
        print(line)

