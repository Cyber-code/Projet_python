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
        while(self.monster.isAlive()):
            
            action = False
            while(action == False):
                (action, damages) = self.selectAction()
            
            self.monster.getDamages(damages)
            print(self.monster.showBars())

        print("\nWell done, you killed the {}.".format(self.monster.name))
        items = self.monster.dropItems()


    """ This method allows the player to choose an action during a battle """
    def selectAction(self):
        print("\nSelect your action")
        print("1 - Attack with weapon")
        print("2 - Throw a spell")
        print("3 - Use a consumable")
        print("4 - Show bars (health, shield, mana)")
        print("5 - Do nothing")

        choice = str()
        while(choice not in ["1","2","3","4","5"]):
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
        # Show player's bars
        elif(choice == 4):
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