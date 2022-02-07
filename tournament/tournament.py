"""
    Tournament exercise
"""

def tally(rows):
    """
        Return result table
    """

    table = {}
    for line in rows:
        items = line.split(";")
        if items[-1] == "win":
            try:
                table[items[0]][0] += 1
                table[items[0]][1] += 1
                table[items[0]][4] += 3
            except KeyError:
                table[items[0]] = [1, 1, 0, 0, 3]
            try:
                table[items[1]][0] += 1
                table[items[1]][3] += 1
            except KeyError:
                table[items[1]] = [1, 0, 0, 1, 0]
        elif items[-1] == "draw":
            for team in [items[0], items[1]]:
                try:
                    table[team][0] += 1
                    table[team][2] += 1
                    table[team][4] += 1
                except KeyError:
                    table[team] = [1, 0, 1, 0, 1]
        else:
            try:
                table[items[0]][0] += 1
                table[items[0]][3] += 1
            except KeyError:
                table[items[0]] = [1, 0, 0, 1, 0]
            try:
                table[items[1]][0] += 1
                table[items[1]][1] += 1
                table[items[1]][4] += 3
            except KeyError:
                table[items[1]] = [1, 1, 0, 0, 3]
    result = ["Team                           | MP |  W |  D |  L |  P"]
    for item in sorted(table.items(), key=lambda x: (-x[1][-1], x[0])):
        f_str = "{:<30} | {:>2} | {:>2} | {:>2} | {:>2} | {:>2}"
        info = [item[0]] + item[1]
        result.append(f_str.format(*info))
    for line in result:
        print(line)
    return result
