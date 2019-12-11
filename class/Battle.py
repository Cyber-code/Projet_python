from Monster import Monster
from Player import Player

""" Battle class instantiate a battle object where the player figth a monster """
class Battle:
    def __init__(self, player, monster):
        self.player = player
        self.monster = monster

    """ This method launch the battle """
    def run(self):
        print("\nYou enter into the battle against a {}.".format(self.monster.name))
        print(self.monster.showInfo())
        while(self.monster.isAlive() and self.player.isAlive()):
            
            # Player attacks the monster
            action = False
            while(action == False):
                (action, damages) = self.selectAction()
            self.monster.getDamages(damages)
            print(self.monster.showBars())

            if(self.monster.isAlive()):
                print("\n", self.monster.name, " attacks !")
                self.player.getDamages(self.monster.hit())
                print(self.player.showBars())

        # Player alive, monster dead
        if(self.player.isAlive()):
            print("\nWell done, you killed the {}.".format(self.monster.name))
            self.player.shield = self.player.maxShield  # Reaload the player's shield

            items = self.monster.dropItems()
            print("{} got {} xp.".format(self.player.name, str(items[0])))
            print("{} got {} gold.".format(self.player.name, str(items[1])))
            self.player.addXp(items[0])
            self.player.inventory.gold += items[1]
            for objects in items[2]:
                print("{} got {}.".format(self.player.name, objects.showInfo()))
                self.player.inventory.objects.append(objects)
            
            print(self.player.showInventory())
            return True
        # Player dead, monster alive
        else:
            print("\nYou have been killed by the {}.".format(self.monster.name))
            return False


    """ This method allows the player to choose an action during a battle """
    def selectAction(self):
        print("\nSelect your action")
        print("1 - Attack with weapon")
        print("2 - Throw a spell")
        print("3 - Use a consumable")
        print("4 - Equip with an object")
        print("5 - Take off an object")
        print("6 - Show bars (health, shield, mana)")
        print("7 - Do nothing")

        choice = str()
        while(choice not in ["1","2","3","4","5","6","7"]):
            choice = input("Your action: ")

        print("--------------------------------------------------")
        choice = int(choice)

        # Fight with weapon
        if(choice == 1):
            choice2 = self.selectWeapon()
            if(choice2 == 1):
                damages = self.player.hit("leftHand")
                return (True, damages)
            elif(choice2 == 2):
                damages = self.player.hit("rightHand")
                return (True, damages)
            else:
                return (False, 0)
        # Throw a spell
        elif(choice == 2):
            choice2 = self.selectSpell()
            if(choice2 == 1):
                damages = self.player.throwSpell("Fireball")
                if (damages == 0):
                    return (False, 0)
                else:
                    return (True, damages)
            elif(choice2 == 2):
                damages = self.player.throwSpell("Lightning")
                if (damages == 0):
                    return (False, 0)
                else:
                    return (True, damages)
            else:
                return (False, 0)
        # Use a consumable
        elif(choice == 3):
            choice2 = self.selectConsumable()
            if(choice2 != -1):
                self.player.use(choice2)
            return (False, 0)
        # Equip with an object
        elif(choice == 4):
            (choice2, slot) = self.selectObjectToEquip()
            if(choice2 > -1):
                self.player.equipItem(self.player.inventory.objects[choice2], slot)
            return (False, 0)
        # Take off an object
        elif(choice == 5):
            choice2 = self.selectObjectToDequip()
            if(choice2 != None):
                self.player.dequipItem(choice2)
            return (False, 0)
        # Show player's bars
        elif(choice == 6):
            print(self.player.showBars())
            return (False, 0)
        # Do nothing
        else:
            return (True, 0)

    """ This method allows the player to choose a weapon """
    def selectWeapon(self):
        print("\nSelect your weapon:")
        print("0 - Previous")
        if(self.player.inventory.weapon["leftHand"] == None):
            leftHand = "None"
        else:
            leftHand = self.player.inventory.weapon["leftHand"].showInfo()
        print("1 - Attack with {}".format(leftHand))
        if(self.player.inventory.weapon["rightHand"] == None):
            rightHand = "None"
        else:
            rightHand = self.player.inventory.weapon["rightHand"].showInfo()
        print("2 - Attack with {}".format(rightHand))

        choice = str()
        while(choice not in ["0","1","2"]):
            choice = input("Your weapon: ")
        print("--------------------------------------------------")
        return (int(choice))
        
    """ This method allows the player to choose a spell """
    def selectSpell(self):
        print("\nSelect the spell to throw: ")
        print("0 - Previous")
        print("1 - Throw a Fireball  (Damage: 2, Mana: 5)")
        print("2 - Throw a Lightning (Damage: 5, Mana: 10)")

        choice = str()
        while(choice not in ["0","1","2"]):
            choice = input("Your spell: ")
        print("--------------------------------------------------")
        return int(choice)

    """ This method allows the player to use a consumable """
    def selectConsumable(self):
        print("\nSelect the consumable to use: ")
        print("-1 -  Previous")
        consumableIndex = ['-1']
        for i,objects in enumerate(self.player.inventory.objects):
            if(objects.type == "consumable"):
                print(i, " - ", objects.showInfo())
                consumableIndex.append(str(i))

        choice = str()
        while(choice not in consumableIndex):
            choice = input("Consumable to use: ")
        print("--------------------------------------------------")
        return int(choice)


    """ This method equip the player with an object """
    def selectObjectToEquip(self):
        print("\nSelect the object to equip: ")
        print("-1 -  Previous")
        objectIndex = ['-1']
        for i,objects in enumerate(self.player.inventory.objects):
            if(objects.type in ["head","chest","arms","legs","feet","weapon","jewel"]):
                print(i, " - ", objects.showInfo())
                objectIndex.append(str(i))

        choice = str()
        while(choice not in objectIndex):
            choice = input("Object to equip: ")
        print("--------------------------------------------------")

        slot = "0"
        if(choice != "-1" and self.player.inventory.objects[int(choice)].type in ["jewel","weapon"]):
            print("\nSelect the slot : ")
            print("1 -  Slot 1")
            print("2 -  Slot 2")
            while(slot not in ["1","2"]):
                slot = input("Slot : ")
            print("--------------------------------------------------")

        return (int(choice), int(slot))

    """ This method allows the player to take off an object """
    def selectObjectToDequip(self):
        print("\nSelect the object to take off: ")
        print("-1 -  Previous")
        objectIndex = ['-1']
        equipement = [obj for obj in [self.player.inventory.weapon["leftHand"], self.player.inventory.weapon["rightHand"], self.player.inventory.jewels["jewel1"], self.player.inventory.jewels["jewel2"], self.player.inventory.armor["head"], self.player.inventory.armor["chest"], self.player.inventory.armor["arms"], self.player.inventory.armor["legs"], self.player.inventory.armor["feet"]] if obj != None]
        for i,objects in enumerate(equipement):
            print(i, " - ", objects.showInfo())
            objectIndex.append(str(i))

        choice = str()
        while(choice not in objectIndex):
            choice = input("Object to take off: ")
        print("--------------------------------------------------")

        if(int(choice) == -1):
            return None
        else:
            return equipement[int(choice)]