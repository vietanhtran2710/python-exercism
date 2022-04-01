"""
    Rail fence cipher exercise
"""
def encode(message, rails):
    """
        Encode the message
    """
    rows, ind, direction = ["" for i in range(rails)], 0, 1
    for char in message:
        rows[ind] += char
        ind += direction
        if ind in [rails, -1]:
            direction *= -1
            ind += direction * 2
    return "".join(rows)


def decode(encoded_message, rails):
    """
        Decode the message
    """
    rows, ind, direction = ["" for i in range(rails)], 0, 1
    for _char in encoded_message:
        rows[ind] += " "
        ind += direction
        if ind in [rails, -1]:
            direction *= -1
            ind += direction * 2
    for item in rows:
        print(len(item))
    embed_length = 0
    for i in range(rails):
        rows[i] = encoded_message[embed_length: embed_length + len(rows[i])]
        embed_length += len(rows[i])
    for item in rows:
        print(item)
    rail_ind = [0 for i in range(rails)]
    result, ind, direction = "", 0, 1
    for i in range(embed_length):
        result += rows[ind][rail_ind[ind]]
        rail_ind[ind] += 1
        ind += direction
        if ind in [rails, -1]:
            direction *= -1
            ind += direction * 2
    return result
