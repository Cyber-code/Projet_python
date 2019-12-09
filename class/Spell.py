""" Spell class instantiate a spell object which can be thrown by a character """
class Spell:
    def __init__(self, name="Fireball", damage=2, mana=5):
        self.name = name
        self.damage = damage
        self.mana = mana

    def showInfo(self):
        return "\nSpell:\nName: {}\nDamages: {}\nMana: {}".format(self.name, str(self.damage), str(self.mana))

def generateFireball():
    return Spell(name="Fireball", damage=2, mana=5)

def generateLightning():
    return Spell(name="Lightning", damage=5, mana=10)