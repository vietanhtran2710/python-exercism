"""
    Rectangle exercise
"""

def rectangles(str):
    """
        Return the number of rectangles
    """
    check = []
    for i, row in enumerate(str):
        for j, char in enumerate(row):
            if char == "+":
                for _a in range(j + 1, len(row)):
                    if str[i][_a] == "+":
                        for _b in range(i + 1, len(str)):
                            if str[_b][_a] == "+" and str[_b][j] == "+":
                                check.append([(i, j), (_b, _a)])
    count = 0
    for item in check:
        horiz = str[item[0][0]][item[0][1]:item[1][1] + 1]
        horiz2 = str[item[1][0]][item[0][1]:item[1][1] + 1]
        if " " not in horiz and "|" not in horiz and " " not in horiz2 and "|" not in horiz2:
            vertical = [str[i][item[1][1]] for i in range(item[0][0], item[1][0] + 1)]
            vertical2 = [str[i][item[0][1]] for i in range(item[0][0], item[1][0] + 1)]
            if " " not in vertical and "-" not in vertical:
                if " " not in vertical2 and "-" not in vertical2:
                    count += 1
    return count
