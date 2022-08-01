from ascii_art import art_dict
from stats import BaseStats, CurrentStats

class Monster(BaseStats, CurrentStats):
    def __init__(self, name, strength, agility, intelligence, constitution, mana):
        BaseStats.__init__(self, strength, agility, intelligence, constitution, mana)
        CurrentStats.__init__(self, strength, agility, intelligence, constitution, mana)
        self.name = name
        self.art = art_dict[name]

    def print_current_stats(self):
        print(f"Strength: {self.strength}")
        print(f"Agility: {self.agility}")
        print(f"Intelligence: {self.intelligence}")
        print(f"Constitution: {self.constitution}")
        print(f"Mana: {self.mana}")

    def print(self):
        print(f"{self.name}\n")
        self.print_current_stats()
        print(self.art)



ghost = Monster("Ghost", 1,1,1,1,1)
ghost.print()