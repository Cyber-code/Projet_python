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


    """ Methods which modify inventory' organisation """

    def setLeftWeapon(self, item):
        if (self.inventory.weapon["leftHand"] != None):
            self.inventory.objects.append(self.inventory.weapon["leftHand"]) # Replace the actual left weapon to the inventory (player's list of objects)
        if (item.type == "weapon"):
            self.inventory.weapon["leftHand"] = item # Set the new left weapon

    def setRightWeapon(self, item):
        if (self.inventory.weapon["rightHand"] != None):
            self.inventory.objects.append(self.inventory.weapon["rightHand"]) # Replace the actual right weapon to the inventory (player's list of objects)
        if (item.type == "weapon"):
            self.inventory.weapon["rightHand"] = item # Set the new right weapon

    def setJewel1(self, item):
        if (self.inventory.jewels["jewel1"] != None):
            self.inventory.objects.append(self.inventory.jewels["jewel1"]) # Replace the actual jewel1 to the inventory (player's list of objects)
        if (item.type == "jewel"):
            self.inventory.jewels["jewel1"] = item # Set the new jewel1

    def setJewel2(self, item):
        if (self.inventory.jewels["jewel2"] != None):
            self.inventory.objects.append(self.inventory.jewels["jewel2"]) # Replace the actual jewel2 to the inventory (player's list of objects)
        if (item.type == "jewel"):
            self.inventory.jewels["jewel2"] = item # Set the new jewel2

    def setHeadArmor(self, item):
        if (self.inventory.armor["head"] != None):
            self.inventory.objects.append(self.inventory.armor["head"]) # Replace the actual head armor to the inventory (player's list of objects)
        if (item.type == "head"):
            self.inventory.armor["head"] = item # Set the new head armor

    def setChestArmor(self, item):
        if (self.inventory.armor["chest"] != None):
            self.inventory.objects.append(self.inventory.armor["chest"]) # Replace the actual chest armor to the inventory (player's list of objects)
        if (item.type == "chest"):
            self.inventory.armor["chest"] = item # Set the new chest armor

    def setArmsArmor(self, item):
        if (self.inventory.armor["arms"] != None):
            self.inventory.objects.append(self.inventory.armor["arms"]) # Replace the actual arms armor to the inventory (player's list of objects)
        if (item.type == "arms"):
            self.inventory.armor["arms"] = item # Set the new arms armor

    def setLegsArmor(self, item):
        if (self.inventory.armor["legs"] != None):
            self.inventory.objects.append(self.inventory.armor["legs"]) # Replace the actual legs armor to the inventory (player's list of objects)
        if (item.type == "legs"):
            self.inventory.armor["legs"] = item # Set the new legs armor

    def setFeetArmor(self, item):
        if (self.inventory.armor["feet"] != None):
            self.inventory.objects.append(self.inventory.armor["feet"]) # Replace the actual feet armor to the inventory (player's list of objects)
        if (item.type == "feet"):
            self.inventory.armor["feet"] = item # Set the new feet armor


    def showInfo(self):
        return "\nPlayer: "+ Character.showInfo(self) + "\nMaximum health: "+str(self.maxHealth)+ "\n"

    """ This method show the whole player's inventory """
    def showInventory(self):
        leftHand = "\nLeft hand weapon: "
        if(self.inventory.weapon["leftHand"] == None):
            leftHand += str(None)
        else:
            leftHand += self.inventory.weapon["leftHand"].name + " (" + str(self.inventory.weapon["leftHand"].value) + " gold, " + str(self.inventory.weapon["leftHand"].damage) + " damages)"

        rightHand = "   Right hand weapon: "
        if(self.inventory.weapon["rightHand"] == None):
            rightHand += str(None)
        else:
            rightHand += self.inventory.weapon["rightHand"].name + " (" + str(self.inventory.weapon["rightHand"].value) + " gold, " + str(self.inventory.weapon["rightHand"].damage) + " damages)"

        jewel1 = "\nJewel 1: "
        if(self.inventory.jewels["jewel1"] == None):
            jewel1 += str(None)
        else:
            jewel1 += self.inventory.jewels["jewel1"].name + " (" + str(self.inventory.jewels["jewel1"].value) + " gold, dodge: +" + str(self.inventory.jewels["jewel1"].dodge) + " %, parry: +" + str(self.inventory.jewels["jewel1"].parry) + " %, critical hit: +" + str(self.inventory.jewels["jewel1"].criticalHit) + " %, max health: +" + str(self.inventory.jewels["jewel1"].maxHealth) + " %)"

        jewel2 = "  Jewel 2: "
        if(self.inventory.jewels["jewel2"] == None):
            jewel2 += str(None)
        else:
            jewel2 += self.inventory.jewels["jewel2"].name + " (" + str(self.inventory.jewels["jewel2"].value) + " gold, dodge: +" + str(self.inventory.jewels["jewel2"].dodge) + " %, parry: +" + str(self.inventory.jewels["jewel2"].parry) + " %, critical hit: +" + str(self.inventory.jewels["jewel2"].criticalHit) + " %, max health: +" + str(self.inventory.jewels["jewel2"].maxHealth) + " %)"

        headArmor = "\nHead armor: "
        if(self.inventory.armor["head"] == None):
            headArmor += str(None)
        else:
            headArmor += self.inventory.armor["head"].name + " (" + str(self.inventory.armor["head"].value) + " gold, armor: +" + str(self.inventory.armor["head"].armor) + " %)"

        chestArmor = "   Chest armor: "
        if(self.inventory.armor["chest"] == None):
            chestArmor += str(None)
        else:
            chestArmor += self.inventory.armor["chest"].name + " (" + str(self.inventory.armor["chest"].value) + " gold, armor: +" + str(self.inventory.armor["chest"].armor) + " %)"

        armsArmor = "   Arms armor: "
        if(self.inventory.armor["arms"] == None):
            armsArmor += str(None)
        else:
            armsArmor += self.inventory.armor["arms"].name + " (" + str(self.inventory.armor["arms"].value) + " gold, armor: +" + str(self.inventory.armor["arms"].armor) + " %)"

        legsArmor = "   Legs armor: "
        if(self.inventory.armor["legs"] == None):
            legsArmor += str(None)
        else:
            legsArmor += self.inventory.armor["legs"].name + " (" + str(self.inventory.armor["legs"].value) + " gold, armor: +" + str(self.inventory.armor["legs"].armor) + " %)"

        feetArmor = "   Feet armor: "
        if(self.inventory.armor["feet"] == None):
            feetArmor += str(None)
        else:
            feetArmor += self.inventory.armor["feet"].name + " (" + str(self.inventory.armor["feet"].value) + " gold, armor: +" + str(self.inventory.armor["feet"].armor) + " %)"

        objects = "\n\nObjects: "
        for elmt in self.inventory.objects:
            objects += "\n"+ elmt.name + " (" + str(elmt.value) + " gold"
            if(elmt.type == "weapon"):
                objects += ", " + str(elmt.damage) + " damages)"
            elif(elmt.type == "jewel"):
                objects += ", dodge: +" + str(elmt.dodge) + " %, parry: +" + str(elmt.parry) + " %, critical hit: +" + str(elmt.criticalHit) + " %, max health: +" + str(elmt.maxHealth) + " %)"
            elif(elmt.type in ["head", "chest", "arms", "legs", "feet"]):
                objects += ", armor: +" + str(elmt.armor) + " %)"
            elif(elmt.type == "consumable"):
                objects += ", health: +" + str(elmt.health) + " PV, shield: +" + str(elmt.shield) + " , mana: +" + str(elmt.mana) + " MP, xp: +" + str(elmt.xp) + ")"
            else:
                objects += "Error: ObjectType not implemented)"

        return "\n\n---------------------------------------- {}'s inventory ----------------------------------------".format(self.name) + "\nGold: "+ str(self.inventory.gold) + leftHand + rightHand + jewel1 + jewel2 + headArmor + chestArmor + armsArmor + legsArmor + feetArmor + objects + "\n" + "".join(["-" for i in range(len("\n\n---------------------------------------- {}'s inventory ----------------------------------------".format(self.name))-1)])