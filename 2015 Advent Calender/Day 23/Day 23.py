Day_23 = "Opening the Turing Lock"

input = {}
registers = {}
registers["a"] = 1
registers["b"] = 0

solved = False

def file_to_list():
    return_list = []
    data = open("./2015 Advent Calender/Day 23/data.txt")
    #data = open("./2015 Advent Calender/Day 23/test.txt")
    for line in data:
        clean_data = filter(None,line.lower().replace(",","").split("\n"))
        return_list += clean_data

    return return_list

data = file_to_list()


def read_input(data):
    turn = 0
    solved = False
    while not solved:

        line = data[turn].replace("+","").split()
        print((turn+1), registers, line)
        
        if "inc" in line:
            registers[line[1]] += 1
            turn += 1
            
            if turn > 45:
                solved = True

        if "hlf" in line:
            registers[line[1]] = int(registers[line[1]] / 2)

            turn += 1
            
            if turn > 45:
                solved = True

        if "tpl" in line:
            registers[line[1]] *= 3
            turn += 1

            if turn > 45:
                solved = True

        if "jio" in line:
            if registers[line[1]] == 1:
                turn += int(line[-1])
            else:
                turn += 1

            if turn > 45:
                solved = True

        if "jie" in line:
            if not registers[line[1]] & 1:
                turn += int(line[-1])
            else:
                turn += 1

            if turn > 45:
                solved = True

        if "jmp" in line:
            turn += int(line[-1])

            if turn > 45:
                solved = True


for i, line in enumerate(data):
    input[i] = line

read_input(input)

#for line in input:
#    print(line, input[line])