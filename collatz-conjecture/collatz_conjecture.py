"""
    Collatz Conjecture exercise
"""

def steps(number):
    """
        Count the number of steps
    """

    if number <= 0:
        raise ValueError("Only positive integers are allowed")
    step = 0
    while number != 1:
        number = 3 * number + 1 if number % 2 else number // 2
        step += 1
    return step
