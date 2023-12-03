import re

vowel_counter = 0
nice_counter = 0
previouschar = ""
two_char_ago = ""
doubles = 0
line_count = 0
every_other_repeat = False
new_nice_counter = 0
char_pair = ""


def file_to_list():
    return_list = []
    data = open("./2015 Advent Calender/Day 5/data.txt")
    #data = open("./2015 Advent Calender/Day 5/test.txt")
    for line in data:
        clean_data = line.lower().split()
        return_list += clean_data

    return return_list


data = file_to_list()


def char_pairs(string):
    string = re.findall('.{1,2}', string)
    
    for pair in string:
        if string.count(pair) >= 2:
            return True
    return False

def check_pair(string):
    char_zero = ""
    pair_list = []

    for char in string:
        pair = f"{char_zero},{char}"
        if pair not in pair_list:
            pair_list.append(f"{char_zero},{char}")
        elif pair == pair_list[-1]:
            pair_list.append(f"0,{char}")
            print(pair_list[-2], pair_list[-1])
        else:
            print(new_nice_counter, line_count, pair_list)
            return True

        char_zero = char



def check_pair_test(string):
    char_zero = ""
    pair_list = []

    for char in string:
        pair = f"{char_zero},{char}"
        if pair not in pair_list:
            pair_list.append(f"{char_zero},{char}")
        elif pair == pair_list[-1]:
            pair_list.append(f"0,{char}")
            print(pair_list[-2], pair_list[-1])
        else:
            print(new_nice_counter, line_count, pair_list)
            return True

        char_zero = char
        

#for line in data:
#    line_count += 1
#
#    if "ab" in line:
#        print("Had ab")
#        continue
#    if "cd" in line:
#        print("Had cd")
#        continue
#    if "pq" in line:
#        print("Had pq")
#        continue
#    if "xy" in line:
#        print("Had xy")
#        continue
#
#    for char in line:
#        if char == previouschar:
#            doubles += 1
#        previouschar = char

#   if doubles >= 1:
#       for char in line:
#           if char == "a":
#               vowel_counter += 1
#            if char == "e":
#                vowel_counter += 1
#            if char == "i":
#                vowel_counter += 1
#            if char == "o":
#                vowel_counter += 1
#            if char == "u":
#                vowel_counter += 1
#
#    if vowel_counter >= 3:
#        print(line_count , line, True)
#        doubles = 0
#        previouschar = ""
#        vowel_counter = 0
#        nice_counter += 1
#    else:
#        doubles = 0
#        previouschar = ""
#        vowel_counter = 0
#        print(line_count, line)

#print(nice_counter)

for line in data:
    line_count += 1
             
    for char in line:
        
        #This is supposed to check if you have a letter that matched a letter two spaces away, with exactly one character in between
        if char == two_char_ago:
            every_other_repeat = True
        two_char_ago = previouschar
        previouschar = char

    #print(line_count, line, every_other_repeat)



    if every_other_repeat:
        #if the above boolean is true, this is supposed to check if there is a copy of any pair of letters within a single line
        if check_pair(line):
            new_nice_counter += 1
        

    previouschar = ""
    two_char_ago = ""
    every_other_repeat = False
    doubles = 0



#check_pair_test("xxywiogwairvaaaaa")

print(new_nice_counter)