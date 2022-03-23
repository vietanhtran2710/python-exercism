"""
    Spell number exercise
"""

def say(number):
    """
        Speak a number in English
    """
    if number < 0 or number > 999999999999:
        raise ValueError("input out of range")
    if not number:
        return "zero"
    dct = {
        0: "", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five",
        6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten",
        11: "elevent", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen",
        16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen",
    }
    dct2 = dct.copy()
    dct2[4], dct2[5], dct2[2], dct2[8], dct2[3] = "for", "fif", "twen", "eigh", "thir"
    result, time = "", 0
    chunk_name = ["", "thousand", "million", "billion"]
    while number != 0:
        chunk, num = number % 1000, ""
        if chunk != 0:
            if chunk >= 100:
                num += dct[chunk // 100] + " hundred"
            chunk %= 100
            if chunk != 0:
                num += " "
            if chunk >= 20:
                num += dct2[chunk // 10] + "ty"
                chunk %= 10
                if chunk != 0:
                    num += "-"
            if chunk != 0:
                num += dct[chunk]
        if number % 1000 != 0:
            result = num + " " + chunk_name[time] + " " + result.strip()
        print(result)
        time += 1
        number //= 1000
    return result.strip()
