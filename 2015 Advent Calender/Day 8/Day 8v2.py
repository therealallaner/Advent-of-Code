
raw_data = 0
str_data = 0

encode_data = 0


with open('./2015 Advent Calender/Day 8/data.txt', 'r') as f:
    for line in f.readlines():
        raw_data += len(line.strip())
        str_data += len(eval(line))
        encode_data += 2
        for char in line.strip():
            encode_data += 1
            if char == '"':
                encode_data += 1
            if char == '\\':
                encode_data += 1

    


print("Part 1 =", raw_data - str_data)
print("Part 2 =", encode_data - raw_data)

