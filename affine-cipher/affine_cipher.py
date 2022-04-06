"""
    Affine Cipher
"""
from string import ascii_lowercase as low
from textwrap import wrap
from math import gcd

def encode(plain_text, a_value, b_value):
    """
        Encode text
    """
    if gcd(a_value, 26) != 1:
        raise ValueError("a and m must be coprime.")
    plain_text = list(filter(lambda x: x.isalnum(), list(plain_text)))
    for index, char in enumerate(plain_text):
        if char.isalpha():
            new_index = (a_value * low.index(char.lower()) + b_value) % len(low)
            plain_text[index] = low[new_index]
    return " ".join(wrap("".join(plain_text), 5))


def decode(ciphered_text, a_value, b_value):
    """
        Decode text
    """
    if gcd(a_value, 26) != 1:
        raise ValueError("a and m must be coprime.")
    ciphered_text = list("".join(ciphered_text.split()))
    for index, char in enumerate(ciphered_text):
        if char.isalpha():
            mmi = 1
            while a_value * mmi % 26 != 1:
                mmi += 1
                new_index = mmi * (low.index(char) - b_value) % len(low)
                ciphered_text[index] = low[new_index]
    return "".join(ciphered_text)
