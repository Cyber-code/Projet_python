from Character import Character
from Inventory import Inventory
from math import sqrt

""" Player class instantiate a player object controled by the user """
class Player(Character):
    def __init__(self, name="Player", health=20, shield=10, dodge=0,
                 parry=0, criticalHit=1, mana=10, damageMin=1,
                 damageMax=2, armor=0, xp=0, inventory=Inventory()):
        Character.__init__(self, name, health, shield, dodge, parry, criticalHit, mana, damageMin, damageMax, armor, xp, inventory)

    """ 
    This method is called when the player killed
    monsters and he earn some xp
    """
    def addXp(self, xp):
        level = self.level
        self.xp += xp
        # From lvl 0 to 16
        if(self.xp < 353):
            self.level = int((-6 + sqrt(36+4*self.xp))//2)
        # From lvl 17 to 31
        elif(self.xp < 1508):
            self.level = int((40.5 + sqrt((40.5)**2 -3600 + 10*self.xp))//5)
        # From 32 to ...
        else:
            self.level = int((162.5 + sqrt((162.5)**2 -39960+18*self.xp))//9)

        if (level < self.level):
            self.levelUp()


    """ Only for the player, when he earns enought xp, then he gains a level """
    def levelUp(self):
        factor = 1.2
        self.maxHealth = int(factor*self.maxHealth)
        self.health = int(factor*self.health)
        self.maxShield = int(factor*self.maxShield)
        self.shield = int(factor*self.shield)
        self.maxMana = int(factor*self.maxMana)
        self.mana = int(factor*self.mana)
        self.damageMin += 1
        self.damageMax += 1
        self.dodge += 1
        self.parry += 1
        self.criticalHit += 1
        self.armor += 1