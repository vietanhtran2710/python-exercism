"""
    Isogram exercise
"""


def is_isogram(string):
    """
        Check is a word is isogram
    """

    char_set = set()
    for char in string.lower():
        if char.isalpha():
            if char in char_set:
                return False
            char_set.add(char)
    return True
