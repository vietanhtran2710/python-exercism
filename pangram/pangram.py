"""
    Pangram exercise
"""

import re

def is_pangram(sentence):
    """
        Check if a sentence is a pangram
    """

    return len(set("".join(re.split("[^a-z]", sentence.lower())))) == 26
