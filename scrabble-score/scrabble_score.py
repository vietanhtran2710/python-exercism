"""
    Scrabble Score Exercise
"""

def score(word):
    """
        Calculate score for a word
    """

    result = 0
    for char in word.upper():
        if char in "AEIOULNRST":
            result += 1
        elif char in "DG":
            result += 2
        elif char in "BCMP":
            result += 3
        elif char in "FHVWY":
            result += 4
        elif char == "K":
            result += 5
        elif char in "JX":
            result += 8
        else:
            result += 10
    return result
