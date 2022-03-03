"""
    Allergies exercise
"""

class Allergies:
    """
        Class to get all allergies from a score
    """

    def __init__(self, score):
        """
            Calculate list of allergies from score using dynamic programming
        """
        self.dct = {
            1: "eggs",
            2: "peanuts",
            4: "shellfish",
            8: "strawberries",
            16: "tomatoes",
            32: "chocolate",
            64: "pollen",
            128: "cats"
        }
        dp_array = [([], 0) for i in range(score + 1)]
        dp_array[0] = ([], - 1)
        for i in range(score):
            power = dp_array[i][1] + 1
            while i + 2 ** power <= score:
                if power <= 7:
                    dp_array[i + 2 ** power] = (dp_array[i][0] + [self.dct[2 ** power]], power)
                else:
                    dp_array[i + 2 ** power] = dp_array[i]
                power += 1
        self.allergies = dp_array[score][0]

    def allergic_to(self, item):
        """
            Check if a score contains an allergies
        """
        return item in self.lst

    @property
    def lst(self):
        """
            List all allergies
        """
        values = {}
        for key, value in self.dct.items():
            values[value] = key
        return self.allergies
