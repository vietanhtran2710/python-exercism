"""
    Matching Brackets Exercise
"""

def is_paired(input_string):
    """
        Check if a string is a valid bracket expression
    """
    stack = []
    dct = {"{": "}", "[": "]", "(": ")"}
    for char in input_string:
        if char in "{([":
            stack.append(char)
        elif char in "})]":
            try:
                if dct[stack.pop()] != char:
                    return False
            except IndexError:
                return False
    return len(stack) == 0
