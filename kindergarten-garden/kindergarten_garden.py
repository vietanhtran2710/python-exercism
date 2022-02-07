"""
    Kindergarten Garden Exercise
"""

class Garden:
    """
        Garden class
    """

    def __init__(self, diagram, students=(
            "Alice", "Bob", "Charlie", "David",
            "Eve", "Fred", "Ginny", "Harriet",
            "Ileana", "Joseph", "Kincaid", "Larry")):
        """
            Create garden
        """

        self.student = sorted(students)
        self.diagram = diagram.split("\n")
        self.plant = {"V": "Violets", "C": "Clover", "R": "Radishes", "G": "Grass"}

    def plants(self, name):
        """
            Return student's plant
        """

        result, ind = [], self.student.index(name)
        for row in self.diagram:
            result.append(self.plant[row[ind * 2]])
            result.append(self.plant[row[ind * 2 + 1]])
        return result
