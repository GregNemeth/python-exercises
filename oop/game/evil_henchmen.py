class Evil_henchmen:

    def __init__(self, name, age, type, favourite_weapon, motto):
        self.name = name
        self.age = age
        self.type = type
        self.favourite_weapon = favourite_weapon
        self.motto = motto

    def proof_of_intellect(self):
        return f"{self.name} says: '{self.motto}'"


thug_1 = Evil_henchmen("Jimmy the earless listener","56", "schemer", "poison","""
    If you'd be rich enough, 
    you'd know that a slice of bread that's 
    buttered on both side,will never 
    fall to the ground. It just spins wildly mid-air""")

thug_2 = Evil_henchmen("Andrew the one armed bandit", "37", "gambler", "loaded dice", """
    A rigged game is the easiest to beat!""")

thug_3 = Evil_henchmen("Conman the barbarian", "32", "maniac berserker", "bare hands or axe", """
    I'm gonna show you pain you never knew existed!
    You're going to see a whole new spectrum of pain.
    LIKE A RAINBOW!!But this rainbow
    isn't just like any other rainbow...""")

print(thug_1.proof_of_intellect())

