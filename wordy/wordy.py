"""
    Wordy exercise
"""
def answer(question):
    """
        Evaluate expression
    """
    if not question.startswith("What is"):
        raise ValueError("unknown operation")
    math = question[7:-1].replace("minus", "-").replace("plus", "+")
    math = math.replace("multiplied by", "*").replace("divided by", "/")
    math = math.split()
    if not math or not math[0].lstrip("-").isnumeric():
        raise ValueError("syntax error")
    current = [int(math[0])]
    for index in range(1, len(math)):
        if not math[index].lstrip("-").isnumeric():
            if math[index] not in "/*+-":
                raise ValueError("unknown operation")
            current.append(math[index])
            if index < len(math) - 1 and math[index + 1] in "/*+-":
                raise ValueError("syntax error")
        else:
            try:
                if current[-1] == "+":
                    current = [current[0] + int(math[index])]
                elif current[-1] == "-":
                    current = [current[0] - int(math[index])]
                elif current[-1] == "*":
                    current = [current[0] * int(math[index])]
                elif current[-1] == "/":
                    current = [current[0] / int(math[index])]
                else:
                    raise ValueError("syntax error")
            except TypeError:
                raise ValueError("syntax error")
    if len(current) == 1:
        return current[0]
    raise ValueError("syntax error")
