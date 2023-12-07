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


swaps = True
while swaps:
    swaps = False
    for h, hand in enumerate(high_card):
        if hand != high_card[-1]:
            if card_ranks.index(hand[0][0]) > card_ranks.index(high_card[h+1][0][0]):
                high_card[h], high_card[h+1] = high_card[h+1], high_card[h]
                swaps = True

            elif card_ranks.index(hand[0][0]) == card_ranks.index(high_card[h+1][0][0]):
                if card_ranks.index(hand[0][1]) > card_ranks.index(high_card[h+1][0][1]):
                    high_card[h], high_card[h+1] = high_card[h+1], high_card[h]
                    swaps = True

                elif card_ranks.index(hand[0][1]) == card_ranks.index(high_card[h+1][0][1]):
                    if card_ranks.index(hand[0][2]) > card_ranks.index(high_card[h+1][0][2]):
                        high_card[h], high_card[h+1] = high_card[h+1], high_card[h]
                        swaps = True

                    elif card_ranks.index(hand[0][2]) == card_ranks.index(high_card[h+1][0][2]):
                        if card_ranks.index(hand[0][3]) > card_ranks.index(high_card[h+1][0][3]):
                            high_card[h], high_card[h+1] = high_card[h+1], high_card[h]
                            swaps = True

                        elif card_ranks.index(hand[0][3]) == card_ranks.index(high_card[h+1][0][3]):
                            if card_ranks.index(hand[0][4]) > card_ranks.index(high_card[h+1][0][4]):
                                high_card[h], high_card[h+1] = high_card[h+1], high_card[h]
                                swaps = True

print("High Cards done")

swaps = True
while swaps:
    swaps = False
    for h, hand in enumerate(one_pair):
        if hand != one_pair[-1]:
            if card_ranks.index(hand[0][0]) > card_ranks.index(one_pair[h+1][0][0]):
                one_pair[h], one_pair[h+1] = one_pair[h+1], one_pair[h]
                swaps = True

            elif card_ranks.index(hand[0][0]) == card_ranks.index(one_pair[h+1][0][0]):
                if card_ranks.index(hand[0][1]) > card_ranks.index(one_pair[h+1][0][1]):
                    one_pair[h], one_pair[h+1] = one_pair[h+1], one_pair[h]
                    swaps = True

                elif card_ranks.index(hand[0][1]) == card_ranks.index(one_pair[h+1][0][1]):
                    if card_ranks.index(hand[0][2]) > card_ranks.index(one_pair[h+1][0][2]):
                        one_pair[h], one_pair[h+1] = one_pair[h+1], one_pair[h]
                        swaps = True

                    elif card_ranks.index(hand[0][2]) == card_ranks.index(one_pair[h+1][0][2]):
                        if card_ranks.index(hand[0][3]) > card_ranks.index(one_pair[h+1][0][3]):
                            one_pair[h], one_pair[h+1] = one_pair[h+1], one_pair[h]
                            swaps = True

                        elif card_ranks.index(hand[0][3]) == card_ranks.index(one_pair[h+1][0][3]):
                            if card_ranks.index(hand[0][4]) > card_ranks.index(one_pair[h+1][0][4]):
                                one_pair[h], one_pair[h+1] = one_pair[h+1], one_pair[h]
                                swaps = True

print("Single Pairs done")

