import Object

class Inventory:
    def __init__(self, objects, gold, leftHand, rigthHand, jewel1, jewel2, headArmor, chestArmor, pantsArmor, armsArmor, legsArmor):
        self.objects = objects  # objects is a list of weapons, jewels and armors
        self.gold = gold
        self.weapon = {"leftHand": leftHand, "rigthHand": rigthHand}     # 2 Slots for weapons in each hand
        self.jewels = {"jewel1": jewel1, "jewel2": jewel2}       # 2 Slots for jewels
        self.armor = {"head": headArmor, "chest": chestArmor, "pants": pantsArmor, "arms": armsArmor, "legs": legsArmor}       # 5 Slots for armor => head, chest, pants, arms, legs
        
    """ Method """

    def showInfo(self):
        return "\nInventory" + "\nGold: "+str(self.gold)+" coins" + "\nObjects: "+str(self.objects) +"\nWeapon: "+str(self.weapon) + "\nJewels: "+str(self.jewels)+" %" + "\nArmor: "+str(self.armor)+ "\n"
