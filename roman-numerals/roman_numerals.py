"""
    Roman numerals exercise
"""
def roman(number):
    """
        Decimal integer to roman numeral string
    """
    m_count, number = number // 1000, number % 1000
    result = "M" * m_count
    if number // 100 == 9:
        result += "CM"
        number %= 900
    d_count, number = number // 500, number % 500
    if d_count:
        result += "D" * d_count
    c_count, number = number // 100, number % 100
    if c_count:
        result += "C" * c_count if c_count != 4 else "CD"
    if number // 10 == 9:
        result += "XC"
        number %= 90
    l_count, number = number // 50, number % 50
    if l_count:
        result += "L" * l_count
    x_count, number = number // 10, number % 10
    if x_count:
        result += "X" * x_count if x_count != 4 else "XL"
    if number == 9:
        return result + "IX"
    v_count, number = number // 5, number % 5
    if v_count:
        result += "V" * v_count
    if number == 4:
        result += "IV"
    else:
        result += "I" * number
    return result
