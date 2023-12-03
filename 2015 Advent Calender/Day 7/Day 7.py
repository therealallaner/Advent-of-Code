
wires = {}
turned_on = {}
data_lines = []
times_run = 0

def file_to_list():
    return_list = []
    data = open("./2015 Advent Calender/Day 7/data.txt")
    #data = open("./2015 Advent Calender/Day 7/test.txt")
    for line in data:
        clean_data = filter(None,line.lower().split())
        return_list += clean_data

    return return_list

Data = file_to_list()

for char in "abcdefghijklmnopqrstuvwxyz":
    wires[char] = 0
    turned_on[char] = False
    for char_2 in "abcdefghijklmnopqrstuvwxyz":
        wires[f"{char}{char_2}"] = 0
        turned_on[f"{char}{char_2}"] = False

def bit_and(line):
    
    #line = line.split()

    if line[0].isnumeric():
        line[0] = int(line[0])
        if line[0] > 0:
            if turned_on[line[2]]:
                wires[line[-1]] = int(line[0]) & wires[line[2]]
                turned_on[line[-1]] = True
                line = ' '.join(map(str, line))
                data_lines.append(line)
                #print(data_lines)

    else:
        if turned_on[line[0]]:
            if turned_on[line[2]]:
                wires[line[-1]] = int(wires[line[0]] & wires[line[2]])
                turned_on[line[-1]] = True
                line = ' '.join(map(str, line))
                data_lines.append(line)
        #print(data_lines)


def bit_not(line):
    #line = line.split()
    return_string = wires[line[1]]
    if turned_on[line[1]]:
        wires[line[-1]] = int("0b1111111111111111", 2) - return_string
        turned_on[line[-1]] = True
        
        line = ' '.join(map(str, line))
        data_lines.append(line)
        #print(data_lines)
    



def bit_or(line):
    #pass
    #line = line.split()
    #print(line)
    #print("1", wires[line[-1]])
    if turned_on[line[0]] and turned_on[line[0]]:
        wires[line[-1]] = wires[line[0]] | wires[line[2]]
        turned_on[line[-1]] = True
        line = ' '.join(map(str, line))
        data_lines.append(line)
        if wires[line[-1]] == 0:
            print(wires[line[-1]])
        #print(data_lines)
    #print("2", wires[line[-1]])


def bit_rshift(line):
    character_count = 0
    #print(line)
    #line = line.split()
    binary = bin(wires[line[0]])
    shift_times = int(line[2])
    #print(binary)
    if turned_on[line[0]]:
        for char in binary:
            character_count += 1
        while character_count < 18:
            binary = binary[:2] + "0" + binary[2:]
            #print(binary)
            character_count += 1
        #print(line[2])
        #wires[line[-1]] = binary >> 2
        #print(binary)
        while shift_times > 0:
            binary = binary[:2] + "0" + binary[2:]
            binary = binary[:-1]
            shift_times -= 1
        #print(binary)
        #print(len(binary))
        wires[line[-1]] = int(binary, 2)
        turned_on[line[-1]] = True
        line = ' '.join(map(str, line))
        data_lines.append(line)
        #print(data_lines)
        #print(bin(wires[line[-1]]))
        #print(int("0b000011101011101", 2) >> 2)


def bit_lshift(line):
    character_count = 0
    #print(line)
    #line = line.split()
    binary = bin(wires[line[0]])
    #print(binary)
    shift_times = int(line[2])
    if turned_on[line[0]]:
        for char in binary:
            character_count += 1
        while character_count < 18:
            binary = binary[:2] + "0" + binary[2:]
            #print(binary)
            character_count += 1
        #print(line[2])
        #wires[line[-1]] = binary >> 2
        #print("1", binary)
        while shift_times > 0:
            binary = binary + "0"
            binary = binary[:2] + binary[3:]
            shift_times -= 1
        #print("3", binary)
        #print(binary)
        #print(len(binary))
        wires[line[-1]] = int(binary, 2)
        turned_on[line[-1]] = True
        line = ' '.join(map(str, line))
        data_lines.append(line)
        if wires[line[-1]] == 0:
            print(wires[line[-1]], turned_on[line[-1]], line.split()[-1])
        #print(data_lines)
        #print(bin(wires[line[-1]]))
        #print(int("0b000011101011101", 2) >> 2)

def assign(line):
    #print(line)
    #line = line.split()
    #print(line)
    #print("1", wires[line[-1]])
    if line[0].isnumeric():
        line[0] = int(line[0])
        if line[0] > 0:
            #print(line)
            wires[line[-1]] = int(line[0])
            turned_on[line[-1]] = True
            line = ' '.join(map(str, line))
            data_lines.append(line)
            #print(data_lines)
            #print(line[0])
    else:
        if turned_on[line[0]]:
            wires[line[-1]] = wires[line[0]]
            turned_on[line[-1]] = True
            line = ' '.join(map(str, line))
            data_lines.append(line)
        #print(data_lines)
            #print(wires[line[0]])
    #print("2", wires[line[-1]])
        
    #print("1", wires[line[-1]])
    #print(wires[line[0]])
    #wires[line[-1]] = wires[line[0]]
    #print("2", wires[line[-1]])

    #print(len(data_lines), data_lines)

#while not turned_on["lx"]:
while len(data_lines) < 305:
    times_run += 1
    line_count = 0
    for line in Data:
        line_count += 1
        #print(times_run, line_count, data_lines)
        #print(wires["a"])

        if line not in data_lines:
            
            line = line.split()
            #print(times_run, line_count, len(data_lines))

            #if "a" in line:
                #print(line)


            if "and" in line:
                bit_and(line)

            elif "not" in line:
                bit_not(line)

            elif "or" in line:
                bit_or(line)

            elif "rshift" in line:
                bit_rshift(line)

            elif "lshift" in line:
                bit_lshift(line)

            else:
                #print(line)
                assign(line)

#print(bin(65412))
#print(int("0b1111111110000100", 2))
for char in "defghixyacb":
    print(f"{char} = {wires[char]}", turned_on[char])
print("lx =", wires["lx"], turned_on["lx"])
print("lv =", wires["lv"], turned_on["lv"])
print("lu =", wires["lu"], turned_on["lu"])
print(len(data_lines))
print(data_lines[-1])

#for var_name, var_value in wires.items():
        #print(var_name, "=", var_value, turned_on[var_name])