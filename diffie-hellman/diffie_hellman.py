"""
    Diffie Hellman Exercise
"""

from random import choice
from math import sqrt

def power_mod(val, power, m_value):
    """
        Calculate power mod the efficent way
    """
    if power <= 100:
        return (val ** power) % m_value
    if power % 2 == 0:
        return (power_mod(val, power // 2, m_value) ** 2) % m_value
    return (power_mod(val, power // 2, m_value) * power_mod(val, power // 2 + 1, m_value)) % m_value

def private_key(p_value):
    """
        Generate a private key
    """
    if p_value > 1000000000:
        p_value = int(sqrt(p_value))
    is_prime = [True for i in range(p_value)]
    primes = []
    for i in range(2, p_value):
        if is_prime[i]:
            primes.append(i)
            for j in range(2, p_value // i + 1):
                if i * j < p_value:
                    is_prime[i * j] = False
    return choice(primes)

def public_key(p_value, g_value, private):
    """
        Generate the public key
    """
    return power_mod(g_value, private, p_value)


def secret(p_value, public, private):
    """
        Generate the secret
    """
    return power_mod(public, private, p_value)
