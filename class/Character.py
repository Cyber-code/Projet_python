from Inventory import Inventory
from random import randint
from math import sqrt
from Spell import generateSpell

class Character:
    """ Chacracter class instantiate character object who can be a Player, a Monster or a Merchant. """
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
        self.inventory = Inventory()
        self.maxLevel = 40

        self.maxHealth = health
        self.maxShield = shield
        self.maxMana = mana

        self.addXp(xp) # To update the level in function of xp


    def addHealth(self, health):
        """ This method is used to regenerate an amount of health to the character whithout exceeding the maximun amount of health (maxHealth). """
        if(self.health + health >= self.maxHealth):
            self.health = self.maxHealth
        else:
            self.health += health
        return True


    def addGold(self, gold=0):
        """ This method is used to give a lot of gold to the character. """
        self.inventory.gold += gold
        return True


    def addItem(self, item):
        """ This method is used to add an item/object to the character's inventory. """
        self.inventory.objects.append(item)
        return True


    def addMana(self, mana):
        """ This method is used to regenerate an amount of mana to the character whithout exceeding the maximun amount of mana (maxMana). """
        if(self.mana + mana >= self.maxMana):
            self.mana = self.maxMana
        else:
            self.mana += mana
        return True


    def addShield(self, shield):
        """ This method is used to regenerate an amount of shield to the character whithout exceeding the maximun amount of shield (maxShield). """
        if(self.shield + shield >= self.maxShield):
            self.shield = self.maxShield
        else:
            self.shield += shield
        return True


    def addXp(self, xp):
        """ This method is used to give a lot of xp to the character and to update his level. """
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
        return True


    def hit(self, hand="leftHand"):
        """ This method calculates the amount of damages given by the character depending on the choosen hand (leftHand or rightHand). """
        damages = int()
        if (hand in ["leftHand", "rightHand"] and self.inventory.weapon[hand] != None):
            damages += self.inventory.weapon[hand].damage
        damages += randint(self.damageMin, self.damageMax)
        if (randint(0, 100) <= self.criticalHit):
            damages *= 2
            print("Critical hit !")
        return damages


    def throwSpell(self, spellName="Fireball"):
        """ This method calculates the amount of damages given by the character depending on the choosen spell (lightning or fireball). """
        if(spellName == "Lightning"):
            spell = generateSpell("lightning")
        else:
            spell = generateSpell(name="fireball")

        damages = spell.damage
        if (0 < spell.mana <= self.mana):
            self.mana -= spell.mana
        else:
            print("\nNot enought mana !\n")
            damages = 0

        if (randint(0, 100) <= self.criticalHit):
            damages *= 2
            print("Critical hit !")
        return damages


    def getDamages(self, damages):
        """ 
        This method calculate incoming amount of damages and could be deleted or reduced if the character dodges or parries the attack.
        Damages are also reduces by percentage of armor of the player.
        Damages are shared first on the character's shield and after on his health. 

        Return True if the character is still alive.
        """
        if(randint(0, 100) <= self.dodge):
            damages = 0
            print(self.name + " dodges the attack.")
        elif(randint(0, 100) <= self.parry):
            damages = int(damages * 0.3)
            print(self.name + " parries the attack, damages are reduced by 70 %.")

        totalArmor = self.armor
        for slot in self.inventory.armor:
            if(self.inventory.armor[slot] != None):
                totalArmor += self.inventory.armor[slot].armor
        if(totalArmor > 90):
            totalArmor = 90

        damages = int(damages * (1 - totalArmor/100))
        if(self.shield - damages < 0):
            self.health = self.health - (damages - self.shield)
            self.shield = 0
        else:
            self.shield -= damages

        return self.isAlive()


    def isAlive(self):
        """ Return True if the character has more than 0 health or False otherwise. """
        if self.health > 0:
            return True
        else:
            return False


    def setWeapon(self, item, slot="leftHand"):
        """ 
        Replace the actual weapon in the character's inventory and equip the character with a weapon in the chosen slot 
        (leftHand or rightHand).
        """

        if (item == None or (item.type == "weapon" and slot in ["leftHand", "rightHand"])):
            if (self.inventory.weapon[slot] != None):
                self.inventory.objects.append(self.inventory.weapon[slot]) # Replace the actual left or right weapon to the inventory (player's list of objects)

            self.inventory.weapon[slot] = item # Set the new left or right weapon
            return True
        else:
            return False


    def setJewel(self, item, slot="jewel1"):
        """ 
        Replace the actual jewel in the character's inventory and equip the character with a jewel in the chosen slot 
        (jewel1 or jewel2).
        """

        if (item == None or (item.type == "jewel" and slot in ["jewel1", "jewel2"])):
            if (self.inventory.jewels[slot] != None):
                # Restore the default character parameters
                self.dodge -= self.inventory.jewels[slot].dodge
                self.parry -= self.inventory.jewels[slot].parry
                self.criticalHit -= self.inventory.jewels[slot].criticalHit
                self.maxHealth -= self.inventory.jewels[slot].maxHealth
                self.health -= self.inventory.jewels[slot].maxHealth

                self.inventory.objects.append(self.inventory.jewels[slot]) # Replace the actual jewel to the inventory (player's list of objects)
            
            self.inventory.jewels[slot] = item # Set the new jewel
            
            # Set the new character parameters
            if(item != None):
                self.dodge += self.inventory.jewels[slot].dodge
                self.parry += self.inventory.jewels[slot].parry
                self.criticalHit += self.inventory.jewels[slot].criticalHit
                self.maxHealth += self.inventory.jewels[slot].maxHealth
                self.health += self.inventory.jewels[slot].maxHealth
            return True
        else:
            return False


    def setArmor(self, item):
        """ 
        Replace the actual armor in the character's inventory and equip the character with an armor in the chosen slot 
        (head, chest, arms, legs or feet).
        """
        if (item.type in ["head", "chest", "arms", "legs", "feet"]):
            if (self.inventory.armor[item.type] != None):
                self.inventory.objects.append(self.inventory.armor[item.type]) # Replace the actual armor to the inventory (player's list of objects)
            self.inventory.armor[item.type] = item # Set the new armor
            return True
        else:
            return False


    def showBars(self):
        """ This method return a string containing character's health, shield and mana. """
        return "\n{} (lvl {}, {} xp)".format(self.name, self.level, self.xp) + "\nHealth: {} / {}".format(self.health, self.maxHealth) + "\nShield: {} / {}".format(self.shield, self.maxShield) + "\nMana: {} / {}".format(self.mana, self.maxMana)


    def showInfo(self):
        """ This method return a string containing character's parameters. """
        totalArmor = self.armor
        for slot in self.inventory.armor:
            if(self.inventory.armor[slot] != None):
                totalArmor += self.inventory.armor[slot].armor
        if(totalArmor > 90):
            totalArmor = 90
        return self.showBars() + "\nDamages: {} - {}\nDodge: {} %\nParry: {} %\nCritical hit: {} %\nArmor: {} %\n".format(self.damageMin, self.damageMax, self.dodge, self.parry, self.criticalHit, totalArmor)


    def showInventory(self):
        """ This method return a string containing character's inventory. """
        leftHand = "\n\nLeft hand weapon: "
        if(self.inventory.weapon["leftHand"] == None):
            leftHand += str(None)
        else:
            leftHand += self.inventory.weapon["leftHand"].name + " (" + str(self.inventory.weapon["leftHand"].value) + " gold, " + str(self.inventory.weapon["leftHand"].damage) + " damages)"

        rightHand = "\nRight hand weapon: "
        if(self.inventory.weapon["rightHand"] == None):
            rightHand += str(None)
        else:
            rightHand += self.inventory.weapon["rightHand"].name + " (" + str(self.inventory.weapon["rightHand"].value) + " gold, " + str(self.inventory.weapon["rightHand"].damage) + " damages)"

        jewel1 = "\n\nJewel 1: "
        if(self.inventory.jewels["jewel1"] == None):
            jewel1 += str(None)
        else:
            jewel1 += self.inventory.jewels["jewel1"].name + " (" + str(self.inventory.jewels["jewel1"].value) + " gold, dodge: +" + str(self.inventory.jewels["jewel1"].dodge) + " %, parry: +" + str(self.inventory.jewels["jewel1"].parry) + " %, critical hit: +" + str(self.inventory.jewels["jewel1"].criticalHit) + " %, max health: +" + str(self.inventory.jewels["jewel1"].maxHealth) + " %)"

        jewel2 = "\nJewel 2: "
        if(self.inventory.jewels["jewel2"] == None):
            jewel2 += str(None)
        else:
            jewel2 += self.inventory.jewels["jewel2"].name + " (" + str(self.inventory.jewels["jewel2"].value) + " gold, dodge: +" + str(self.inventory.jewels["jewel2"].dodge) + " %, parry: +" + str(self.inventory.jewels["jewel2"].parry) + " %, critical hit: +" + str(self.inventory.jewels["jewel2"].criticalHit) + " %, max health: +" + str(self.inventory.jewels["jewel2"].maxHealth) + " %)"

        headArmor = "\n\nHead armor: "
        if(self.inventory.armor["head"] == None):
            headArmor += str(None)
        else:
            headArmor += self.inventory.armor["head"].name + " (" + str(self.inventory.armor["head"].value) + " gold, armor: +" + str(self.inventory.armor["head"].armor) + " %)"

        chestArmor = "\nChest armor: "
        if(self.inventory.armor["chest"] == None):
            chestArmor += str(None)
        else:
            chestArmor += self.inventory.armor["chest"].name + " (" + str(self.inventory.armor["chest"].value) + " gold, armor: +" + str(self.inventory.armor["chest"].armor) + " %)"

        armsArmor = "\nArms armor: "
        if(self.inventory.armor["arms"] == None):
            armsArmor += str(None)
        else:
            armsArmor += self.inventory.armor["arms"].name + " (" + str(self.inventory.armor["arms"].value) + " gold, armor: +" + str(self.inventory.armor["arms"].armor) + " %)"

        legsArmor = "\nLegs armor: "
        if(self.inventory.armor["legs"] == None):
            legsArmor += str(None)
        else:
            legsArmor += self.inventory.armor["legs"].name + " (" + str(self.inventory.armor["legs"].value) + " gold, armor: +" + str(self.inventory.armor["legs"].armor) + " %)"

        feetArmor = "\nFeet armor: "
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


    def use(self, consumableIndex):
        """ 
        This method allows the character to use a consumable and pop it from its inventory. 
        Return True if this object is a consumable or return False otherwise.
        """
        if(self.inventory.objects[consumableIndex].type == "consumable"):
            self.addHealth(self.inventory.objects[consumableIndex].health)
            self.addMana(self.inventory.objects[consumableIndex].mana)
            self.addShield(self.inventory.objects[consumableIndex].shield)
            self.addXp(self.inventory.objects[consumableIndex].xp)

            self.inventory.objects.pop(consumableIndex)
            return True

        else:
            return False