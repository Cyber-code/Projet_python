from Merchant import Merchant
from Player import Player

""" Transaction class instantiate a transaction object where the player buy or objects with a merchant """
class Transaction:
    def __init__(self, player, merchant):
        self.player = player
        self.merchant = merchant

    """ This method starts the transaction with the merchant """
    def run(self):
        print("You meet a {}.".format(self.merchant.name.lower()))
        while(True):
            if(self.selectAction()):
                break
        
        print("\nYou leave the transaction.")
        return True

    """ This method allows the player to choose an action during a transaction """
    def selectAction(self):
        print("\nSelect your action")
        print("1 - Buy an object")
        print("2 - Sell an object")
        print("3 - Show inventory")
        print("4 - Equip with an object")
        print("5 - Take off an object")
        print("6 - Leave transaction")

        choice = str()
        while(choice not in ["1","2","3","4","5","6"]):
            choice = input("Your action: ")

        print("--------------------------------------------------")
        choice = int(choice)

        # Buy an object
        if(choice == 1):
            return False
        # Sell an object
        elif(choice == 2):
            return False
        # Show the Inventory
        elif(choice == 3):
            print(self.player.showInventory())
            return False
        # Equip with an object
        elif(choice == 4):
            return False
        # Take off an object
        elif(choice == 5):
            return False
        # Leave transaction
        else:
            return True

    def selectObjectToBuy(self):
        pass

    def selectObjectTosell(self):
        pass

    def selectObjectToEquip(self):
        pass

    def selectObjectToDequip(self):
        pass