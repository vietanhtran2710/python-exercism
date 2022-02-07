"""
    Series exercise
"""

def slices(series, length):
    """
        Return list of slices of len "length" from series"
    """

    if length < 0:
        raise ValueError("slice length cannot be negative")
    if length == 0:
        raise ValueError("slice length cannot be zero")
    if series == "":
        raise ValueError("series cannot be empty")
    if length > len(series):
        raise ValueError("slice length cannot be greater than series length")
    result = []
    for i in range(0, len(series) - length + 1):
        result.append(series[i:i + length])
    return result
