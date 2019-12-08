from Character import Character
from Inventory import Inventory
from Consumable import Consumable
from Weapon import Weapon
from Armor import Armor
from Jewels import Jewels

""" Monster class instantiate a monster object who will fight the player """
class Monster(Character):
    def __init__(self, name="Zombie", health=20, shield=2, dodge=0,
                 parry=0, criticalHit=1, mana=0, damageMin=2,
                 damageMax=4, armor=0, xp=0, inventory=Inventory()):
        Character.__init__(self, name, health, shield, dodge, parry, criticalHit, mana, damageMin, damageMax, armor, xp, inventory)


    """ When the monster is killed by the player then it drops a lot of items 
        This method can be modified """
    def dropItems(self):
        gold = 10
        healthPotion = Consumable(name="Potion of heath", value=5, health=5)
        return [gold, self.xp, healthPotion]


def generateZombie():
    return Monster(name="Zombie", health=20, shield=2, damageMin=2, damageMax=4, xp=5)

def generateBowmanSkeleton():
    return Monster(name="Bowman skeleton", health=20, dodge=10, damageMin=1, damageMax=5, xp=5)

def generateSwordmanSkeleton():
    return Monster(name="Swordman skeleton", health=20, dodge=5, parry=5, damageMin=2, damageMax=3, xp=5)

def generateSpider():
    return Monster(name="Spider", health=16, dodge=20, damageMin=2, damageMax=3, xp=5)

def generateEnderman():
    return Monster(name="Enderman", health=20, dodge=40, criticalHit=5, damageMin=4, damageMax=10, xp=5)

def generateZombiePigman():
    return Monster(name="Zombie Pigman", health=20, shield=2, dodge=20, damageMin=5, damageMax=12, xp=5)

def generateGhast():
    return Monster(name="Ghast", health=10, dodge=30, criticalHit=5, damageMin=1, damageMax=17, xp=5)

def generateBlaze():
    return Monster(name="Blaze", health=20, parry=20, criticalHit=5, damageMin=3, damageMax=7, xp=10)

def generateEnderDragon():
    return Monster(name="Ender dragon", health=200, dodge=30, criticalHit=10, damageMin=6, damageMax=15, xp=500)