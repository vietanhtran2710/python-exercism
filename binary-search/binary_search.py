"""
    Binary search exercise
"""
def find(search_list, value):
    """
        Find the value in the search list, return its index
    """
    def search(left, right):
        if left > right:
            raise ValueError("value not in array")
        if left == right:
            if search_list[left] != value:
                raise ValueError("value not in array")
            return left
        mid = (left + right) // 2
        if search_list[mid] == value:
            return mid
        if search_list[mid] > value:
            return search(left, mid - 1)
        return search(mid + 1, right)
    return search(0, len(search_list) - 1)
