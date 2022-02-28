"""
    Prime factors exercise
"""

from math import sqrt

def is_prime(value):
    """
        Check if a number is a prime number
    """
    for i in range(2, int(sqrt(value)) + 1):
        if value % i == 0:
            return False
    return True

def factors(value):
    """
        Get all prime factors of a number
    """
    result = []
    prime = 2
    while value != 1:
        if value % prime == 0 and is_prime(prime):
            result.append(prime)
            value //= prime
        else:
            prime += 1
    return result
