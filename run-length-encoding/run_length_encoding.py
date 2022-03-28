"""
    Run length encoding exercise
"""
def decode(string):
    """
        Decode the string
    """
    result, index, count = "", 0, ""
    while index < len(string):
        if string[index].isdigit():
            count += string[index]
        else:
            if not count:
                result += string[index]
            else:
                result += int(count) * string[index]
                count = ""
        index += 1
    return result

def encode(string):
    """
        Encode the string
    """
    result, index = "", 0
    while index < len(string):
        count, j = 1, index + 1
        while j < len(string) and string[j] == string[index]:
            count += 1
            j += 1
        if count > 1:
            result += str(count) + string[index]
        else:
            result += string[index]
        index = j
    return result
