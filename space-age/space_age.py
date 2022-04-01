"""
    Space age exercise
"""
class SpaceAge:
    """
        Class to calculate space age
    """
    def __init__(self, seconds):
        self.earth_age = seconds / 31557600

    def on_earth(self):
        """
            Calculate space on earth
        """
        return round(self.earth_age, 2)

    def on_mercury(self):
        """
            Calculate space on mercury
        """
        return round(self.earth_age / 0.2408467, 2)

    def on_venus(self):
        """
            Calculate space on venus
        """
        return round(self.earth_age / 0.61519726, 2)

    def on_mars(self):
        """
            Calculate space on mars
        """
        return round(self.earth_age / 1.8808158, 2)

    def on_jupiter(self):
        """
            Calculate space on jupiter
        """
        return round(self.earth_age / 11.862615, 2)

    def on_saturn(self):
        """
            Calculate space on saturn
        """
        return round(self.earth_age / 29.447498, 2)

    def on_neptune(self):
        """
            Calculate space on neptune
        """
        return round(self.earth_age / 164.79132, 2)

    def on_uranus(self):
        """
            Calculate space on uranus
        """
        return round(self.earth_age / 84.016846, 2)
