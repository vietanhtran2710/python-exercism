"""
    All your base exercise
"""
def rebase(input_base, digits, output_base):
    """
        Change digits of a number from input base to output base
    """
    if input_base < 2:
        raise ValueError("input base must be >= 2")
    if any(map(lambda x: x < 0 or x >= input_base, digits)):
        raise ValueError("all digits must satisfy 0 <= d < input base")
    if output_base < 2:
        raise ValueError("output base must be >= 2")
    base10 = 0
    for index, digit in enumerate(digits[::-1]):
        base10 += digit * input_base ** index
    result = []
    while base10 != 0:
        result.append(base10 % output_base)
        base10 //= output_base
    return result[::-1] if result else [0]
