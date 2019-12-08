from Object import Object

""" Consumable class instantiate consumable object which is used to restore health, shield, mana or xp of the player"""
class Consumable(Object):
    def __init__(self, name="Empty bottle", value=0, health=0, shield=0, mana=0, xp=0):
        Object.__init__(self, name, value)
        self.health = health
        self.shield = shield
        self.mana = mana
        self.xp = xp

        self.type = "consumable"


    def showInfo(self):
        return "\nConsumable: " + Object.showInfo(self) + "\nHealth: +"+ str(self.health)+" PV" + "\nShield: +"+str(self.shield) + "\nMana: +"+str(self.mana) + "\nXp: +"+str(self.xp) +"\n"


def generatePotionHealing():
    return Consumable(name="Potion of Healing", value=2, health=10)

def generatePotionMana():
    return Consumable(name="Potion of Mana", value=2, mana=5)

def generatePotionRegeneration():
    return Consumable(name="Potion of Regeneration", value=10, health=1000, shield=1000, mana=1000)

def generatShieldPiece():
    return Consumable(name="Piece of Shield", value=2, shield=5)

def generateKnowledgeBook():
    return Consumable(name="Book of Knowledge", value=100, xp=100)