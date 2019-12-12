class Interaction:
    """ Interaction class is the super class of Battle and Transaction classes. """
    def __init__(self, player, mob):
        self.player = player
        self.mob = mob


    def selectConsumable(self):
        """ 
        This method allows the player to choose a consumable in his inventory. 
        Return the consumable index of the inventory or -1 if the player want to come back.
        """

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


    def selectObjectToDequip(self):
        """ 
        This method allows the player to choose to take off wich equipement must return to his inventory. 
        Return the equipement index of the inventory or -1 if the player want to come back.
        """
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


    def selectObjectToEquip(self):
        """ 
        This method allows the player to choose to equip with an equipement from his inventory. 
        Return the equipement index of the inventory or -1 if the player want to come back.
        """
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