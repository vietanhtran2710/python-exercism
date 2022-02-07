"""
    Robot Exercise
"""

import datetime
import random
import string

STATE = 1

class Robot:
    """
        Robot class
    """

    def __init__(self):
        """
            Generate a random name for robot
        """

        global STATE
        self.name = ""
        random.seed(datetime.date.today() + datetime.timedelta(days=STATE))
        for _i in range(2):
            self.name += random.choice(string.ascii_uppercase)
        for _i in range(3):
            self.name += random.choice(string.digits)
        STATE += random.randint(1, 10000)

    def reset(self):
        """
            Reset robot name
        """

        Robot.__init__(self)
