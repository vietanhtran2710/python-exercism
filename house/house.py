"""
    House exercise
"""
def recite(start_verse, end_verse):
    """
        Recite the the song mutlitple times from start verse to end verse
    """
    objects = [
        "house that Jack built.",
        "malt",
        "rat",
        "cat",
        "dog",
        "cow with the crumpled horn",
        "maiden all forlorn",
        "man all tattered and torn",
        "priest all shaven and shorn",
        "rooster that crowed in the morn",
        "farmer sowing his corn",
        "horse and the hound and the horn"
    ]

    action = [
        "",
        "lay in",
        "ate",
        "killed",
        "worried",
        "tossed",
        "milked",
        "kissed",
        "married",
        "woke",
        "kept",
        "belonged to",
        ""
    ]

    result = []
    for i in range(start_verse, end_verse + 1):
        verse = "This is the " + objects[i - 1]
        for j in range(i - 1, 0, -1):
            verse += " that " + action[j] + " the " + objects[j - 1]
        result.append(verse)

    return result
