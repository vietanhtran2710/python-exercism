"""
    Triangle exercise
"""

def is_triangle(sides):
    """
        Check if 3 sides length can create a triangle
    """
    if sides[0] + sides[1] > sides[2]:
        if sides[0] + sides[2] > sides[1]:
            if sides[2] + sides[1] > sides[0]:
                return True
    return False

def equilateral(sides):
    """
        Check if a triangle is equilateral
    """
    if is_triangle(sides):
        return len(set(sides)) == 1
    return False


def isosceles(sides):
    """
        Check if a triangle is isosceles
    """
    if is_triangle(sides):
        return len(set(sides)) <= 2
    return False


def scalene(sides):
    """
        Check if a triangle is scalene
    """
    if is_triangle(sides):
        return len(set(sides)) == 3
    return False
