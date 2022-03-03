"""
    Simple Cipher Excersise
"""

from string import ascii_lowercase
from random import choices

class Cipher:
    """
        Cipher class
    """
    def __init__(self, key=None):
        """
            Create a key
        """
        if key is None:
            self.key = "".join(choices(ascii_lowercase, k=100))
        else:
            self.key = key

    def encode(self, text):
        """
            Encode text
        """
        lst = list(text)
        for ind, char in enumerate(text):
            ascii_ind = ascii_lowercase.index(char)
            shift_ind = ascii_lowercase.index(self.key[ind % len(self.key)]) + ascii_ind
            replace_ind = shift_ind % len(ascii_lowercase)
            replace_char = ascii_lowercase[replace_ind]
            lst[ind] = replace_char
        return "".join(lst)

    def decode(self, text):
        """
            Decode text
        """
        lst = list(text)
        for ind, char in enumerate(text):
            ascii_ind = ascii_lowercase.index(char)
            replace_ind = ascii_lowercase.index(self.key[ind % len(self.key)]) - ascii_ind
            replace_char = ascii_lowercase[-replace_ind]
            lst[ind] = replace_char
        return "".join(lst)
