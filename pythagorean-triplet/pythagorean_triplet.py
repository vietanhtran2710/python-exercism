"""
    Pythagorean Triplet Exercise
"""

def triplets_with_sum(number):
    """
        Get all triplets
    """
    result = []
    for _a in range(1, number - 1):
        if _a ** 2 % (number - _a) == 0:
            if (number - _a + (_a ** 2) // (number - _a)) % 2 == 0:
                _c = (number - _a + (_a ** 2) // (number - _a)) // 2
                _b = number - _a - _c
                if _b > 0 and _c > 0 and _a < _b < _c:
                    result.append([_a, _b, _c])
    return result
