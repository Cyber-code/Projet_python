from random import randint

class Spell:
    """ Spell class instantiate a spell object which can be thrown by a character if he has enought mana. """
    def __init__(self, name="Fireball", damage=2, mana=5):
        self.name = name
        self.damage = damage
        self.mana = mana

    def showInfo(self):
        """ This method return a string containing spell's parameters. """
        return "\nSpell:\nName: {}\nDamages: {}\nMana: {}".format(self.name, str(self.damage), str(self.mana))

def generateSpell(name=""):
    """ Return a spell object. """
    if(name=="fireball"):
        return Spell(name="Fireball", damage=2, mana=5)
    elif(name=="lightning"):
        return Spell(name="Lightning", damage=5, mana=10)
    else:
        spell = ["fireball","lightning"]
        return generateSpell(name=spell[randint(0,len(spell)-1)])