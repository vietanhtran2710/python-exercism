"""
    Grep exercise
"""

FILE_TEXT = {
    "iliad.txt": """Achilles sing, O Goddess! Peleus' son;
His wrath pernicious, who ten thousand woes
Caused to Achaia's host, sent many a soul
Illustrious into Ades premature,
And Heroes gave (so stood the will of Jove)
To dogs and to all ravening fowls a prey,
When fierce dispute had separated once
The noble Chief Achilles from the son
Of Atreus, Agamemnon, King of men.\n""",
    "midsummer-night.txt": """I do entreat your grace to pardon me.
I know not by what power I am made bold,
Nor how it may concern my modesty,
In such a presence here to plead my thoughts;
But I beseech your grace that I may know
The worst that may befall me in this case,
If I refuse to wed Demetrius.\n""",
    "paradise-lost.txt": """Of Mans First Disobedience, and the Fruit
Of that Forbidden Tree, whose mortal tast
Brought Death into the World, and all our woe,
With loss of Eden, till one greater Man
Restore us, and regain the blissful Seat,
Sing Heav'nly Muse, that on the secret top
Of Oreb, or of Sinai, didst inspire
That Shepherd, who first taught the chosen Seed\n""",
}

def print_match(file_name, ind, row, flags):
    """
        Format output
    """
    result = ""
    if "-l" in flags:
        return file_name + "\n"
    if "-m" in flags:
        result += file_name + ":"
    if "-n" in flags:
        result += str(ind) + ":"
    result += row
    return result

def grep(pattern, flags, files):
    """
        Find matching pattern in each line of file
    """
    flags = flags.split(" ") + ["-m"] if len(files) > 1 else flags.split(" ")
    pattern = pattern.lower() if "-i" in flags else pattern
    result = []
    for file in files:
        text = FILE_TEXT[file]
        lines = text.split("\n")
        for index, row in enumerate(lines):
            try:
                find = row.lower() if "-i" in flags else row
                if "-x" in flags:
                    if find != pattern:
                        raise ValueError
                    if "-v" not in flags and row != "":
                        result.append(print_match(file, index + 1, row + "\n", flags))
                        if "-l" in flags:
                            break
                else:
                    find.index(pattern)
                    if "-v" not in flags and row != "":
                        result.append(print_match(file, index + 1, row + "\n", flags))
                        if "-l" in flags:
                            break
            except ValueError:
                if "-v" in flags and row != "":
                    result.append(print_match(file, index + 1, row + "\n", flags))
                    if "-l" in flags:
                        break
    return "".join(result)
