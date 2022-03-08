"""
    Secret handshake exercise
"""

def commands(binary_str):
    """
        Return list of commands
    """
    commands_lst = ["wink", "double blink", "close your eyes", "jump"]
    result = []
    for i in range(len(binary_str) - 1, 0, -1):
        if binary_str[i] == "1":
            result.append(commands_lst[len(binary_str) - 1 - i])
    if binary_str[-5] == "1":
        return result[::-1]
    return result
