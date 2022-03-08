"""
    Poker exercise
"""
from collections import Counter

VALUE_DCT = {"A": 14, "K": 13, "Q": 12, "J": 11, "T": 10}
for _i in range(2, 10):
    VALUE_DCT[str(_i)] = _i

ONE_PAIR = 15
TWO_PAIR = 16
THREE_OF_A_KIND = 17
STRAIGHT = 18
FLUSH = 19
FULL_HOUSE = 20
FOUR_OF_A_KIND = 21
STRAIGHT_FLUSH = 22
ROYAL_FLUSH = 23

def is_one_pair(hand):
    """
        Check if hand got one pair
    """
    value = [item[0] for item in hand]
    dct = Counter(value)
    values, count = 0, 0
    for key, value in dct.items():
        if dct[key] == 2:
            values, count = key, count + 1
    if count == 1:
        return [True, VALUE_DCT[values]]
    return [False]

def is_two_pair(hand):
    """
        Check if hand got two pairs
    """
    value = [item[0] for item in hand]
    dct = Counter(value)
    values, single, count = [], 0, 0
    for key, value in dct.items():
        if dct[key] == 2:
            values.append(key)
            count += 1
        if dct[key] == 1:
            single = key
    if count == 2:
        values.sort(reverse=True)
        return [True, VALUE_DCT[values[0]], VALUE_DCT[values[1]], VALUE_DCT[single]]
    return [False]

def is_three_of_a_kind(hand):
    """
        Check if hand got three of a kind
    """
    value = [item[0] for item in hand]
    values, kind = [], 0
    dct = Counter(value)
    for key, value in dct.items():
        if dct[key] == 3:
            kind = key
        else:
            values.append(key)
    values.sort(reverse=True)
    if kind:
        return [True, kind] + values
    return [False]

def is_straight(hand):
    """
        Check if hand got straight
    """
    value = sorted([VALUE_DCT[item[0]] for item in hand])
    for i in range(len(value) - 1):
        if value[i] + 1 != value[i + 1]:
            dct = {"A": 1, "K": 13, "Q": 12, "J": 11, "T": 10}
            for j in range(2, 10):
                dct[str(j)] = j
            value = sorted([dct[item[0]] for item in hand])
            for j in range(len(value) - 1):
                if value[j] + 1 != value[j + 1]:
                    return [False]
    return [True, max(value)]

def is_flush(hand):
    """
        Check if hand got flush
    """
    _s = set()
    for item in hand:
        _s.add(item[1])
    if len(_s) == 1:
        hand.sort(key=lambda x: x[0])
        return [True, VALUE_DCT[hand[-1][0]]]
    return [False]

def is_full_house(hand):
    """
        Check if hand got full house
    """
    value = [item[0] for item in hand]
    dct = Counter(value)
    three, pair = 0, 0
    for key, value in dct.items():
        if value == 3:
            three = key
        elif value == 2:
            pair = key
        else:
            return [False]
    return [True, VALUE_DCT[three], VALUE_DCT[pair]]

def is_four_of_a_kind(hand):
    """
        Check if hand got four of a kind
    """
    value = [item[0] for item in hand]
    dct = Counter(value)
    kind, single = 0, 0
    for key, value in dct.items():
        if value == 4:
            kind = key
        else:
            single = key
    if kind:
        return [True, kind, single]
    return [False]

def is_straight_flush(hand):
    """
        Check if hand got straight flush
    """
    check_result = is_straight(hand)
    if check_result[0] and is_flush(hand)[0]:
        return [True, check_result[1]]
    return [False]

def is_royal_flush(hand):
    """
        Check if hand got royal flush
    """
    value = "".join(sorted([item[0] for item in hand]))
    if value == "AJKQT" and is_flush(hand):
        return [True]
    return [False]

def get_rank(hand):
    """
        Get a hand's rank (score)
    """
    if is_royal_flush(hand)[0]:
        return [ROYAL_FLUSH]
    check_result = is_straight_flush(hand)
    if check_result[0]:
        return [STRAIGHT_FLUSH, check_result[1]]
    check_result = is_four_of_a_kind(hand)
    if check_result[0]:
        return [FOUR_OF_A_KIND, check_result[1], check_result[2]]
    check_result = is_full_house(hand)
    if check_result[0]:
        return [FULL_HOUSE, check_result[1], check_result[2]]
    check_result = is_flush(hand)
    if check_result[0]:
        return [FLUSH, check_result[1]]
    check_result = is_straight(hand)
    if check_result[0]:
        return [STRAIGHT, check_result[1]]
    check_result = is_three_of_a_kind(hand)
    if check_result[0]:
        return [THREE_OF_A_KIND, check_result[1], check_result[2], check_result[3]]
    check_result = is_two_pair(hand)
    if check_result[0]:
        return [TWO_PAIR, check_result[1], check_result[2], check_result[3]]
    check_result = is_one_pair(hand)
    if check_result[0]:
        return [ONE_PAIR, check_result[1]]
    value = [VALUE_DCT[item[0]] for item in hand]
    value.sort(reverse=True)
    return value

def best_hands(hands):
    """
        Get best hands
    """
    _max, result = [0, 0, 0], []
    for hand in hands:
        cards = hand.replace("10", "T").split()
        score = get_rank(cards)
        print(cards, score)
        index = 0
        while index < len(score) and index < len(_max) and score[index] == _max[index]:
            index += 1
        if index >= len(score) or index >= len(_max):
            result.append(hand)
        elif score[index] > _max[index]:
            _max, result = list(score), [hand]
        print(_max)
    return result
