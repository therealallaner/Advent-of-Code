Day_20 = "Infinite Elves and Infinite Houses"

number_found = False
target_number = 33100000
house_num = 0
part_1 = 776160
part_2 = 786240
elves = {}


def find_divisors(number):
    divisors = set()
    for i in range(1, int(number**0.5) + 1):
        if number % i == 0:
            if elves[i] < 50:
                divisors.add(i*11)
                elves[i] += 1
            if elves[number // i] < 50:
                divisors.add((number // i)*11)
                elves[number // i] += 1
    return divisors


def deliver_presents(house):
    div = find_divisors(house)
    presents = sum(div)
    return presents >= target_number
    
    
while not number_found:
    house_num += 1
    elves[house_num] = 0
    if deliver_presents(house_num):
        number_found = True
        print(house_num)

