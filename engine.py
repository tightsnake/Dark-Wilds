from player import Player, get_player_name
from combat import Combat

class Engine:

    def main_loop(self):
        print(
        "Welcome to Dark Wilds! Get ready for combat, adventurer! Anything can happen in the wilderness >:)"
        )
        player_name = get_player_name()
        player = Player(
        name=player_name, strength=1, agility=1, intelligence=1, constitution=20
        )
        while True:
            combat = Combat()
            combat.run(player)



        # loot the monster?
        # character gets closer to levelling up?


