from player import Player, get_player_name
from combat import (
    get_random_monster,
    get_initiative_order,
    combat_loop
)

print(
    "Welcome to Dark Wilds! Get ready for combat, adventurer! Anything can happen in the wilderness >:)"
)

player_name = get_player_name()
player = Player(
    name=player_name, strength=1, agility=1, intelligence=1, constitution=20
)
monster = get_random_monster()

monster.print()
print(f"A {monster.name} appears! Get ready to fight, {player_name}!")

combat_loop(player, monster)

    # loot the monster?
    # character gets closer to levelling up?


