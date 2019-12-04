from Object import Object

""" Consumable class is used to restore health, shield, mana or xp of the player"""
class Consumable(Object):
    def __init__(self, name="Bottle of water", value=0, health=0, shield=0, mana=0, xp=0):
        Object.__init__(self, name, value)
        self.health = health
        self.shield = shield
        self.mana = mana
        self.xp = xp

    def showInfo(self):
        return "\nConsumable: " + Object.showInfo(self) + "\nHealth: "+ str(self.health) + "\nShield: "+str(self.shield) + "\nMana: "+str(self.mana) + "\nXp: "+str(self.xp) +"\n"