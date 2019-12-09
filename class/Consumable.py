from Object import Object

""" Consumable class instantiate consumable object which is used to restore health, shield, mana or xp of the player"""
class Consumable(Object):
    def __init__(self, name="Empty bottle", value=0, health=0, shield=0, mana=0, xp=0):
        Object.__init__(self, name, value, typeObject="consumable")
        self.health = health
        self.shield = shield
        self.mana = mana
        self.xp = xp


    def showInfo(self):
        return Object.showInfo(self) + "Health: +"+ str(self.health)+" PV" + ", Shield: +"+str(self.shield) + ", Mana: +"+str(self.mana) + ", Xp: +"+str(self.xp) +")"

def generateConsumable(name="potion_healing"):
    if(name == "potion_healing"):
        return Consumable(name="Potion of Healing", value=2, health=10)
    elif(name == "potion_mana"):
        return Consumable(name="Potion of Mana", value=2, mana=5)
    elif(name == "potion_regeneration"):
        return Consumable(name="Potion of Regeneration", value=10, health=1000, shield=1000, mana=1000)
    elif(name == "piece_shield"):
        return Consumable(name="Piece of Shield", value=2, shield=5)
    elif(name == "book_knowledge"):
        return Consumable(name="Book of Knowledge", value=100, xp=100)
    else:
        return Consumable(name="Potion of Healing", value=2, health=10)