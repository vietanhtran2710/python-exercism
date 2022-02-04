"""
    High scores exercise
"""

def latest(scores):
    """
        Return the latest scores from the list
    """

    return scores[-1]


def personal_best(scores):
    """
        Return max score
    """

    return max(scores)


def personal_top_three(scores):
    """
        Sort and return the first three scores
    """

    return sorted(scores, reverse=True)[:3]
