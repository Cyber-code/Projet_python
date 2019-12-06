from Character import Character
from Inventory import Inventory
from Consumable import Consumable

""" Merchant class instantiate a merchant object that the player can interact with him in order to buy or sell objects """
class Merchant(Character):
    def __init__(self, name="Merchant", health=20, shield=0, dodge=0,
                 parry=0, criticalHit=1, mana=10, damageMin=1,
                 damageMax=2, armor=0, level=1, xp=0, inventory=Inventory(),
                 maxHealth=20):
        inventory = [Consumable(name="Potion of health", value=10, health=10, shield=0, mana=0, xp=0),
                    Consumable(name="Potion of shield", value=10, health=0, shield=10, mana=0, xp=0),
                    Consumable(name="Potion of mana", value=10, health=0, shield=0, mana=10, xp=0),
                    Consumable(name="Potion of xp", value=10, health=0, shield=0, mana=0, xp=10),
                    Consumable(name="Potion of mana", value=5, health=0, shield=0, mana=20, xp=0)]
        Character.__init__(self, name, health, shield, dodge, parry, criticalHit, mana, damageMin, damageMax, armor, level, xp, inventory)
        self.maxHealth = maxHealth

    def showInfo(self):
        return "\nMerchant: "+ Character.showInfo(self) + "\nMaximum health: "+str(self.maxHealth)+ "\n"