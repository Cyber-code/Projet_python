from Character import Character
from Inventory import Inventory
from Consumable import Consumable

""" Merchant class instantiate a merchant object that the player can interact with him in order to buy or sell objects """
class Merchant(Character):
    def __init__(self, name="Merchant", health=20, shield=0, dodge=0,
                 parry=0, criticalHit=1, mana=10, damageMin=1,
                 damageMax=2, armor=0, xp=0, inventory=Inventory(),
                 maxHealth=20):
        Character.__init__(self, name, health, shield, dodge, parry, criticalHit, mana, damageMin, damageMax, armor, xp, inventory)

    def showInfo(self):
        return "\nMerchant: "+ Character.showInfo(self) + "\nMaximum health: "+str(self.maxHealth)+ "\n"


def generateWeaponMerchant():
    pass