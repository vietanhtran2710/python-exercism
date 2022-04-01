"""
    Diamond exercise
"""
from string import ascii_uppercase as up

def rows(letter):
    """
        Create the diamond
    """
    spaces_length = [0] + list(range(1, 60, 2))
    max_length = spaces_length[up.index(letter)] + 2
    print(max_length)
    if letter == "A":
        return ["A"]
    result = [" " * ((max_length - 1) // 2) + "A" + " " * ((max_length - 1) // 2)]
    for i in range(1, up.index(letter) + 1):
        spaces = " " * spaces_length[i]
        space_padding = " " * ((max_length - len(spaces) - 2) // 2)
        result.append(space_padding + up[i] + spaces + up[i] + space_padding)
    result += result[-2::-1]
    for line in result:
        print(line)
    return result
