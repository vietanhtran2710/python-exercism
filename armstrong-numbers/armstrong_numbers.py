"""
    Armstrong numbers exercise
"""

def is_armstrong_number(number):
    """
        Check if a number is an Armstrong number
    """
    return number == sum([int(digit) ** len(str(number)) for digit in str(number)])
