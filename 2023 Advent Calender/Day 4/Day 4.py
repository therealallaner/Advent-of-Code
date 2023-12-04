
Day_4 = ""

card_values = []

def file_to_list():
    return_list = []
    data = open("./2023 Advent Calender/Day 4/data.txt")
    #data = open("./2023 Advent Calender/Day 4/test.txt")
    for line in data:
        clean_data = filter(None,line.lower().split("\n"))
        return_list += clean_data

    return return_list


data = file_to_list()


def card_comp(win, elf):

    match_num = []
    card_value = 1

    for item in win:
        if item in elf:
            match_num.append(item)

    x = len(match_num)

    if x > 0:
        card_value = 1

        while x > 1:
            card_value *= 2
            x -= 1

    else:
        card_value = 0

    return card_value



# Read list of winning numbers
# Read list of scratch numbers
# Calc card value
# Sum cards

for line in data:
    line = line.split()
    win_num = []
    elf_num = []

    for i, x in enumerate(line):

        if i >= 2 and i <= 11:
            win_num.append(x)

        if i >= 13 and i <= 37:
            elf_num.append(x)



    card_values.append(card_comp(win_num, elf_num))
    
print("Part 1 =", sum(card_values))

# Part 2

# You dont earn points per match but copies of subsequent cards per match
# I need to be able to "store" future cards as copies
# And then I need to count the number of cards i end with

card_copies = {}


def card_comp2(win, elf):

    match_num = []

    for item in win:
        if item in elf:
            match_num.append(item)

    return len(match_num)


for line in data:
    line = line.replace(":","").split()
    card_num = line[1]

    card_copies[card_num] = 1


for line in data:
    line = line.replace(":","").split()
    card_num = line[1]
    win_num = []
    elf_num = []
    
    for i, x in enumerate(line):

        #Real needs to change to <= 11
        if i >= 2 and i <= 11:
            win_num.append(x)

        #Real needs to change to >= 13 and <= 37
        if i >= 13 and i <= 37:
            elf_num.append(x)


    r = card_comp2(win_num,elf_num)
    cc = card_copies[card_num]
    c = 0

    while r > 0:
        #print(r)

        c += 1

        if int(card_num)+c < 203:
            card_copies[str(int(card_num)+c)] += cc
        
        #if int(card_num)+c < 11:
        #    card_copies[str(int(card_num)+c)] += cc


        r -= 1


print("Part 2 =", sum(card_copies.values()))
#print(card_copies)