swaps = True
while swaps:
    swaps = False
    for h, hand in enumerate(two_pair):
        if hand != two_pair[-1]:
            if card_ranks.index(hand[0][0]) > card_ranks.index(two_pair[h+1][0][0]):
                two_pair[h], two_pair[h+1] = two_pair[h+1], two_pair[h]
                swaps = True

            elif card_ranks.index(hand[0][0]) == card_ranks.index(two_pair[h+1][0][0]):
                if card_ranks.index(hand[0][1]) > card_ranks.index(two_pair[h+1][0][1]):
                    two_pair[h], two_pair[h+1] = two_pair[h+1], two_pair[h]
                    swaps = True

                elif card_ranks.index(hand[0][1]) == card_ranks.index(two_pair[h+1][0][1]):
                    if card_ranks.index(hand[0][2]) > card_ranks.index(two_pair[h+1][0][2]):
                        two_pair[h], two_pair[h+1] = two_pair[h+1], two_pair[h]
                        swaps = True

                    elif card_ranks.index(hand[0][2]) == card_ranks.index(two_pair[h+1][0][2]):
                        if card_ranks.index(hand[0][3]) > card_ranks.index(two_pair[h+1][0][3]):
                            two_pair[h], two_pair[h+1] = two_pair[h+1], two_pair[h]
                            swaps = True

                        elif card_ranks.index(hand[0][3]) == card_ranks.index(two_pair[h+1][0][3]):
                            if card_ranks.index(hand[0][4]) > card_ranks.index(two_pair[h+1][0][4]):
                                two_pair[h], two_pair[h+1] = two_pair[h+1], two_pair[h]
                                swaps = True

print("Two Pairs done")

swaps = True
while swaps:
    swaps = False
    for h, hand in enumerate(three_kind):
        if hand != three_kind[-1]:
            if card_ranks.index(hand[0][0]) > card_ranks.index(three_kind[h+1][0][0]):
                three_kind[h], three_kind[h+1] = three_kind[h+1], three_kind[h]
                swaps = True

            elif card_ranks.index(hand[0][0]) == card_ranks.index(three_kind[h+1][0][0]):
                if card_ranks.index(hand[0][1]) > card_ranks.index(three_kind[h+1][0][1]):
                    three_kind[h], three_kind[h+1] = three_kind[h+1], three_kind[h]
                    swaps = True

                elif card_ranks.index(hand[0][1]) == card_ranks.index(three_kind[h+1][0][1]):
                    if card_ranks.index(hand[0][2]) > card_ranks.index(three_kind[h+1][0][2]):
                        three_kind[h], three_kind[h+1] = three_kind[h+1], three_kind[h]
                        swaps = True

                    elif card_ranks.index(hand[0][2]) == card_ranks.index(three_kind[h+1][0][2]):
                        if card_ranks.index(hand[0][3]) > card_ranks.index(three_kind[h+1][0][3]):
                            three_kind[h], three_kind[h+1] = three_kind[h+1], three_kind[h]
                            swaps = True

                        elif card_ranks.index(hand[0][3]) == card_ranks.index(three_kind[h+1][0][3]):
                            if card_ranks.index(hand[0][4]) > card_ranks.index(three_kind[h+1][0][4]):
                                three_kind[h], three_kind[h+1] = three_kind[h+1], three_kind[h]
                                swaps = True


print("Three of a kind done")

swaps = True
while swaps:
    swaps = False
    for h, hand in enumerate(full_house):
        if hand != full_house[-1]:
            if card_ranks.index(hand[0][0]) > card_ranks.index(full_house[h+1][0][0]):
                full_house[h], full_house[h+1] = full_house[h+1], full_house[h]
                swaps = True

            elif card_ranks.index(hand[0][0]) == card_ranks.index(full_house[h+1][0][0]):
                if card_ranks.index(hand[0][1]) > card_ranks.index(full_house[h+1][0][1]):
                    full_house[h], full_house[h+1] = full_house[h+1], full_house[h]
                    swaps = True

                elif card_ranks.index(hand[0][1]) == card_ranks.index(full_house[h+1][0][1]):
                    if card_ranks.index(hand[0][2]) > card_ranks.index(full_house[h+1][0][2]):
                        full_house[h], full_house[h+1] = full_house[h+1], full_house[h]
                        swaps = True

                    elif card_ranks.index(hand[0][2]) == card_ranks.index(full_house[h+1][0][2]):
                        if card_ranks.index(hand[0][3]) > card_ranks.index(full_house[h+1][0][3]):
                            full_house[h], full_house[h+1] = full_house[h+1], full_house[h]
                            swaps = True

                        elif card_ranks.index(hand[0][3]) == card_ranks.index(full_house[h+1][0][3]):
                            if card_ranks.index(hand[0][4]) > card_ranks.index(full_house[h+1][0][4]):
                                full_house[h], full_house[h+1] = full_house[h+1], full_house[h]
                                swaps = True


