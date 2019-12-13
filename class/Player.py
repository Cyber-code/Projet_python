from Character import Character
from Inventory import Inventory
from math import sqrt
from Statistics import Statistics
from Success import Success
from DBMineRPG import *

class Player(Character):
    """ Player class instantiate a player object controled by the user. """
    def __init__(self, name="Player", health=20, shield=10, dodge=0,
                 parry=0, criticalHit=1, mana=10, damageMin=1,
                 damageMax=2, armor=0, xp=0, inventory=Inventory()):
        Character.__init__(self, name, health, shield, dodge, parry, criticalHit, mana, damageMin, damageMax, armor, xp, inventory)

        self.statistics = Statistics()
        self.success = {"monster_hunter":Success(name="Monster hunter"), "commercial":Success(name="Commercial"), "lucky":Success(name="Lucky"), "compulsive_buyer":Success(name="Compulsive buyer"), "vendor":Success(name="Vendor on the run"), "consumer":Success(name="Consumer"), "the_end":Success(name="The End")}


    def addXp(self, xp):
        """ 
        This method is used to give a lot of xp to the player and to update his level.
        If the player gains a level, then his stats are increased.
        """
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


    def buyItem(self, item):
        """ 
        This method allows the player to buy an items, return the value of the item if it is bought or return 0 otherwise.
        If the player has enought gold, then the item is added to player's inventory.
        """
        if(self.inventory.gold >= item.value):
            self.inventory.gold -= item.value
            self.addItem(item)
            self.statistics.objectsBought += 1
            return item.value
        else:
            print("\nNot enought gold !\n")
            return 0


    def dequipItem(self, item):
        """ This methods allows the player to take off a weapon, jewel or armor. """
        if(item != None):
            if(item == self.inventory.weapon["leftHand"]):
                self.setWeapon(item=None, slot="leftHand")

            elif(item == self.inventory.weapon["rightHand"]):
                self.setWeapon(item=None, slot="rightHand")

            elif(item == self.inventory.jewels["jewel1"]):
                self.setJewel(item=None, slot="jewel1")

            elif(item == self.inventory.jewels["jewel2"]):
                self.setJewel(item=None, slot="jewel2")

            elif(item == self.inventory.armor["head"]):
                self.inventory.armor["head"] = None
                self.addItem(item)

            elif(item == self.inventory.armor["chest"]):
                self.inventory.armor["chest"] = None
                self.addItem(item)

            elif(item == self.inventory.armor["arms"]):
                self.inventory.armor["arms"] = None
                self.addItem(item)

            elif(item == self.inventory.armor["legs"]):
                self.inventory.armor["legs"] = None
                self.addItem(item)

            elif(item == self.inventory.armor["feet"]):
                self.inventory.armor["feet"] = None
                self.addItem(item)
            return True
        else:
            return False


    def equipItem(self, item, slot):
        """ This methods allows the player to equip himself with a weapon, jewel or armor. """
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


    def sellItem(self, item):
        """ This method allows the player to sell an items, return True if the item is not None or return False otherwise. """
        if(item != None):
            self.inventory.gold += item.value
            self.inventory.objects.remove(item)
            self.statistics.objectsSold += 1
            return True
        else:
            return False


    def levelUp(self):
        """ This method increases player stats when he gains a level. """
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
        """ Return a string which contains player's statistics of the game. """
        return "\n{}'s statistics:\nMonsters killed: {}\nMerchants met: {}\nChests found: {}\nObjects bought: {}\nObjects sold: {}\nConsumables used: {}\nEnder dragon killed: {}\n".format(self.name, self.statistics.monstersKilled, self.statistics.merchantsMet, self.statistics.chestsFound, self.statistics.objectsBought, self.statistics.objectsSold, self.statistics.consumablesUsed, self.statistics.enderDragonsKilled)


    def showSuccess(self):
        """ Return a string which contains player's unlocked success. """
        success = ""
        for elt in self.success:
            success += self.success[elt].showInfo()
        return "\n{}'s success: {}".format(self.name, success)


    def updateSuccess(self):
        """ This method updates unlocked success if the player has required statitics. """
        if(self.statistics.monstersKilled > 9):
            self.success["monster_hunter"].unlock = True
        if(self.statistics.merchantsMet > 9):
            self.success["commercial"].unlock = True
        if(self.statistics.chestsFound > 0):
            self.success["lucky"].unlock = True
        if(self.statistics.objectsBought > 9):
            self.success["compulsive_buyer"].unlock = True
        if(self.statistics.objectsSold > 9):
            self.success["vendor"].unlock = True
        if(self.statistics.consumablesUsed > 9):
            self.success["consumer"].unlock = True
        if(self.statistics.enderDragonsKilled > 0):
            self.success["the_end"].unlock = True

    def save(self):
        leftHand="None" 
        rightHand="None"
        jewel1="None"
        jewel2="None"
        head="None"
        chest="None" 
        arms="None"
        legs="None"
        feet="None"

        if(self.inventory.weapon["leftHand"] != None):
            leftHand = self.inventory.weapon["leftHand"].libelle
        if(self.inventory.weapon["rightHand"] != None):
            rightHand = self.inventory.weapon["rightHand"].libelle
        if(self.inventory.jewels["jewel1"] != None):
            jewel1 = self.inventory.jewels["jewel1"].libelle
        if(self.inventory.jewels["jewel2"] != None):
            jewel2 = self.inventory.jewels["jewel2"].libelle
        if(self.inventory.armor["head"] != None):
            head = self.inventory.armor["head"].libelle
        if(self.inventory.armor["chest"] != None):
            chest = self.inventory.armor["chest"].libelle
        if(self.inventory.armor["arms"] != None):
            arms = self.inventory.armor["arms"].libelle
        if(self.inventory.armor["legs"] != None):
            legs = self.inventory.armor["legs"].libelle
        if(self.inventory.armor["feet"] != None):
            feet = self.inventory.armor["feet"].libelle

        print(self.maxHealth) 
        updatePlayerData(self.name, self.health, self.shield, self.dodge, self.parry, self.criticalHit, self.mana, self.damageMin, self.damageMax, self.armor, self.xp, self.level, self.maxHealth, self.maxShield, self.maxMana)
        updateStatisticsData(getId(self.name), self.statistics.monstersKilled, self.statistics.merchantsMet, self.statistics.chestsFound, self.statistics.objectsBought, self.statistics.objectsSold, self.statistics.consumablesUsed, self.statistics.enderDragonsKilled)
        updateInventoryData(getId(self.name), self.inventory.gold, leftHand, rightHand, jewel1, jewel2, head, chest, arms, legs, feet)