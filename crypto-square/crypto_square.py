"""
    Crypto square exercise
"""

from textwrap import wrap
from math import sqrt

def cipher_text(plain_text):
    """
        Cipher the text
    """
    if not plain_text:
        return ""
    plain_text = "".join(filter(lambda x: x.isalnum(), plain_text.lower()))
    if sqrt(len(plain_text)) == int(sqrt(len(plain_text))):
        row = int(sqrt(len(plain_text)))
        col = row
    else:
        col = int(sqrt(len(plain_text))) + 1
        row = col - 1
    if row * col < len(plain_text):
        row += 1
    print(col, row)
    square, result = wrap(plain_text, col), ""
    square[-1] += " " * (col - len(square[-1]))
    for line in square:
        print(line)
    for i in range(col):
        result += "".join([line[i] for line in square])
    encode = wrap(result, row)
    for i in range(len(encode) - 1, -1, -1):
        if len(encode[i]) < row:
            encode[i] += " " * (row - len(encode[i]))
        else:
            break
    return " ".join(encode)