print("Full House done")

swaps = True
while swaps:
    swaps = False
    for h, hand in enumerate(four_kind):
        if hand != four_kind[-1]:
            if card_ranks.index(hand[0][0]) > card_ranks.index(four_kind[h+1][0][0]):
                four_kind[h], four_kind[h+1] = four_kind[h+1], four_kind[h]
                swaps = True

            elif card_ranks.index(hand[0][0]) == card_ranks.index(four_kind[h+1][0][0]):
                if card_ranks.index(hand[0][1]) > card_ranks.index(four_kind[h+1][0][1]):
                    four_kind[h], four_kind[h+1] = four_kind[h+1], four_kind[h]
                    swaps = True

                elif card_ranks.index(hand[0][1]) == card_ranks.index(four_kind[h+1][0][1]):
                    if card_ranks.index(hand[0][2]) > card_ranks.index(four_kind[h+1][0][2]):
                        four_kind[h], four_kind[h+1] = four_kind[h+1], four_kind[h]
                        swaps = True

                    elif card_ranks.index(hand[0][2]) == card_ranks.index(four_kind[h+1][0][2]):
                        if card_ranks.index(hand[0][3]) > card_ranks.index(four_kind[h+1][0][3]):
                            four_kind[h], four_kind[h+1] = four_kind[h+1], four_kind[h]
                            swaps = True

                        elif card_ranks.index(hand[0][3]) == card_ranks.index(four_kind[h+1][0][3]):
                            if card_ranks.index(hand[0][4]) > card_ranks.index(four_kind[h+1][0][4]):
                                four_kind[h], four_kind[h+1] = four_kind[h+1], four_kind[h]
                                swaps = True

print("Four of a kind done")

swaps = True
while swaps:
    swaps = False
    for h, hand in enumerate(five_kind):
        if hand != five_kind[-1]:
            if card_ranks.index(hand[0][0]) > card_ranks.index(five_kind[h+1][0][0]):
                five_kind[h], five_kind[h+1] = five_kind[h+1], five_kind[h]
                swaps = True

            elif card_ranks.index(hand[0][0]) == card_ranks.index(five_kind[h+1][0][0]):
                if card_ranks.index(hand[0][1]) > card_ranks.index(five_kind[h+1][0][1]):
                    five_kind[h], five_kind[h+1] = five_kind[h+1], five_kind[h]
                    swaps = True

                elif card_ranks.index(hand[0][1]) == card_ranks.index(five_kind[h+1][0][1]):
                    if card_ranks.index(hand[0][2]) > card_ranks.index(five_kind[h+1][0][2]):
                        five_kind[h], five_kind[h+1] = five_kind[h+1], five_kind[h]
                        swaps = True

                    elif card_ranks.index(hand[0][2]) == card_ranks.index(five_kind[h+1][0][2]):
                        if card_ranks.index(hand[0][3]) > card_ranks.index(five_kind[h+1][0][3]):
                            five_kind[h], five_kind[h+1] = five_kind[h+1], five_kind[h]
                            swaps = True

                        elif card_ranks.index(hand[0][3]) == card_ranks.index(five_kind[h+1][0][3]):
                            if card_ranks.index(hand[0][4]) > card_ranks.index(five_kind[h+1][0][4]):
                                five_kind[h], five_kind[h+1] = five_kind[h+1], five_kind[h]
                                swaps = True

answer = 0
rank = 1

for i in high_card:
    answer += rank * int(i[1])
    rank += 1

for i in one_pair:
    answer += rank * int(i[1])
    rank += 1

for i in two_pair:
    answer += rank * int(i[1])
    rank += 1
    
for i in three_kind:
    answer += rank * int(i[1])
    rank += 1
    
for i in full_house:
    answer += rank * int(i[1])
    rank += 1
    
for i in four_kind:
    answer += rank * int(i[1])
    rank += 1
    
for i in five_kind:
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

print("Part 2 =", answer)