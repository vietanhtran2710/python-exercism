"""
    Transpose exercise
"""
def transpose(lines):
    """
        Transpose the lines
    """
    lines = lines.split("\n")
    if not lines:
        return ""
    max_length = max(map(len, lines))
    result = []
    for index in range(max_length):
        col, spaces = "", ""
        for line in lines:
            try:
                col += spaces + line[index]
                spaces = ""
            except IndexError:
                spaces += " "
        result.append(col)
    for line in result:
        print("\"" + line + "\"")
    return "\n".join(result)
