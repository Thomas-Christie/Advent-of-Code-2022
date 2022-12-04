from string import ascii_lowercase
from string import ascii_uppercase

LOWERCASE_SCORES = {letter: score for score, letter in enumerate(ascii_lowercase, start=1)}
UPPERCASE_SCORES = {letter: score for score, letter in enumerate(ascii_uppercase, start=27)}


def sum_shared_item_priorities():
    with open("day_3_input.txt") as fp:
        lines = fp.readlines()
        score = 0
        for line in lines:
            first_half = line[0:len(line)//2]
            second_half = line[len(line)//2:len(line)]
            for letter in first_half:
                if letter in second_half:
                    if letter.isupper():
                        score += UPPERCASE_SCORES[letter]
                    else:
                        score += LOWERCASE_SCORES[letter]
                    break
    return score


def sum_badge_priorities():
    with open("day_3_input.txt") as fp:
        lines = fp.readlines()
        score = 0
        index = 0
        while index < len(lines):
            rucksack_one = lines[index]
            rucksack_two = lines[index + 1]
            rucksack_three = lines[index + 2]
            for item in rucksack_one:
                if item in rucksack_two and item in rucksack_three:
                    if item.isupper():
                        score += UPPERCASE_SCORES[item]
                    else:
                        score += LOWERCASE_SCORES[item]
                    break
            index += 3
    return score


if __name__ == "__main__":
    shared_item_score = sum_shared_item_priorities()
    group_badge_score = sum_badge_priorities()
    print(f"Sum of shared item priorities = {shared_item_score}")
    print(f"Sum of group badge priorities = {group_badge_score}")
