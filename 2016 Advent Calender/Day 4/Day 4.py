import re
from collections import Counter

Day_4 = "Security Through Obscurity"

sumIDs = 0

def file_to_list():
    return_list = []
    data = open("./2016 Advent Calender/Day 4/data.txt")
    #data = open("./2016 Advent Calender/Day 4/test.txt")
    for line in data:
        clean_data = filter(None,line.lower().split("\n"))
        return_list += clean_data

    return return_list


data = file_to_list()


def Compare_Codes(s,l):
    l = l.replace("[","").replace("]","")
    if s == l:
        return True

def Five_Most_Common(l):
    topFiveLetters = dict(Counter(l).most_common(5))
    return topFiveLetters

def Count_Letters(l):

    letterCounts = {}
    
    for char in "abcdefghijklmnopqrstuvwxyz":
        letterCounts[char] = 0

    for i in l[0]:
        for c in i:
            letterCounts[c] += 1

    f = Five_Most_Common(letterCounts)
    s = ""
    for i in f:
        s += f"{i}"


    return s

def Separate_Numbers_Alphabets(str):
    numbers = re.findall(r'[0-9]+', str)
    alphabets = re.findall(r'[a-zA-Z]+', str)
    return alphabets,numbers



for l in data:
    l = l.replace("["," [").split()
    x = Separate_Numbers_Alphabets(l[0])
    s = Count_Letters(x)
    if Compare_Codes(s,l[-1]):
        sumIDs += int(x[1][0])


print(f"Part 1 answer is {sumIDs}")


#   Part 2

shiftPattern = {}

def Shift_Char(c,n):
    n = int(n)
    base = ord('a')
    shiftedChar = chr((ord(c) - base + n) % 26 + base)
    return shiftedChar


def Shift_String(a,n):
    shiftedString = ""
    for c in a:
        shiftedString += Shift_Char(c,n)
    return shiftedString


def Decryption(x):
    a = x[0]
    n = x[1][0]

    shiftedString = " "
    for i in a:
        shiftedString += Shift_String(i,n)
        shiftedString += " "

    if "north" in shiftedString:
        print(f"{shiftedString} is room number {n}")


for l in data:
    l = l.replace("["," [").split()
    x = Separate_Numbers_Alphabets(l[0])
    Decryption(x)