"""
    List operations exercise
"""
def append(list1, list2):
    """
    Given two lists, add all items in the second list to the end of the first list
    """
    return list1 + list2


def concat(lists):
    """
    Given a series of lists, combine all items in all lists into one flattened list
    """
    result = []
    for lst in lists:
        for item in lst:
            result += [item]
    return result


def filter(function, list):
    """
    Given a series of lists, combine all items in all lists into one flattened list
    """
    return [item for item in list if function(item)]


def length(list):
    """
    Given a list, return the total number of items within it
    """
    count = 0
    for _item in list:
        count += 1
    return count


def map(function, list):
    """
    Given a function and a list,
    return the list of the results of applying function(item) on all items
    """
    return [function(item) for item in list]


def foldl(function, list, initial):
    """
    Given a function, a list, and initial accumulator,
    fold (reduce) each item into the accumulator from the left using function(accumulator, item)
    """
    for item in list:
        initial = function(initial, item)
    return initial


def foldr(function, list, initial):
    """
    given a function, a list, and an initial accumulator,
    fold (reduce) each item into the accumulator from the right using function(item, accumulator)
    """
    for item in list[::-1]:
        initial = function(item, initial)
    return initial


def reverse(list):
    """
    given a list, return a list with all the original items, but in reversed order
    """
    return list[::-1]
