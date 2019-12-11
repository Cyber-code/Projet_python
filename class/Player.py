from Character import Character
from Inventory import Inventory
from math import sqrt
from Statistics import Statistics
from Success import Success

""" Player class instantiate a player object controled by the user """
class Player(Character):
    def __init__(self, name="Player", health=20, shield=10, dodge=0,
                 parry=0, criticalHit=1, mana=10, damageMin=1,
                 damageMax=2, armor=0, xp=0, inventory=Inventory()):
        Character.__init__(self, name, health, shield, dodge, parry, criticalHit, mana, damageMin, damageMax, armor, xp, inventory)

        self.statistics = Statistics()
        self.success = {"monster_hunter":Success(name="Monster hunter"), "commercial":Success(name="Commercial"), "lucky":Success(name="Lucky"), "compulsive_buyer":Success(name="Compulsive buyer"), "vendor":Success(name="Vendor on the run"), "consumer":Success(name="Consumer"), "the_end":Success(name="The End")}

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
            for i in range(self.level-level):
                self.levelUp()
                print(i)

    """ 
    This method allows the player to buy an items, return the value of the item if it is bought or return 0 otherwise 
    If the player has enought gold, then the item is added to player's inventory
    """
    def buyItem(self, item):
        if(self.inventory.gold >= item.value):
            self.inventory.gold -= item.value
            self.addItem(item)
            return item.value
        else:
            print("\nNot enought gold !\n")
            return 0

    """ This methods allows the player to take off a weapon, jewel or armor """
    def dequipItem(self, item):
        if(item != None):
            if(item == self.inventory.weapon["leftHand"]):
                self.inventory.weapon["leftHand"] = None
            elif(item == self.inventory.weapon["rightHand"]):
                self.inventory.weapon["rightHand"] = None
            elif(item == self.inventory.jewels["jewel1"]):
                self.inventory.jewels["jewel1"] = None
            elif(item == self.inventory.jewels["jewel2"]):
                self.inventory.jewels["jewel2"] = None
            elif(item == self.inventory.armor["head"]):
                self.inventory.armor["head"] = None
            elif(item == self.inventory.armor["chest"]):
                self.inventory.armor["chest"] = None
            elif(item == self.inventory.armor["arms"]):
                self.inventory.armor["arms"] = None
            elif(item == self.inventory.armor["legs"]):
                self.inventory.armor["legs"] = None
            elif(item == self.inventory.armor["feet"]):
                self.inventory.armor["feet"] = None
            else:
                pass
            self.addItem(item)
            return True
        else:
            return False

    """ This methods allows the player to equip himself with a weapon, jewel or armor """
    def equipItem(self, item, slot):
        if(item in self.inventory.objects):
            if(item.type == "weapon" and slot == 1):
                self.setWeapon(item, slot="leftHand")
            elif(item.type == "weapon" and slot == 2):
                self.setWeapon(item, slot="rightHand")
            elif(item.type == "jewel" and slot == 1):
                self.setJewel(item, slot="jewel1")
            elif(item.type == "jewel" and slot == 2):
                self.setJewel(item, slot="jewel2")
            elif(item.type in ["head", "chest", "arms", "legs", "feet"]):
                self.setArmor(item)
            else:
                pass
            self.inventory.objects.remove(item)
            return True
        else:
            return False

    """ This method allows the player to sell an items, return True if the item is not None or return False otherwise """
    def sellItem(self, item):
        if(item != None):
            self.inventory.gold += item.value
            self.inventory.objects.remove(item)
            return True
        else:
            return False


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

    def showStatistics(self):
        return "\n{}'s statistics:\nMonsters killed: {}\nMerchants met: {}\nChests found: {}\nObjects bought: {}\nObjects sold: {}\nConsumables used: {}\nEnder dragon killed: {}\n".format(self.name, self.statistics.monstersKilled, self.statistics.merchantsMet, self.statistics.chestsFound, self.statistics.objectsBought, self.statistics.objectsSold, self.statistics.consumablesUsed, self.statistics.enderDragonsKilled)

    def showSuccess(self):
        success = ""
        for elt in self.success:
            success += self.success[elt].showInfo()
        return "\n{}'s success: {}".format(self.name, success)