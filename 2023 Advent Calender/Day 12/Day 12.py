from itertools import product, cycle

Day_12 = "Hot Springs"


def file_to_list():
    return_list = []
    #data = open("./2023 Advent Calender/Day 12/data.txt")
    data = open("./2023 Advent Calender/Day 12/test.txt")
    for line in data:
        clean_data = filter(None,line.split("\n"))
        return_list += clean_data

    return return_list


data = file_to_list()

def replace_question_marks_recursive(line, index, replacements, current_pattern, target_numbers):
    if index == len(line):
        # Check if the current pattern matches the target numbers
        if check_pattern_match(current_pattern, target_numbers):
            print(f"Pattern {current_pattern} matches target numbers.")
        return

    if line[index] == '?':
        # Replace the current '?' with each possible replacement
        for replacement in replacements:
            # Create a new pattern with the current replacement
            new_pattern = current_pattern[:index] + replacement + current_pattern[index+1:]
            replace_question_marks_recursive(line, index + 1, replacements, new_pattern, target_numbers)
    else:
        # If the character is not '?', move to the next position
        replace_question_marks_recursive(line, index + 1, replacements, current_pattern, target_numbers)

def check_pattern_match(pattern, numbers):
    pattern_numbers = [sum(1 for char in row if char == '#') for row in pattern]
    return pattern_numbers == numbers

def find_all_permutations(top_line, target_numbers):
    #target_numbers = target_numbers.replace(","," ").split()
    #target_numbers = [int(num) for num in target_numbers]
    replacements = ['.', '#']
    replace_question_marks_recursive(top_line, 0, replacements, top_line, target_numbers)



# top_line = "?###????????"
# target_numbers = [3, 2, 1]
# find_all_permutations(top_line, target_numbers)

find_all_permutations("?###????????", [3, 2, 1])



#for l in data:
    #l = l.split()
    #find_all_permutations(l[0], l[1])




            