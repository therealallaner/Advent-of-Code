import re
numbers = []
total = 0 

word_to_digit = {
    'nine' : '9',
    'eight' : '8',
    'seven' : '7',
    'six' : '6',
    'five' : '5',
    'four' : '4',
    'three' : '3',
    'two' : '2',
    'one' : '1',
    'nin' : "9",
    "eigh" : "8",
    "seve" : "7",
    "si" : "6",
    "fiv" : "5",
    "fou" : "4",
    "thre" : "3",
    "tw" : "2",
    "on" : "1",
    'ine' : "9",
    "ight" : "8",
    "even" : "7",
    "ix" : "6",
    "ive" : "5",
    "our" : "4",
    "hree" : "3",
    "wo" : "2",
    "ne" : "1",
}

def file_to_list():
    return_list = []
    data = open("./2023 Advent Calender/Day 1/data.txt")
    #data = open("./2023 Advent Calender/Day 1/test.txt")
    #data = open("./2023 Advent Calender/Day 1/matt.txt")
    for line in data:
        clean_data = filter(None,line.lower().split("\n"))
        return_list += clean_data

    return return_list


data = file_to_list()


for line in data:
    for word, index in word_to_digit.items():
        if word in line:
            line = line.replace(word, index)

        


    line = re.sub('\D', '',line)
    if (len(line) == 1):
         numbers.append(int(str(line[0]) + str(line[-1])))
         continue
       
    numbers.append(int(str(line[0]) + str(line[-1])))
 

for num in numbers:
    num = int(num)
    total += num


print(total)    