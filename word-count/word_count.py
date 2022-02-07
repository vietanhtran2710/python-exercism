"""
    Word count exercise
"""


from collections import Counter
import re

def count_words(sentence):
    """
        Return the number of words
    """

    words = list(filter(lambda x: x != '', re.split("[^a-zA-Z0-9']", sentence.lower())))
    for i, word in enumerate(words):
        if word.startswith("'") or word.startswith("\""):
            index = 0
            while word[index] in "'\"":
                index += 1
            words[i] = word[index:-index]
    return Counter(words)

# return Counter(re.findall(r"[a-z0-9]+(?:'[a-z]+)?", sentence.lower()))