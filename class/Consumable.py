from Object import Object
from random import randint

class Consumable(Object):
    """ 
    Consumable class instantiate consumable object which is used to restore health, shield, mana or xp of the character.
    Consumables are used just use one time.
    """

    def __init__(self, name="Empty bottle", value=0, health=0, shield=0, mana=0, xp=0, libelle="empty_bottle"):
        Object.__init__(self, name, value, typeObject="consumable", libelle=libelle)
        self.health = health
        self.shield = shield
        self.mana = mana
        self.xp = xp


    def showInfo(self):
        """ Return a string which are precised parameters of the consumable object. """
        return Object.showInfo(self) + "Health: +"+ str(self.health)+" PV" + ", Shield: +"+str(self.shield) + ", Mana: +"+str(self.mana) + ", Xp: +"+str(self.xp) +")"

def generateConsumable(name=""):
    """ Return a Consumable object. """

    if(name == "potion_healing"):
        return Consumable(name="Potion of Healing", value=2, health=10, libelle="potion_healing")
    elif(name == "potion_mana"):
        return Consumable(name="Potion of Mana", value=2, mana=5, libelle="potion_mana")
    elif(name == "potion_regeneration"):
        return Consumable(name="Potion of Regeneration", value=100, health=1000, shield=1000, mana=1000, libelle="potion_regeneration")
    elif(name == "piece_shield"):
        return Consumable(name="Piece of Shield", value=2, shield=5, libelle="piece_shield")
    elif(name == "book_knowledge"):
        return Consumable(name="Book of Knowledge", value=200, xp=100, libelle="book_knowledge")
    else:
        items = ["potion_healing","potion_mana","piece_shield","potion_regeneration","book_knowledge"]

        return generateConsumable(name=items[randint(0,len(items)-1)])