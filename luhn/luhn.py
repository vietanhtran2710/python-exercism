"""
    Luhn exercise
"""

class Luhn:
    """
        Luhn class
    """

    def __init__(self, card_num):
        """
            Format card number string
        """

        self.num = "".join(card_num.split())

    def valid(self):
        """
            Check if card is valid
        """

        if not self.num.isnumeric() or len(self.num) <= 1:
            return False
        result = sum(map(int, list(self.num)))
        for i in range(len(self.num) - 2, -1, -2):
            result += int(self.num[i])
            if int(self.num[i]) * 2 > 9:
                result -= 9
        print(result)
        return result % 10 == 0
