"""
    Dragon and dungeon exercise
"""
from random import randint, choice

def modifier(value):
    """
        Return modifier value of constitution stat
    """
    return (value - 10) // 2

class Character:
    """
        Class for a character in DnD game
    """
    def __init__(self):
        """
            Generate abilities stat and HP
        """
        self.strength = sum(sorted([randint(1, 6) for _ in range(4)])[1:])
        self.dexterity = sum(sorted([randint(1, 6) for _ in range(4)])[1:])
        self.constitution = sum(sorted([randint(1, 6) for _ in range(4)])[1:])
        self.intelligence = sum(sorted([randint(1, 6) for _ in range(4)])[1:])
        self.wisdom = sum(sorted([randint(1, 6) for _ in range(4)])[1:])
        self.charisma = sum(sorted([randint(1, 6) for _ in range(4)])[1:])
        self.hitpoints = 10 + modifier(self.constitution)

    def ability(self):
        """
            Return a random ability
        """
        ability = [
            self.strength,
            self.dexterity,
            self.constitution,
            self.intelligence,
            self.wisdom,
            self.charisma
        ]
        return choice(ability)
