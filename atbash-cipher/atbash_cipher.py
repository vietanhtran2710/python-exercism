"""
    Atbash cipher exercise
"""
from string import ascii_lowercase as alpha
from string import digits
from textwrap import wrap

def encode(plain_text):
    """
        Encrypt text
    """
    dct, plain_text = {}, "".join(plain_text.split())
    for index in range(26):
        dct[alpha[index]] = alpha[::-1][index]
    function = lambda x: dct[x] if x in alpha else x if x in digits + " " else ""
    encoded = "".join(map(function, list(plain_text.lower())))
    return " ".join(wrap(encoded, 5))

def decode(ciphered_text):
    """
        Decrypt text
    """
    join = "".join(ciphered_text.split())
    dct = {}
    function = lambda x: dct[x] if x in alpha else x if x in digits + " " else ""
    for index in range(26):
        dct[alpha[::-1][index]] = alpha[index]
    return "".join(map(function, list(join)))
