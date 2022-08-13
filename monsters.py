from ascii_art import art_dict
from stats import BaseStats, CurrentStats


class Monster(BaseStats, CurrentStats):
    def __init__(self, name, strength, agility, intelligence, constitution):
        BaseStats.__init__(self, strength, agility, intelligence, constitution)
        CurrentStats.__init__(self, strength, agility, intelligence, constitution)
        self.name = name
        self.art = art_dict[name]

    def print_current_stats(self):
        print(f"Strength: {self.current_strength}")
        print(f"Agility: {self.current_agility}")
        print(f"Intelligence: {self.current_intelligence}")
        print(f"Constitution: {self.current_constitution}")

    def print(self):
        print(f"{self.name}\n")
        self.print_current_stats()
        print(self.art)


ghost = Monster("Ghost", 1, 1, 1, 5)
devil = Monster("Devil", 1, 1, 1, 5)
skeleton_warrior = Monster("Skeleton Warrior", 3, 3, 3, 10)

monster_dict = {"Ghost": ghost, "Devil": devil, "Skeleton Warrior" : skeleton_warrior}
