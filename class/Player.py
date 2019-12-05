from Character import Character
from Inventory import Inventory

""" Player class instantiate a player object controled by the user """
class Player(Character):
    def __init__(self, name="Player", health=20, shield=0, dodge=0,
                 parry=0, criticalHit=1, mana=10, damageMin=1,
                 damageMax=2, armor=0, level=1, xp=0, inventory=Inventory(),
                 maxHealth=20):
        Character.__init__(self, name, health, shield, dodge, parry, criticalHit, mana, damageMin, damageMax, armor, level, xp, inventory)
        self.maxHealth = maxHealth

    """ When the player uses a consumable which regerate his health """
    def addHealth(self, health):
        if(self.health + health >= self.maxHealth):
            self.health = self.maxHealth
        else:
            self.health += health

    """ This method is used to add an item/object to the player's inventory """
    def addItem(self, item):
        self.inventory.objects.append(item)

    """ 
    This method is called when the player killed
    monsters and he earn some xp
    """
    def addXp(self, xp):
        self.xp += xp

        # This dict corresponds for each level its xp to reach it
        lvl_xp = {1:0, 2:50, 3:100, 4:250, 5:500,
                6:750, 7:1000, 8:2500, 9:5000,
                10:7500, 11:10000, 12:25000, 13:50000,
                14:75000, 15:100000, 16:250000, 17:500000,
                18:750000, 19:1000000, 20:2500000}

        # We verify for each lvl above current level if we have enougth xp to levelup
        xp_temp = self.xp
        while xp_temp - lvl_xp[self.level + 1] > 0:
            if (self.xp >= lvl_xp[self.level + 1]):
                self.levelUp()
                xp_temp -= lvl_xp[self.level + 1]

    """ When the player earned enought xp, he gained a level """
    def levelUp(self):
        if self.level < self.maxLevel:
            self.level += 1
        
        croissance = 1.2

        # These stats are increase about 20% (arbitrary)
        self.maxHealth = int(croissance*self.maxHealth)
        self.health = int(croissance*self.health)
        self.shield = int(croissance*self.shield)
        self.mana = int(croissance*self.mana)
        self.damageMin = int(croissance*self.damageMin)
        self.damageMax = int(croissance*self.damageMax)

        # These stats are inscrease (arbitrary) whithout exceed 20 (of the stat)
        if(self.dodge < 20/croissance):
            self.dodge = int(croissance*self.dodge)

        if(self.parry < 20/croissance):
            self.parry = int(croissance*self.parry)
        
        if(self.criticalHit < 20/croissance):
            self.criticalHit = int(croissance*self.criticalHit)
        
        if(self.armor < 20/croissance):
            self.armor = int(croissance*self.armor)

    def showInfo(self):
        return "\nPlayer: "+ Character.showInfo(self) + "\nMaximum health: "+str(self.maxHealth)+ "\n"

    def showInventory(self):
        objects = "\nObjects: "
        for elmt in self.inventory.objects:
            objects += str(elmt) + "  "
        return "\n{}'s inventory: ".format(self.name) + "\nGold: "+ str(self.inventory.gold) + "\nLeft hand weapon: {}  Right hand weapon: {}".format(self.inventory.weapon["leftHand"], self.inventory.weapon["rightHand"]) + "\nJewel 1: {}  Jewel 2: {}".format(self.inventory.jewels["jewel1"], self.inventory.jewels["jewel2"]) + "\nHead armor: {}  Chest armor: {}  Arms armor: {}  Legs armor: {}  Feet armor: {}".format(self.inventory.armor["head"], self.inventory.armor["chest"], self.inventory.armor["arms"], self.inventory.armor["legs"], self.inventory.armor["feet"]) + objects +"\n"