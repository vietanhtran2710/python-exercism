"""
    Sieve exercise
"""

def primes(limit):
    """
        Get all primes below a limit
    """
    if limit < 2:
        return []
    prime = [True for i in range(limit + 1)]
    result = []
    for i in range(2, limit + 1):
        if prime[i]:
            result.append(i)
            for j in range(2, limit // i + 1):
                if i * j <= limit:
                    prime[i * j] = False
    return result
