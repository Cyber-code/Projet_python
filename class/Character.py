from Inventory import Inventory
from random import randint
from math import sqrt
from Spell import Spell

class Character:
    def __init__(self, name, health, shield, dodge,
                 parry, criticalHit, mana, damageMin,
                 damageMax, armor, xp, inventory):
        self.name = name
        self.health = health
        self.shield = shield    
        self.dodge = dodge              # Chance of dodge (%) to avoid attacks (damages are nullfied)
        self.parry = parry              # Change of parry (%) to reduce amount of damage by 70%
        self.criticalHit = criticalHit  # Chance of critical hit (%) to double the amount of damage inflicted
        self.mana = mana                # Magic point, to use spells
        self.damageMin = damageMin      # Mininum damage that the character is able to inflict
        self.damageMax = damageMax      # Maximum damage "                                   "
        self.armor = armor              # Armor point, reduced incoming damage by a percentage
        self.level = 0                  # Level, each leave increase a small of the characteristics above
        self.xp = 0                     # Experience bar, when filled, increase cureent level by one
        self.inventory = inventory
        self.maxLevel = 40

        self.maxHealth = health
        self.maxShield = shield
        self.maxMana = mana

        self.addXp(xp) # To update the level in function of xp

    """ 
    This method is called when the player killed
    monsters and he earn some xp
    """
    def addXp(self, xp):
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

    """ This method calculates damages given by a Character """
    def hit(self, hand):
        damages = int()
        if (hand in ["leftHand", "rightHand"] and self.inventory.weapon[hand] != None):
            damages += self.inventory.weapon[hand].damage
        damages += randint(self.damageMin, self.damageMax)
        if (randint(0, 100) <= self.criticalHit):
            damages *= 2
            print("Critical hit !")
        return damages

    """ This method selects spell and calculates its damages """
    def throwSpell(self, spell):
        damages = spell.damage
        if (0 < spell.mana <= self.mana):
            self.mana -= spell.mana
        else:
            print("\nNot enought mana !\n")

        if (randint(0, 100) <= self.criticalHit):
            damages *= 2
            print("Critical hit !")
        return damages


    """ This method calculate the getting amount of damages """
    def getDamages(self, damages):
        if(randint(0, 100) <= self.dodge):
            damages = 0
            print(self.name + " dodges the attack.")
        elif(randint(0, 100) <= self.parry):
            damages = int(damages * 0.3)
            print(self.name + " parries the attack, damages are reduced by 70 %.")

        if(self.shield - damages < 0):
            self.health = self.health - (damages - self.shield)
            self.shield = 0
        else:
            self.shield -= damages

        return self.isAlive()


    def isAlive(self):
        if self.health > 0:
            return True
        else:
            return False


    """ Methods which modify inventory's organisation """

    def setWeapon(self, item, hand="leftHand"):
        if (item.type == "weapon" and hand in ["leftHand", "rightHand"]):
            if (self.inventory.weapon[hand] != None):
                self.inventory.objects.append(self.inventory.weapon[hand]) # Replace the actual left or right weapon to the inventory (player's list of objects)

            self.inventory.weapon[hand] = item # Set the new left or right weapon
            return True
        else:
            return False


    def setJewel(self, item, slot="jewel1"):
        if (item.type == "jewel" and slot in ["jewel1", "jewel2"]):
            if (self.inventory.jewels[slot] != None):
                # Restore the default character parameters
                self.dodge -= self.inventory.jewels[slot].dodge
                self.parry -= self.inventory.jewels[slot].parry
                self.criticalHit -= self.inventory.jewels[slot].criticalHit
                self.maxHealth -= self.inventory.jewels[slot].maxHealth
                self.inventory.objects.append(self.inventory.jewels[slot]) # Replace the actual jewel to the inventory (player's list of objects)
            
            # Set the new character parameters
            self.inventory.jewels[slot] = item # Set the new jewel
            self.dodge += self.inventory.jewels[slot].dodge
            self.parry += self.inventory.jewels[slot].parry
            self.criticalHit += self.inventory.jewels[slot].criticalHit
            self.maxHealth += self.inventory.jewels[slot].maxHealth
            return True
        else:
            return False


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

    """ This method shows player's health, shield and mana """
    def showBars(self):
        return "\n{} (lvl {}, {} xp)".format(self.name, self.level, self.xp) + "\nHearth: {} / {}".format(self.health, self.maxHealth) + "\nShield: {} / {}".format(self.shield, self.maxShield) + "\nMana: {} / {}".format(self.mana, self.maxMana)


    def showInfo(self):
        return self.showBars() + "\nDamages: {} - {}\nDodge: {} %\nParry: {} %\nCritical hit: {} %\nArmor: {} %\n".format(self.damageMin, self.damageMax, self.dodge, self.parry, self.criticalHit, self.armor)

    """ This method shows the whole player's inventory """
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

        jewel2 = "\nJewel 2: "
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
