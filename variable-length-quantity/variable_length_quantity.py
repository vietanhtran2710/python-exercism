"""
    Variable length quantity exercise
"""
def encode(numbers):
    """
        Encode
    """
    result = []
    for value in numbers:
        binary, count, encoded = bin(value)[2:], 0, []
        print(binary)
        while len(binary) != 0:
            byte = "0" * (7 - len(binary[-7:])) + binary[-7:]
            number = "1" + byte if count != 0 else byte
            encoded.insert(0, (int(number, 2)))
            binary = binary[:-7]
            count += 1
        result += encoded
    return result


def decode(bytes_):
    """
        Decode into one or multiple values
    """
    result = []
    decoded = ""
    for value in bytes_:
        print(bin(value))
        binary = bin(value)
        if len(binary[2:]) < 8:
            decoded += "0" * (7 - len(binary[2:])) + binary[2:]
        else:
            decoded += binary[3:]
        if binary[2] == "0" or len(binary[2:]) < 8:
            try:
                result.append(int(decoded, 2))
            except ValueError:
                result.append(0)
            decoded = ""
    if decoded:
        raise ValueError("incomplete sequence")
    return result
