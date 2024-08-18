from utils.decorators import time_it
from utils.mymethods import Data_to_List
import random


Day_12 = "Leonardo's Monorail"


data = Data_to_List(2016,12,"data")


instruction = 0

register = {
    "a":0,
    "b":0,
    "c":1,
    "d":0
}

while instruction < len(data):
    l = data[instruction]
    l = l.split()

    if "cpy" in l:
        r = l[-1]
        c = l[1]
        if c.isnumeric():
            register[r] = int(c)
        else:
            register[r] = register[c]
        instruction += 1

    elif "inc" in l:
        r = l[-1]
        register[r] += 1
        instruction += 1

    elif "dec" in l:
        r = l[-1]
        register[r] -= 1
        instruction += 1

    elif "jnz" in l:
        r = l[1]
        i = l[-1]

        if r.isnumeric():
            if int(r) > 0:
                instruction += int(i)
            else:
                instruction += 1
        else:
            if register[r] > 0:
                instruction += int(i)
            else:
                instruction += 1

#    print(f'Register A at instruction {instruction}: {register['a']}')


print(register)