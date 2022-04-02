"""
    Palindrome products exercise
"""

def largest(min_factor, max_factor):
    """Given a range of numbers, find the largest palindromes which
       are products of two numbers within that range.

    :param min_factor: int with a default value of 0
    :param max_factor: int
    :return: tuple of (palindrome, iterable).
             Iterable should contain both factors of the palindrome in an arbitrary order.
    """
    if min_factor > max_factor:
        raise ValueError("min must be <= max")
    for product in range(max_factor ** 2, min_factor ** 2 - 1, -1):
        if str(product) == str(product)[::-1]:
            factors = []
            for j in range(min_factor, max_factor + 1):
                if product % j == 0 and min_factor <= (product // j) <= max_factor:
                    factors.append(sorted([j, product // j]))
            if factors:
                return product, factors
    return None, []


def smallest(min_factor, max_factor):
    """Given a range of numbers, find the smallest palindromes which
    are products of two numbers within that range.

    :param min_factor: int with a default value of 0
    :param max_factor: int
    :return: tuple of (palindrome, iterable).
    Iterable should contain both factors of the palindrome in an arbitrary order.
    """
    if min_factor > max_factor:
        raise ValueError("min must be <= max")
    for product in range(min_factor ** 2, max_factor ** 2 + 1):
        if str(product) == str(product)[::-1]:
            factors = []
            for j in range(min_factor, max_factor + 1):
                if product % j == 0 and min_factor <= product // j <= max_factor:
                    print(j, product // j)
                    factors.append(sorted([j, product // j]))
            if factors:
                return product, factors
    return None, []
