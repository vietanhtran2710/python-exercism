"""
    Anagram exercise
"""

def find_anagrams(word, candidates):
    """
        Return a list of word's anagrams from candidates
    """

    same_removed = filter(lambda x: x.lower() != word.lower(), candidates)
    return filter(lambda x: sorted(x.lower()) == sorted(word.lower()), same_removed)
