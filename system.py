import os

debugging = True

def clear_screen():
    if not debugging:
        os.system('cls' if os.name == 'nt' else 'clear')