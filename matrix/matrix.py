"""
    Matrix exercise
"""

class Matrix:
    """
        Matrix class
    """

    def __init__(self, matrix_string):
        """
            Create a matrix
        """

        self.rows = []
        self.columns = [[] for i in range(len(matrix_string.split("\n")[0].split()))]
        for line in matrix_string.split("\n"):
            items = list(map(int, line.split(" ")))
            self.rows.append(items)
            for index, value in enumerate(items):
                self.columns[index].append(value)

    def row(self, index):
        """
            Return a row by index
        """

        return self.rows[index - 1]

    def column(self, index):
        """
            Return a column by index
        """

        return self.columns[index - 1]
