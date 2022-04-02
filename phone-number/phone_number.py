"""
    Phone number exercise
"""
import re

class PhoneNumber:
    """
        Class to format phone number input
    """
    def __init__(self, number):
        for char in number:
            if not char.isdigit() and char not in "()-. +":
                if char.isalpha():
                    raise ValueError("letters not permitted")
                raise ValueError("punctuations not permitted")
        print(re.sub("[^0-9]", "", number))
        self.number = re.sub("[^0-9]", "", number)
        if len(self.number) < 10:
            raise ValueError("incorrect number of digits")
        if len(self.number) > 11:
            raise ValueError("more than 11 digits")
        if len(self.number) == 11:
            if self.number[0] != "1":
                raise ValueError("11 digits must start with 1")
            self.area_code = self.number[1:4]
            self.number = self.number[1:]
        else:
            self.area_code = self.number[:3]
        exchange_code = self.number[3:6]
        if self.area_code[0] == "0":
            raise ValueError("area code cannot start with zero")
        if self.area_code[0] == "1":
            raise ValueError("area code cannot start with one")
        if exchange_code[0] == "0":
            raise ValueError("exchange code cannot start with zero")
        if exchange_code[0] == "1":
            raise ValueError("exchange code cannot start with one")

    def pretty(self):
        """
            Prettify the phone number string
        """
        return "(" + self.number[:3] + ")-" + self.number[3:6] + "-" + self.number[6:]
