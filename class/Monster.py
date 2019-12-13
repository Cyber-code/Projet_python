from Character import Character
from Inventory import Inventory
from Consumable import generateConsumable
from Weapon import generateWeapon
from Armor import generateArmor
from Jewels import generateJewel
from random import randint, expovariate, gauss

class Monster(Character):
    """ Monster class instantiate a monster object who will fight the player. """
    def __init__(self, name="Zombie", health=20, shield=2, dodge=0,
                 parry=0, criticalHit=1, mana=0, damageMin=2,
                 damageMax=4, armor=0, xp=0, inventory=Inventory()):
        Character.__init__(self, name, health, shield, dodge, parry, criticalHit, mana, damageMin, damageMax, armor, xp, inventory)


    def dropItems(self):
        """ Return a tuple containing monster's amount of gold and xp and a chest. """
        items = (self.xp, int(gauss(self.xp, 2)), generateChest())
        # Clear the monster's inventory
        self.inventory.gold = 0
        self.inventory.objects = []
        return items

def generateChest():
    """
    Return a chest with n items.
    n is generate with an exponential law. By default, lamb=1 i.e the average item number generated by expovariate is 1.
    Add 1 to have one item at least, thus the n average is 2.
    """
    n = int(expovariate(1)) + 1
    random = 0
    chest = []
    for i in range(n):
        random = randint(0,99)
        # 70 % of chance to append a consumable
        if(random < 70):
            chest.append(generateConsumable())
        # 10 % of chance to append a jewel
        elif(random < 80):
            chest.append(generateJewel())
        # 10 % of chance to append an armor
        elif(random < 90):
            chest.append(generateArmor())
        # 10 % of chance to append a weapon
        else:
            chest.append(generateWeapon())
    return chest


def generateMonster(name=""):
    """ Return a Monster object."""
    if(name == "zombie"):
        return Monster(name="Zombie", health=20, shield=2, damageMin=2, damageMax=4, xp=5)
    elif(name == "bowman_skeleton"):
        return Monster(name="Bowman skeleton", health=20, dodge=10, damageMin=1, damageMax=5, xp=5)
    elif(name == "swordman_skeleton"):
        return Monster(name="Swordman skeleton", health=20, dodge=5, parry=5, damageMin=2, damageMax=3, xp=5)
    elif(name == "spider"):
        return Monster(name="Spider", health=16, dodge=20, damageMin=2, damageMax=3, xp=5)
    elif(name == "enderman"):
        return Monster(name="Enderman", health=20, dodge=40, criticalHit=5, damageMin=4, damageMax=10, xp=5)
    elif(name == "zombie_pigman"):
        return Monster(name="Zombie Pigman", health=20, shield=2, dodge=20, damageMin=5, damageMax=12, xp=5)
    elif(name == "ghast"):
        return Monster(name="Ghast", health=10, dodge=30, criticalHit=5, damageMin=1, damageMax=17, xp=5)
    elif(name == "blaze"):
        return Monster(name="Blaze", health=20, parry=20, criticalHit=5, damageMin=3, damageMax=7, xp=10)
    elif(name == "ender_dragon"):
        return Monster(name="Ender dragon", health=200, dodge=30, criticalHit=10, damageMin=6, damageMax=15, xp=500)
    else:
        items = ["zombie","bowman_skeleton","swordman_skeleton","spider","enderman","zombie_pigman","ghast","blaze","ender_gradon"]
        return generateMonster(name=items[int(expovariate(1/(len(items)//4))) % len(items)])