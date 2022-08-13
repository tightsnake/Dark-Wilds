class BaseStats:
    def __init__(self, strength, agility, intelligence, constitution):
        self.base_strength = strength
        self.base_agility = agility
        self.base_intelligence = intelligence
        self.base_constitution = constitution


class CurrentStats:
    def __init__(self, strength, agility, intelligence, constitution):
        self.current_strength = strength
        self.current_agility = agility
        self.current_intelligence = intelligence
        self.current_constitution = constitution
