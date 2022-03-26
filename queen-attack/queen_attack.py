"""
    Queen attack exercise
"""

class Queen:
    """
        Store queen coordinate
    """
    def __init__(self, row, column):
        if row < 0:
            raise ValueError("row not positive")
        if column < 0:
            raise ValueError("column not positive")
        if row >= 8:
            raise ValueError("row not on board")
        if column >= 8:
            raise ValueError("column not on board")
        self.row = row
        self.col = column

    def can_attack(self, another_queen):
        """
            Check if the queen can attack another queen
        """
        if self.row == another_queen.row:
            if self.col == another_queen.col:
                raise ValueError("Invalid queen position: both queens in the same square")
            return True
        if self.col == another_queen.col:
            return True
        row_diff = abs(self.row - another_queen.row)
        col_diff = abs(self.col - another_queen.col)
        if row_diff == col_diff:
            return True
        return False
