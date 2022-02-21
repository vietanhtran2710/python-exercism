"""
    Ellen's alien game exercise
"""

class Alien():
    """
        Alien class
    """
    total_aliens_created = 0

    def __init__(self, x_coord, y_coord):
        """
            Create an alien
        """
        self.x_coordinate = x_coord
        self.y_coordinate = y_coord
        self.health = 3
        Alien.total_aliens_created += 1

    def hit(self):
        """
            Decrease alien health by one
        """
        self.health -= 1

    def is_alive(self):
        """
            Check if alien is alive
        """
        return self.health > 0

    def teleport(self, x_coord, y_coord):
        """
            Change alien's coordinate
        """
        self.x_coordinate = x_coord
        self.y_coordinate = y_coord

    def collision_detection(self, *args):
        """
            Unfinished function
        """
        pass

def new_aliens_collection(positions):
    """Function taking a list of position tuples, creating one Alien instance per position.

    :param positions: list - A list of tuples of (x, y) coordinates.
    :return: list - A list of Alien objects.
    """

    return [Alien(pos[0], pos[1]) for pos in positions]
