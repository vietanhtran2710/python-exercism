"""
    Clock exercise
"""

class Clock:
    """
        Clock class
    """

    def __init__(self, hour, minute):
        """
            Create minute stamp for the clock
        """

        self.min = (hour * 60 + minute) % (24 * 60)

    def __repr__(self):
        """
            String representation of the clock
        """

        return "Clock({}, {})".format(self.min // 60, self.min % 60)

    def __str__(self):
        """
            To string method
        """

        return "{:02d}:{:02d}".format(self.min // 60, self.min % 60)

    def __eq__(self, other):
        """
            Clocks equal comparison
        """

        if self.min % (24 * 60) // 60 == other.min % (24 * 60) // 60:
            if self.min % 60 == other.min % 60:
                return True
        return False

    def __add__(self, minutes):
        """
            Add minutes to clock
        """

        self.min = (self.min + minutes) % (24 * 60)
        return Clock(self.min // 60, self.min % 60)

    def __sub__(self, minutes):
        """
            Substract minutes to clock
        """

        self.min -= minutes
        if self.min < 0:
            self.min = 24 * 60 - abs(self.min) % (24 * 60)
        return Clock(self.min // 60, self.min % 60)
