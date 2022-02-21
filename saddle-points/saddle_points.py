"""
    Saddle points exercise
"""

def saddle_points(matrix):
    """
        Return coordinates of all saddle points
    """
    if len({len(row) for row in matrix}) > 1:
        raise ValueError("irregular matrix")
    result = []
    for i, row in enumerate(matrix):
        for j, cell in enumerate(row):
            if cell == max(row):
                if cell == min([matrix[r][j] for r in range(len(matrix))]):
                    result.append({"row": i + 1, "column": j + 1})
    return result
