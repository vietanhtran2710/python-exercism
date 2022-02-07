""""
    Grade school exercise
"""

class School:
    """
        Implement a class for a school
    """

    def __init__(self):
        """
            Create database
        """

        self.grades = {}
        self.add_history = []

    def add_student(self, name, grade):
        """
            Add a student to the database
        """

        try:
            for students in self.grades.values():
                if name in students:
                    self.add_history.append(False)
                    return
            self.grades[grade].add(name)
        except KeyError:
            self.grades[grade] = set([name])
        self.add_history.append(True)

    def roster(self):
        """
            Return every student sorted by grade then by name
        """

        result = []
        for grade in sorted(self.grades.keys()):
            result += sorted(self.grades[grade])
        return result

    def grade(self, grade_number):
        """
            Return all students in a grade
        """

        try:
            return sorted(self.grades[grade_number])
        except KeyError:
            return []

    def added(self):
        """
            Return adding student history
        """

        return self.add_history
