"""
    Scale generator exercise
"""

class Scale:
    """
        Scale class
    """
    def __init__(self, tonic):
        """
            Create necessary data
        """
        self.sharp_major = ["G", "D", "A", "E", "B", "F#", "C"]
        self.sharp_minor = ["e", "b", "f#", "c#", "g#", "d#", "a"]
        self.flat_major = ["F", "Bb", "Eb", "Ab", "Db", "Gb"]
        self.flat_minor = ["d", "g", "c", "f", "bb", "eb"]

        self.major_sharp_sort = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]
        self.major_flat_sort = ["A", "Bb", "B", "C", "Db", "D", "Eb", "E", "F", "Gb", "G", "Ab"]
        self.tonic = tonic

    def chromatic(self):
        """
            Generate chromatic
        """
        if self.tonic in self.flat_major:
            array = self.major_flat_sort
        elif self.tonic in self.sharp_major:
            array = self.major_sharp_sort
        elif self.tonic in self.flat_minor:
            array = list(map(lambda x: x.lower(), self.major_sharp_sort))
        else:
            array = list(map(lambda x: x.lower(), self.major_flat_sort))
        result = []
        for i in range(array.index(self.tonic), len(array)):
            result.append(array[i])
        for i in range(0, array.index(self.tonic)):
            result.append(array[i])
        return result

    def interval(self, intervals):
        """
            Generate scale based on interval
        """
        if self.tonic in self.sharp_major:
            array = self.major_sharp_sort
        elif self.tonic in self.major_flat_sort:
            array = self.major_flat_sort
        elif self.tonic in self.sharp_minor:
            array = self.major_sharp_sort
            self.tonic = self.tonic.upper()
        else:
            array = self.major_flat_sort
            if len(self.tonic) > 1:
                self.tonic = self.tonic[0].upper() + self.tonic[1]
            else:
                self.tonic = self.tonic.upper()
        result = [self.tonic]
        index = array.index(self.tonic)
        for item in intervals:
            if item == "m":
                index = (index + 1) % len(array)
            elif item == "M":
                index = (index + 2) % len(array)
            else:
                index = (index + 3) % len(array)
            result.append(array[index])
        return result
