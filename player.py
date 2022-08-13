from stats import BaseStats, CurrentStats


def get_player_name():
    player_name = input("What is your name, adventurer?\n")
    return player_name

class Player(BaseStats, CurrentStats):
    def __init__(self, name, strength, agility, intelligence, constitution):
        BaseStats.__init__(self, strength, agility, intelligence, constitution)
        CurrentStats.__init__(self, strength, agility, intelligence, constitution)
        self.name = name

    def print_current_stats(self):
        print(f"Strength: {self.current_strength}")
        print(f"Agility: {self.current_agility}")
        print(f"Intelligence: {self.current_intelligence}")
        print(f"Constitution: {self.current_constitution}")

    def print(self):
        print(f"{self.name}\n")
        self.print_current_stats()
