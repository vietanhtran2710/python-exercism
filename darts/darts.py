"""
    Darts exercise
"""
from math import sqrt

def score(x_value, y_value):
    """
        Calculate the score
    """
    distance = sqrt(x_value ** 2 + y_value ** 2)
    if distance <= 1:
        return 10
    if distance <= 5:
        return 5
    if distance <= 10:
        return 1
    return 0
