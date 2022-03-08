"""
    Connect Game exercise
"""

class ConnectGame:
    """
        Class to solve the game
    """
    def __init__(self, board):
        self.board = board.replace(" ", "").split("\n")

    def get_winner(self):
        """
            Get the current from the board, return empty string
            if the game hasn't finished
        """
        for line in self.board:
            print(line)
        checked = [[False for i in range(len(self.board[0]))] for j in range(len(self.board))]
        def go_cell(i, j, player):
            if i == len(self.board) - 1 and player == "O":
                return player
            if j == len(self.board[0]) - 1 and player == "X":
                return player
            directions = ((-1, 0), (0, -1), (1, 0), (0, 1), (-1, 1), (1, -1))
            for _dir in directions:
                _x, _y = i + _dir[0], j + _dir[1]
                if 0 <= _x < len(self.board) and 0 <= _y < len(self.board[0]):
                    if self.board[_x][_y] == player and not checked[_x][_y]:
                        checked[_x][_y] = True
                        result = go_cell(_x, _y, player)
                        if result is not None:
                            return result
                        checked[_x][_y] = False
            return None

        for i in range(len(self.board[0])):
            if self.board[0][i] == "O":
                checked[0][i] = True
                result = go_cell(0, i, "O")
                checked[0][i] = False
                if result:
                    return result
        for i in range(len(self.board)):
            if self.board[i][0] == "X":
                checked[i][0] = True
                result = go_cell(i, 0, "X")
                checked[i][0] = False
                if result:
                    return result
        return ""
