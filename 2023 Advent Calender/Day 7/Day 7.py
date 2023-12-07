import re

Day_7 = "Camel Cards"

card_ranks = ['2', '3', '4', '5', '6', '7', '8', '9', 't', 'j', 'q', 'k', 'a']
five_kind = []
four_kind = []
full_house = []
three_kind = []
two_pair = []
one_pair = []
high_card = []


def file_to_list():
    return_list = []
    data = open("./2023 Advent Calender/Day 7/data.txt")
    #data = open("./2023 Advent Calender/Day 7/test.txt")
    for line in data:
        clean_data = filter(None,line.lower().split("\n"))
        return_list += clean_data

    return return_list


data = file_to_list()

# Rank 1 is the lowest rank



for hand in data:
    hand_matches = []
    char_list = []
    hand = hand.split()
    
    for char in hand[0]:
        if char not in char_list:
            char_list.append(char)
    
    for c in char_list:
        hand_matches.append(hand[0].count(c))

    matches = hand_matches
    
    if len(matches) == 5:
        high_card.append(hand)

    elif len(matches) == 4:
        one_pair.append(hand)

    elif len(matches) == 3:
        if matches.count(2) == 2:
            two_pair.append(hand)
        else:
            three_kind.append(hand)

    elif len(matches) == 2:
        if 3 in matches:
            full_house.append(hand)
        else:
            four_kind.append(hand)

    elif len(matches) == 1:
        five_kind.append(hand)



def hand_sorting_algorithm(hand_list):
    swaps = True
    while swaps:
        swaps = False

        for h, hand in enumerate(hand_list):
            if hand != hand_list[-1]:
                if card_ranks.index(hand[0][0]) > card_ranks.index(hand_list[h+1][0][0]):
                    hand_list[h], hand_list[h+1] = hand_list[h+1], hand_list[h]
                    swaps = True

                elif card_ranks.index(hand[0][0]) == card_ranks.index(hand_list[h+1][0][0]):
                    if card_ranks.index(hand[0][1]) > card_ranks.index(hand_list[h+1][0][1]):
                        hand_list[h], hand_list[h+1] = hand_list[h+1], hand_list[h]
                        swaps = True

                    elif card_ranks.index(hand[0][1]) == card_ranks.index(hand_list[h+1][0][1]):
                        if card_ranks.index(hand[0][2]) > card_ranks.index(hand_list[h+1][0][2]):
                            hand_list[h], hand_list[h+1] = hand_list[h+1], hand_list[h]
                            swaps = True

                        elif card_ranks.index(hand[0][2]) == card_ranks.index(hand_list[h+1][0][2]):
                            if card_ranks.index(hand[0][3]) > card_ranks.index(hand_list[h+1][0][3]):
                                hand_list[h], hand_list[h+1] = hand_list[h+1], hand_list[h]
                                swaps = True

                            elif card_ranks.index(hand[0][3]) == card_ranks.index(hand_list[h+1][0][3]):
                                if card_ranks.index(hand[0][4]) > card_ranks.index(hand_list[h+1][0][4]):
                                    hand_list[h], hand_list[h+1] = hand_list[h+1], hand_list[h]
                                    swaps = True

    return hand_list




answer = 0
rank = 1

for i in hand_sorting_algorithm(high_card):
    answer += rank * int(i[1])
    rank += 1

for i in hand_sorting_algorithm(one_pair):
    answer += rank * int(i[1])
    rank += 1

for i in hand_sorting_algorithm(two_pair):
    answer += rank * int(i[1])
    rank += 1
    
for i in hand_sorting_algorithm(three_kind):
    answer += rank * int(i[1])
    rank += 1
    
for i in hand_sorting_algorithm(full_house):
    answer += rank * int(i[1])
    rank += 1
    
for i in hand_sorting_algorithm(four_kind):
    answer += rank * int(i[1])
    rank += 1
    
for i in hand_sorting_algorithm(five_kind):
    answer += rank * int(i[1])
    rank += 1

print("Part 1 =", answer)


# Part 2


card_ranks = ['j', '2', '3', '4', '5', '6', '7', '8', '9', 't', 'q', 'k', 'a']
five_kind = []
four_kind = []
full_house = []
three_kind = []
two_pair = []
one_pair = []
high_card = []




for hand in data:
    hand_matches = []
    char_list = []
    jokers = []
    hand = hand.split()
    
    for char in hand[0]:
        if char != 'j':
            if char not in char_list:
                char_list.append(char)

        else:
            jokers.append(char)
    
    for c in char_list:
        hand_matches.append(int(hand[0].count(c)))


    matches = hand_matches

    matches.sort()

    if not matches:
        matches.append(5)
    elif jokers:
        matches[-1] = matches[-1] + len(jokers)

    
    if len(matches) == 5:
        high_card.append(hand)

    elif len(matches) == 4:
        one_pair.append(hand)

    elif len(matches) == 3:
        if matches.count(2) == 2:
            two_pair.append(hand)
        else:
            three_kind.append(hand)

    elif len(matches) == 2:
        if 3 in matches:
            full_house.append(hand)
        else:
            four_kind.append(hand)

    elif len(matches) == 1:
        five_kind.append(hand)


answer = 0
rank = 1

for i in hand_sorting_algorithm(high_card):
    answer += rank * int(i[1])
    rank += 1

for i in hand_sorting_algorithm(one_pair):
    answer += rank * int(i[1])
    rank += 1

for i in hand_sorting_algorithm(two_pair):
    answer += rank * int(i[1])
    rank += 1
    
for i in hand_sorting_algorithm(three_kind):
    answer += rank * int(i[1])
    rank += 1
    
for i in hand_sorting_algorithm(full_house):
    answer += rank * int(i[1])
    rank += 1
    
for i in hand_sorting_algorithm(four_kind):
    answer += rank * int(i[1])
    rank += 1
    
for i in hand_sorting_algorithm(five_kind):
    answer += rank * int(i[1])
    rank += 1

print("Part 2 =", answer)