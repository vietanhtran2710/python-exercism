"""
    ISBN verifier exercise
"""

def is_valid(isbn):
    """
        Check if a string is a valid ISBN
    """
    if len(isbn) < 10:
        return False
    if isbn[-1] != 'X' and not isbn[-1].isdigit():
        return False
    digits = []
    for index, char in enumerate(isbn):
        if not char.isdigit():
            if index != len(isbn) - 1 and char != '-':
                return False
            if char == 'X':
                digits.append(10)
        else:
            digits.append(int(char))
    if len(digits) > 10:
        return False
    value = sum([digit * (10 - index) for index, digit in enumerate(digits)])
    return value % 11 == 0
