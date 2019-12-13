from Interaction import Interaction
from Merchant import Merchant
from Player import Player

class Transaction(Interaction):
    """ Transaction class instantiate a transaction object where the player buy or objects with a merchant. """
    def __init__(self, player, merchant):
        Interaction.__init__(self, player, merchant)

    def run(self):
        """ This method starts the transaction with the merchant. """

        print("You meet a {}.".format(self.mob.name.lower()))
        print("You have {} gold.".format(self.player.inventory.gold))
        while(True):
            if(self.selectAction() in [True, "exit"]):
                break
        
        print("\nYou leave the transaction.")
        self.player.statistics.merchantsMet += 1
        return True

    def selectAction(self):
        """ This method allows the player to choose an action during a transaction. """

        print("\nSelect your action")
        print("0  - Leave transaction")
        print("1  - Buy an object")
        print("2  - Sell an object")
        print("3  - Use a consumable")
        print("4  - Equip with an object")
        print("5  - Take off an object")
        print("6  - Show bars (health, shield, mana)")
        print("7  - Show infos")
        print("8  - Show inventory")
        print("9  - Show statistics")
        print("10 - Show success")
        print("11 - Save and exit")

        choice = str()
        while(choice not in [str(i) for i in range(12)]):
            choice = input("Your action: ")

        print("--------------------------------------------------")
        choice = int(choice)

        # Leave transaction
        if(choice == 0):
            return True # Leave the loop in the method run

        # Buy an object
        elif(choice == 1):
            choice2 = self.selectObjectToBuy()
            if(choice2 > -1):
                self.player.buyItem(self.mob.inventory.objects[choice2])

        # Sell an object
        elif(choice == 2):
            choice2 = self.selectObjectTosell()
            if(choice2 > -1):
                self.player.sellItem(self.player.inventory.objects[choice2])
            
        # Use a consumable
        elif(choice == 3):
            choice2 = self.selectConsumable()
            if(choice2 > -1):
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

        # Save and exit
        elif(choice == 11):
            self.player.save()
            return "exit" # Leave the loop in the method run
        
        return False

    def selectObjectToBuy(self):
        """ This method allows the player to choose wich objects on sale from Merchant inventory he could buy. """

        print("\nSelect the object to buy: ")
        print("-1 -  Previous")
        objectIndex = ['-1']
        for i,objects in enumerate(self.mob.inventory.objects):
            print(i, " - ", objects.showInfo())
            objectIndex.append(str(i))

        choice = str()
        while(choice not in objectIndex):
            choice = input("Object to buy: ")
        print("--------------------------------------------------")
        return int(choice)

    def selectObjectTosell(self):
        """ This method allows the player to choose wich objects he could sell from his inventory. """

        print("\nSelect the object to sell: ")
        print("-1 -  Previous")
        objectIndex = ['-1']
        for i,objects in enumerate(self.player.inventory.objects):
            print(i, " - ", objects.showInfo())
            objectIndex.append(str(i))

        choice = str()
        while(choice not in objectIndex):
            choice = input("Object to sell: ")
        print("--------------------------------------------------")
        return int(choice)