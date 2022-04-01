"""
    Nth-prime exercise
"""
def prime(number):
    """
        Get the n-th prime
    """
    if number == 0:
        raise ValueError('there is no zeroth prime')
    is_prime, count = [True for i in range(1000000 + 1)], 0
    for i in range(2, 1000000 + 1):
        if is_prime[i]:
            count += 1
            if count == number:
                return i
            for j in range(2, 1000000 // i + 1):
                if i * j <= 1000000:
                    is_prime[i * j] = False
    return None
