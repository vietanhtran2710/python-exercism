"""
    Minesweeper exercise
"""

def annotate(minefield):
    """
        Annotate the minefield
    """
    if len({len(row) for row in minefield}) > 1:
        raise ValueError("The board is invalid with current input.")
    directions = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
    for i, row in enumerate(minefield):
        lst = list(row)
        for j, cell in enumerate(row):
            if cell == " ":
                count = 0
                for _dir in directions:
                    if 0 <= i + _dir[0] < len(minefield) and 0 <= j + _dir[1] < len(minefield[0]):
                        count += 1 if minefield[i + _dir[0]][j + _dir[1]] == "*" else 0
                lst[j] = str(count) if count != 0 else " "
            elif cell != "*":
                raise ValueError("The board is invalid with current input.")
        minefield[i] = "".join(lst)
    return minefield
