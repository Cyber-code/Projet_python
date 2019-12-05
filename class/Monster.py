from Character import Character
from Inventory import Inventory
from Consumable import Consumable
from Weapon import Weapon
from Armor import Armor
from Jewels import Jewels

""" Monster class instantiate a monster object who will fight the player """
class Monster(Character):
    def __init__(self, name="Skeleton", health=10, shield=0, dodge=0,
                 parry=0, criticalHit=1, mana=10, damageMin=1,
                 damageMax=2, armor=0, level=1, xp=10, inventory=Inventory(),
                 maxHealth=10):
        Character.__init__(self, name, health, shield, dodge, parry, criticalHit, mana, damageMin, damageMax, armor, level, xp, inventory)
        self.maxHealth = maxHealth
        # Here self.xp is the amount of xp that the player can earn by killing the monster

    def showInfo(self):
        return "\nMonster: "+ Character.showInfo(self) + "\nMaximum health: "+str(self.maxHealth)+ "\n"

    """ When the monster is killed by the player then it drops a lot of items 
        This method can be modified """
    def dropItems(self):
        gold = 10
        healthPotion = Consumable(name="Potion of heath", value=5, health=5)
        return [gold, self.xp, healthPotion]