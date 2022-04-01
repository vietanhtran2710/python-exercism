"""
    Resistor Color Duo Exercise
"""
COLOR_DCT = {
    "black": 0,
    "brown": 1,
    "red": 2,
    "orange": 3,
    "yellow": 4,
    "green": 5,
    "blue": 6,
    "violet": 7,
    "grey": 8,
    "white": 9,
}

def value(colors):
    """
        Calculate resistor number value
    """
    return COLOR_DCT[colors[0]] * 10 + COLOR_DCT[colors[1]]
