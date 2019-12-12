class Interaction:
    def __init__(self, player, mob):
        self.player = player
        self.mob = mob

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