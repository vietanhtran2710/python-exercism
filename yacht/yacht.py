"""
    Yatch exercise
"""
from collections import Counter

YACHT = 0
ONES = 1
TWOS = 2
THREES = 3
FOURS = 4
FIVES = 5
SIXES = 6
FULL_HOUSE = 7
FOUR_OF_A_KIND = 8
LITTLE_STRAIGHT = 9
BIG_STRAIGHT = 10
CHOICE = 11

def score(dice, category):
    """
        Return the score from the dice and a category
    """
    count = Counter(dice)
    if category == YACHT:
        return 50 if count[dice[0]] == 5 else 0
    if category == ONES:
        return count[1]
    if category == TWOS:
        return 2 * count[2]
    if category == THREES:
        return 3 * count[3]
    if category == FOURS:
        return 4 * count[4]
    if category == FIVES:
        return 5 * count[5]
    if category == SIXES:
        return 6 * count[6]
    if category == FULL_HOUSE:
        if 3 in count.values() and 2 in count.values():
            return sum(dice)
        return 0
    if category == FOUR_OF_A_KIND:
        for key, value in count.items():
            if value >= 4:
                return key * 4
        return 0
    if category == LITTLE_STRAIGHT:
        return 30 if sorted(dice) == [1, 2, 3, 4, 5] else 0
    if category == BIG_STRAIGHT:
        return 30 if sorted(dice) == [2, 3, 4, 5, 6] else 0
    if category == CHOICE:
        return sum(dice)
    return None
