"""
    Twelve Days Exercises
"""

def recite(start_verse, end_verse):
    """
        Return the lyrics
    """

    result = []

    order = [
        "first", "second", "third",
        "fourth", "fifth", "sixth",
        "seventh", "eighth", "ninth",
        "tenth", "eleventh", "twelfth"
    ]

    items = [
        "a Partridge in a Pear Tree.", "two Turtle Doves, ", "three French Hens, ",
        "four Calling Birds, ", "five Gold Rings, ", "six Geese-a-Laying, ",
        "seven Swans-a-Swimming, ", "eight Maids-a-Milking, ", "nine Ladies Dancing, ",
        "ten Lords-a-Leaping, ", "eleven Pipers Piping, ",
        "twelve Drummers Drumming, ",
    ]

    for i in range(start_verse, end_verse + 1):
        verse = "On the " + order[i - 1] + " day of Christmas my true love gave to me: "
        for j in range(i - 1, -1, -1):
            if j == 0 and i != 1:
                verse += "and "
            verse += items[j]
        result.append(verse)

    return result
