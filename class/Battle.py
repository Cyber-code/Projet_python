from Interaction import Interaction
from Monster import Monster
from Player import Player

""" Battle class instantiate a battle object where the player figth a monster """
class Battle(Interaction):
    def __init__(self, player, monster):
        Interaction.__init__(self, player, monster)

    """ This method launch the battle """
    def run(self):
        print("\nYou enter into the battle against a {}.".format(self.mob.name))
        print(self.mob.showInfo())
        while(self.mob.isAlive() and self.player.isAlive()):
            
            # Player attacks the monster
            action = False
            while(action == False):
                (action, damages) = self.selectAction()
            self.mob.getDamages(damages)
            print(self.mob.showBars())

            if(self.mob.isAlive()):
                print("\n",self.mob.name," attacks !")
                self.player.getDamages(self.mob.hit())
                print(self.player.showBars())

        # Player alive, monster dead
        if(self.player.isAlive()):
            print("\nWell done, you killed the {}.".format(self.mob.name))
            if(self.mob.name == "Ender dragon"):
                self.player.statistics.enderDragonsKilled += 1
            self.player.statistics.monstersKilled += 1
            self.player.shield = self.player.maxShield  # Reaload the player's shield

            items = self.mob.dropItems()
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
            print("\nYou have been killed by the {}.".format(self.mob.name))
            return False


    """ This method allows the player to choose an action during a battle """
    def selectAction(self):
        print("\nSelect your action")
        print("0  - Do nothing")
        print("1  - Attack with weapon")
        print("2  - Throw a spell")
        print("3  - Use a consumable")
        print("4  - Equip with an object")
        print("5  - Take off an object")
        print("6  - Show bars (health, shield, mana)")
        print("7  - Show infos")
        print("8  - Show inventory")
        print("9  - Show statistics")
        print("10 - Show success")

        choice = str()
        while(choice not in [str(i) for i in range(11)]):
            choice = input("Your action: ")

        print("--------------------------------------------------")
        choice = int(choice)

        # Do nothing
        if(choice == 0):
            return (True, 0)

        # Fight with weapon
        elif(choice == 1):
            choice2 = self.selectWeapon()
            # Use weapon in the left hand
            if(choice2 == 1):
                damages = self.player.hit("leftHand")
            # Use weapon in the right hand
            elif(choice2 == 2):
                damages = self.player.hit("rightHand")
            return (True, damages)

        # Throw a spell
        elif(choice == 2):
            choice2 = self.selectSpell()
            # Throw a fireball
            if(choice2 == 1):
                damages = self.player.throwSpell("Fireball")
                if (damages == 0):
                    return (False, 0)
                else:
                    return (True, damages)
            # Throw a lightning
            elif(choice2 == 2):
                damages = self.player.throwSpell("Lightning")
                if (damages == 0):
                    return (False, 0)
                else:
                    return (True, damages)

        # Use a consumable
        elif(choice == 3):
            choice2 = self.selectConsumable()
            if(choice2 != -1):
                self.player.use(choice2)

        # Equip with an object
        elif(choice == 4):
            (choice2, slot) = self.selectObjectToEquip()
            if(choice2 > -1):
                self.player.equipItem(self.player.inventory.objects[choice2], slot)
        
        # Take off an object
        elif(choice == 5):
            choice2 = self.selectObjectToDequip()
            if(choice2 != None):
                self.player.dequipItem(choice2)
        
        # Show player's bars
        elif(choice == 6):
            print(self.player.showBars())
        
        # Show player's info
        elif(choice == 7):
            print(self.player.showInfo())
        
        # Show player's inventory
        elif(choice == 8):
            print(self.player.showInventory())
        
        # Show player's statistics
        elif(choice == 9):
            print(self.player.showStatistics())
        
        # Show player's success
        elif(choice == 10):
            print(self.player.showSuccess())
        
        return (False, 0)


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