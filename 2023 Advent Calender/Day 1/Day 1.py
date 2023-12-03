
Day_1 = "Trebuchet?"

total_list = []
part_2 = []
try_3 = []
try_4 = []

line_count = 0

def file_to_list():
    return_list = []
    #data = open("./2023 Advent Calender/Day 1/data.txt")
    #data = open("./2023 Advent Calender/Day 1/test.txt")
    data = open("./2023 Advent Calender/Day 1/matt.txt")
    for line in data:
        clean_data = filter(None,line.lower().split("\n"))
        return_list += clean_data

    return return_list


data = file_to_list()

for line in data:
    line_list = []
    for char in line:
        if char.isnumeric():
            line_list.append(char)
    if line_list:
        total_list.append(int(f"{line_list[0]}{line_list[-1]}"))


print("Part 1 =", sum(total_list)) #Matt number should be 53334

# Part 2 (NOTHING I DID FOR PART 2 WORKED!)

for line in data:
    line_count += 1
    line_list = []
    #print(line_count, line)

    for i, char in enumerate(line):

        if "one" in line[:i]:
            line = line.replace("one", "1", 1)
            i -= 3

        if "two" in line[:i]:
            line = line.replace("two", "2", 1)
            i -= 3
    
        if "three" in line[:i]:
            line = line.replace("three", "3", 1)
            i -= 5
    
        if "four" in line[:i]:
            line = line.replace("four", "4", 1)
            i -= 4
    
        if "five" in line[:i]:
            line = line.replace("five", "5", 1)
            i -= 4
    
        if "six" in line[:i]:
            line = line.replace("six", "6", 1)
            i -= 3

        if "seven" in line[:i]:
            line = line.replace("seven", "7", 1)
            i -= 5
    
        if "eight" in line[:i]:
            line = line.replace("eight", "8", 1)
            i -= 5
    
        if "nine" in line[:i]:
            line = line.replace("nine", "9", 1)
            i -= 4


    for char in line:
        if char.isnumeric():
            line_list.append(char)

    if line_list:
        part_2.append(int(f"{line_list[0]}{line_list[-1]}"))


print("Part 2 =", sum(part_2)) # Matt number should be 52834 

for line in data:
    line_count += 1
    line_list = []
    new_line = ""
    #print(line_count, line)

    for i, char in enumerate(line):

        if "one" in line[:i]:
            line = line.replace("one", "e", 1)
            new_line += "1"

        if "two" in line[:i]:
            line = line.replace("two", "o", 1)
            new_line += "2"
    
        if "three" in line[:i]:
            line = line.replace("three", "e", 1)
            new_line += "3"
    
        if "four" in line[:i]:
            line = line.replace("four", "r", 1)
            new_line += "4"
    
        if "five" in line[:i]:
            line = line.replace("five", "e", 1)
            new_line += "5"
    
        if "six" in line[:i]:
            line = line.replace("six", "x", 1)
            new_line += "6"

        if "seven" in line[:i]:
            line = line.replace("seven", "n", 1)
            new_line += "7"
    
        if "eight" in line[:i]:
            line = line.replace("eight", "t", 1)
            new_line += "8"
    
        if "nine" in line[:i]:
            line = line.replace("nine", "e", 1)
            new_line += "9"

        if char.isnumeric():
            new_line += char
    
    for char in new_line:
        if char.isnumeric():
            line_list.append(char)

    if line_list:
        try_3.append(int(f"{line_list[0]}{line_list[-1]}"))


print("Try 3 =", sum(try_3))

print("For Matt's part 2 I need to get 52834")

for line in data:
    line_list = []
    first_number = False
    second_number = False

    for i, char in enumerate(line):
        if not first_number:

            if "one" in line[:i] and not first_number:
                line_list.append(1)
                first_number = True
        
            if "two" in line[:i] and not first_number:
                line_list.append(2)
                first_number = True
        
            if "three" in line[:i] and not first_number:
                line_list.append(3)
                first_number = True
        
            if "four" in line[:i] and not first_number:
                line_list.append(4)
                first_number = True
        
            if "five" in line[:i] and not first_number:
                line_list.append(5)
                first_number = True
        
            if "six" in line[:i] and not first_number:
                line_list.append(6)
                first_number = True
        
            if "seven" in line[:i] and not first_number:
                line_list.append(7)
                first_number = True
        
            if "eight" in line[:i] and not first_number:
                line_list.append(8)
                first_number = True
        
            if "nine" in line[:i] and not first_number:
                line_list.append(9)
                first_number = True

            if char.isnumeric() and not first_number:
                line_list.append(char)
                second_number = True
        
    if first_number:
        #print(line)
        r_line = ''.join(list(reversed(line)))
        #print(r_line)

        for i, char in enumerate(r_line):
            if not second_number:

                if "eno" in r_line[:i] and not second_number:
                    line_list.append(1)
                    second_number = True
        
                if "owt" in r_line[:i] and not second_number:
                    line_list.append(2)
                    second_number = True
        
                if "eerht" in r_line[:i] and not second_number:
                    line_list.append(3)
                    second_number = True
        
                if "ruof" in r_line[:i] and not second_number:
                    line_list.append(4)
                    second_number = True
        
                if "evif" in r_line[:i] and not second_number:
                    line_list.append(5)
                    second_number = True
        
                if "xis" in r_line[:i] and not second_number:
                    line_list.append(6)
                    second_number = True
        
                if "neves" in r_line[:i] and not second_number:
                    line_list.append(7)
                    second_number = True
        
                if "thgie" in r_line[:i] and not second_number:
                    line_list.append(8)
                    second_number = True
        
                if "enin" in r_line[:i] and not second_number:
                    line_list.append(9)
                    second_number = True

                if char.isnumeric() and not second_number:
                    line_list.append(char)
                    second_number = True
    
    if len(line_list) >= 3:
        pass
        #print(line)
        #print(r_line)
        #print(line_list)

    if line_list:
        try_4.append(int(f"{line_list[0]}{line_list[-1]}"))

print("Try 4 =", sum(try_4))

