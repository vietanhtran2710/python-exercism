"""
    Gigasecond exercise
"""
from datetime import timedelta

def add(moment):
    """
        Add a gigasecond to moment datetime
    """
    return moment + timedelta(seconds=1000000000)
