"""
    Two-fer exercise
"""

def two_fer(*args):
    """
        Given a name, return a string with the message:

        One for name, one for me.
    """
    return "One for {}, one for me.".format("you" if len(args) == 0 else args[0])
