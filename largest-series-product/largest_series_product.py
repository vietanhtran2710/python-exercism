"""
    Largest series product
"""

from functools import reduce


def largest_product(series, size):
    """
        Return the largest product
    """
    if size < 0:
        raise ValueError("span must not be negative")
    if size > len(series):
        raise ValueError("span must be smaller than string length")
    if series and not series.isdigit():
        raise ValueError("digits input must only contain digits")
    if not series or size == 0:
        return 1
    lst = list(map(int, series))
    prod = reduce(lambda a, b: a * b, lst[:size])
    _max = prod
    for i in range(size, len(lst)):
        if lst[i - size] == 0:
            prod = reduce(lambda a, b: a * b, lst[i - size + 1:i + 1])
            _max = max(_max, prod)
        else:
            _max = max(_max, prod // lst[i - size] * lst[i])
            prod = prod // lst[i - size] * lst[i]
    return _max
