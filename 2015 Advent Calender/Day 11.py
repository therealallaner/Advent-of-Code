import re

Day_11 = "Corporate Policy"

letters = "abcdefghijklmnopqrstuvwxyz"
two_ago = ""
one_ago = ""

letter_straights = []
let = {}
counter = 0
letter_ban = ['i', 'o', 'l']

old_password = "cqjxxyzz"
input = "cqjxjnds"
new_password = "cqjxxyzz"
password_is_acceptable = False

for i, char in enumerate(letters):
    if char != "z":
        let[char] = letters[i+1]
    else:
        let[char] = "a"

for char in letters:
    letter_straights.append(f"{two_ago}{one_ago}{char}")
    two_ago = one_ago
    one_ago = char

letter_straights = letter_straights[2:]

def check_pairs(string):
    char_overlap = ""
    char_zero = ""
    pair_count = 0

    for char in string:
        if char != char_overlap:
            if char == char_zero:
                pair_count += 1
        char_overlap = char_zero
        char_zero = char

    if pair_count >= 2:
        return True
    
def check_straight(string):
    for line in letter_straights:
        if line in string:
            return True

def increment_password(line):
    return_string = []
    temp_list = []
    for char in reversed(line):
        temp_list.append(char)
    
    temp_list[0] = let[temp_list[0]]
    if temp_list[0] == "a":
        temp_list[1] = let[temp_list[1]]
        if temp_list[1] == "a":
            temp_list[2] = let[temp_list[2]]
            if temp_list[2] == "a":
                temp_list[3] = let[temp_list[3]]
                if temp_list[3] == "a":
                    temp_list[4] = let[temp_list[4]]
                    if temp_list[4] == "a":
                        temp_list[5] = let[temp_list[5]]
                        if temp_list[5] == "a":
                            temp_list[6] = let[temp_list[6]]
                            if temp_list[6] == "a":
                                temp_list[7] = let[temp_list[7]]


    return_string = ''.join(map(str, reversed(temp_list)))
    return return_string


while not password_is_acceptable:
#for _ in range(100000000):
    counter += 1
    old_password = increment_password(old_password)
    has_ban_letter = False
    has_pairs = False
    for ban in letter_ban:
        if ban in old_password:
            has_ban_letter = True
            #print(test_case, has_ban_letter)
    if not has_ban_letter:
        #print(test_case, has_ban_letter)
        if check_pairs(old_password):
            has_pairs = True
    if has_pairs:
        if check_straight(old_password):
            print(counter, old_password)
            #if "aj" in old_password:
            password_is_acceptable = True
                #print(counter, old_password, "New Password Maker?")
