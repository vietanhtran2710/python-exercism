"""
    Rotational Cipher Exercise
"""

from string import ascii_lowercase as low, ascii_uppercase as up

def rotate(text, key):
    """
        Encrypt the text
    """
    result = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                result += up[(up.index(char) + key) % len(up)]
            else:
                result += low[(low.index(char) + key) % len(low)]
        else:
            result += char
    return result
