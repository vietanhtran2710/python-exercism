"""
    Flatten array excerise
"""
def flatten(iterable):
    """
        Flatten array
    """
    def get_items(array):
        result = []
        for item in array:
            if isinstance(item, list):
                result += get_items(item)
            elif item is not None:
                result.append(item)
        return result
    return get_items(iterable)
