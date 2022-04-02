"""
    Pig Latin exercise
"""
def translate(text):
    """
        Translate the text
    """
    words = text.split()
    for index, word in enumerate(words):
        if word.startswith(("u", "e", "o", "a", "i", "xr", "yt")):
            words[index] += "ay"
        elif word[1:].startswith("qu"):
            words[index] = word[3:] + word[:3] + "ay"
        elif word.startswith("qu"):
            words[index] = word[2:] + word[:2] + "ay"
        else:
            ind = 0
            while ind < len(word) and word[ind] not in "ueoai":
                ind += 1
                if ind > 0 and word[ind] == "y":
                    break
            words[index] = word[ind:] + word[:ind] + "ay"
    return " ".join(words)
