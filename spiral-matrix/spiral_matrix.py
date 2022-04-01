"""
    Spiral matrix exercise
"""
def spiral_matrix(size):
    """
        Create matrix
    """
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    dir_ind, row, col = 0, 0, 0
    result = [[None for i in range(size)] for j in range(size)]
    for value in range(1, size * size + 1):
        result[row][col] = value
        if 0 <= row + directions[dir_ind][0] < size:
            if 0 <= col + directions[dir_ind][1] < size:
                if result[row + directions[dir_ind][0]][col + directions[dir_ind][1]] is not None:
                    dir_ind = (dir_ind + 1) % 4
            else:
                dir_ind = (dir_ind + 1) % 4
        else:
            dir_ind = (dir_ind + 1) % 4
        row += directions[dir_ind][0]
        col += directions[dir_ind][1]
    return result
