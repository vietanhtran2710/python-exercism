"""
    OCR Numbers exercise
"""

def convert(input_grid):
    """
        Convert to digit string
    """
    dct = {
        " _ | ||_|   ": "0",
        "     |  |   ": "1",
        " _  _||_    ": "2",
        " _  _| _|   ": "3",
        "   |_|  |   ": "4",
        " _ |_  _|   ": "5",
        " _ |_ |_|   ": "6",
        " _   |  |   ": "7",
        " _ |_||_|   ": "8",
        " _ |_| _|   ": "9",
    }
    if len(input_grid) % 4:
        raise ValueError("Number of input lines is not a multiple of four")
    if len(input_grid[0]) % 3:
        raise ValueError("Number of input columns is not a multiple of three")
    result = ""
    for i in range(0, len(input_grid), 4):
        for j in range(0, len(input_grid[0]), 3):
            digit = "".join(map(lambda x, j=j: x[j:j + 3], input_grid[i:i + 4]))
            try:
                result += dct[digit]
            except KeyError:
                result += "?"
        if i != len(input_grid) - 4:
            result += ","
    return result
