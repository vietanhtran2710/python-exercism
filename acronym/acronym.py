"""
    Acronym Exercise
"""

import re

def abbreviate(words):
    """
        Return the acronym of a string
    """

    words = filter(lambda x: x != '', re.split("[^a-zA-Z0-9']", words))
    return "".join([word[0].upper() for word in words])
