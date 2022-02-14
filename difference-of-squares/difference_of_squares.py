"""
    Difference of Squares Exercise
"""

def square_of_sum(number):
    """
        Return the square of sum of first [number] neutral integers
    """
    return sum(range(1, number + 1)) ** 2


def sum_of_squares(number):
    """
        Return the sum of square of first [number] neutral integers
    """
    return sum([i ** 2 for i in range(1, number + 1)])


def difference_of_squares(number):
    """
        Return the difference between sum of squares and square of sum
    """
    return abs(square_of_sum(number) - sum_of_squares(number))
