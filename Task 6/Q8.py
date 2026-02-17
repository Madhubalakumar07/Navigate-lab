class Character:
    def attack(self): pass

class Warrior(Character):
    def attack(self): print("Sword Attack")

class Mage(Character):
    def attack(self): print("Magic Attack")
