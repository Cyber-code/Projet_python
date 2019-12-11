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
        print("You have {} gold.".format(self.player.inventory.gold))
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
        print("6 - Use a consumable")
        print("7 - Leave transaction")

        choice = str()
        while(choice not in ["1","2","3","4","5","6","7"]):
            choice = input("Your action: ")

        print("--------------------------------------------------")
        choice = int(choice)

        # Buy an object
        if(choice == 1):
            choice2 = self.selectObjectToBuy()
            if(choice2 > -1):
                self.player.buyItem(self.merchant.inventory.objects[choice2])
            return False
        # Sell an object
        elif(choice == 2):
            choice2 = self.selectObjectTosell()
            if(choice2 > -1):
                self.player.sellItem(self.player.inventory.objects[choice2])
            return False
        # Show the Inventory
        elif(choice == 3):
            print(self.player.showInventory())
            return False
        # Equip with an object
        elif(choice == 4):
            (choice2, slot) = self.selectObjectToEquip()
            if(choice2 > -1):
                self.player.equipItem(self.player.inventory.objects[choice2], slot)
            return False
        # Take off an object
        elif(choice == 5):
            choice2 = self.selectObjectToDequip()
            if(choice2 != None):
                self.player.dequipItem(choice2)
            return False
        # Use a consumable
        elif(choice == 6):
            choice2 = self.selectConsumable()
            if(choice2 > -1):
                self.player.use(choice2)
            return False
        # Leave transaction
        else:
            return True # Leave the loop in the method run

    def selectObjectToBuy(self):
        print("\nSelect the object to buy: ")
        print("-1 -  Previous")
        objectIndex = ['-1']
        for i,objects in enumerate(self.merchant.inventory.objects):
            print(i, " - ", objects.showInfo())
            objectIndex.append(str(i))

        choice = str()
        while(choice not in objectIndex):
            choice = input("Object to buy: ")
        print("--------------------------------------------------")
        return int(choice)

    def selectObjectTosell(self):
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