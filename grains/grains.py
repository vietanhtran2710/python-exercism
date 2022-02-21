"""
    Grains exercise
"""

def square(number):
    """
        Return the number of grains on a square
    """
    if number not in range(1, 65):
        raise ValueError("square must be between 1 and 64")
    return 2 ** (number - 1)

def total():
    """
        Calculate the sum of grains on all squares
    """
    return sum([square(num) for num in range(1, 65)])
