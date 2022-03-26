"""
    Robot simulator exercise
"""

# Globals for the directions
# Change the values as you see fit
EAST = 0
NORTH = 1
WEST = 2
SOUTH = 3


class Robot:
    """
        Class for creating and controlling robot
    """
    def __init__(self, direction=NORTH, x_pos=0, y_pos=0):
        self._x = x_pos
        self._y = y_pos
        self.dir_lst = [NORTH, EAST, SOUTH, WEST]
        self.dir = self.dir_lst.index(direction)
        self.advance_dct = {
            NORTH: [0, 1],
            EAST: [1, 0],
            SOUTH: [0, -1],
            WEST: [-1, 0]
        }

    @property
    def direction(self):
        """
            Return its direction
        """
        return self.dir_lst[self.dir]

    @property
    def coordinates(self):
        """
            Return its coordinates - (x, y)
        """
        return (self._x, self._y)

    def move(self, instruction):
        """
            Change direction and coordinates by a list of instruction
        """
        for step in instruction:
            if step == "A":
                current_dir = self.dir_lst[self.dir]
                self._x += self.advance_dct[current_dir][0]
                self._y += self.advance_dct[current_dir][1]
            elif step == "R":
                self.dir = (self.dir + 1) % 4
            else:
                self.dir = (self.dir - 1) % 4
