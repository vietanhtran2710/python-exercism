"""
    Sum of multiples exercise
"""

def sum_of_multiples(limit, multiples):
    """
        Return a sum of all multiples below the limit
    """
    result = 0
    for i in range(0, limit):
        conditions = map(lambda x, i=i: i % x == 0, filter(lambda x: x != 0, multiples))
        if any(conditions):
            result += i
    return result
