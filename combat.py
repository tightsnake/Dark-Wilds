import random
from monsters import monster_dict
import player

player_alive = True
monster_alive = True
win_status = False
in_combat = True
monster_is_attacking = True

def get_random_monster():
    monster_key = random.choice(list(monster_dict.keys()))
    monster = monster_dict[monster_key]
    return monster


def get_initiative_order():
    order = random.randint(0, 1)
    player_turn = False
    if order == 0:
        player_turn = True
    #print(player_turn)
    return player_turn

# if win_status is True when combat ends, the player has won
# if win_status is False when combat ends, the monster has won


def chance_to_hit(attacker, defender):
    does_it_hit = False
    base_roll = random.randint(0, 20)
    total_roll = base_roll + attacker.current_agility - defender.current_agility
    if total_roll > 10:
        does_it_hit = True
    return does_it_hit


def run_away(attacker, defender):
    gets_away = False
    base_roll_current = random.randint(0, 20)
    base_roll_defending = random.randint(0, 20)
    total_roll_current = base_roll_current + attacker.current_agility
    total_roll_defending = base_roll_defending + defender.current_agility
    if total_roll_current > total_roll_defending:
        gets_away = True
    return gets_away


def attack_damage(attacker, defender, turn):
    global win_status
    global in_combat
    weapon_damage = random.randint(1, 3)
    # Damage is calculated based on both the attacker and the defender's strength
    total_damage = weapon_damage + attacker.current_strength - defender.current_strength
    # The minimum damage that can be dealt is 1.
    if total_damage < 1:
        total_damage = 1
    defender.current_constitution -= total_damage
    # check about constitution being in base stats and current stats
    # if the program will know which to refer to
    # life total of defending_opponent is reduced by total_damage amount
    if defender.current_constitution == 0 and turn == True:
        win_status = True
        in_combat = False

    if attacker.current_constitution == 0:
        win_status = False
        in_combat = False
    return total_damage


def player_actions(attacker, defender, turn):
    player_choice = False
    global in_combat
    while player_choice == False:
        choice = int(input("What would you like to do?\n(1) Attack or (2) Run\n"))
        if choice == 1 or choice == 2:
            player_choice = True
        else:
            print("Only 1 and 2 are valid choices.")
    if choice == 1:
        does_it_hit = chance_to_hit(attacker, defender)
        if does_it_hit == True:
            print("You hit the monster!")
            # ascii art?
            damage_dealt = attack_damage(attacker, defender, turn)
            print(f"You deal {damage_dealt} damage!")

            # damage dealt based on strength score
        else:
            print("You missed!")
            # ascii art?
    else:
        print("You attempt to run away from the monster...")
        # some sort of pause here... maybe an image
        gets_away = run_away(attacker, defender)
        if gets_away == True:
            print("You have escaped from the monster!")
            in_combat = False
        else:
            print("The monster catches you!")
        # player tries to run away
        # whether they get away is based on chance and agility score

    # check if player and monster alive


def monster_actions(attacker, defender, turn):
    global win_status
    global in_combat
    global monster_is_attacking
    print("It is the monster's turn!")
    if attacker.current_constitution == 1:
        monster_is_attacking = False

    if monster_is_attacking:
        does_it_hit = chance_to_hit(attacker, defender)
        if does_it_hit == True:
            print("The monster hits you!")
            # ascii art?
            damage_dealt = attack_damage(attacker, defender, turn)
            print(f"You take {damage_dealt} damage!")

            # damage dealt based on strength score
        else:
            print("The monster misses you!")
            # ascii art?
    else:
        print("The monster attempts to run away...")
        # some sort of pause here... maybe an image
        gets_away = run_away(attacker, defender)
        if gets_away == True:
            print("The monster has escaped!")
            win_status = False
            in_combat = False
        else:
            print("You have caught the monster!")
        # player tries to run away
        # whether they get away is based on chance and agility score

    # player choice of what to do
    # check if player and monster alive
    # monster choice of what to do
    # check if player and monster alive

def combat_loop(adventurer, evil_monster):
    player_turn = get_initiative_order()
    while in_combat:
        if player_turn:
            player_actions(attacker = adventurer, defender = evil_monster, turn = player_turn)
            player_turn = False
        else:
            monster_actions(attacker = evil_monster, defender = adventurer, turn = player_turn)
            player_turn = True
    if win_status == True:
       print("Congratulations! You have defeated the monster!")
    elif win_status == False and adventurer.current_constitution == 0:
        print("The monster has killed you...")

    else:
        print("The monster is gone.")
 
