"""
    Hey Bob Exercise
"""

def response(hey_bob):
    """
        Get the response
    """
    if not hey_bob.strip():
        return "Fine. Be that way!"
    chars = "".join(filter(lambda c: c.isalpha(), hey_bob))
    if hey_bob.strip()[-1] == "?":
        if chars.isupper():
            return "Calm down, I know what I'm doing!"
        return "Sure."
    if chars.isupper():
        return "Whoa, chill out!"
    return "Whatever."
