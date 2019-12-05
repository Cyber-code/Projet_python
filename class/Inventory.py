class Inventory:
    def __init__(self, objects=[], gold=0, leftHand=None, rigthHand=None, jewel1=None, jewel2=None, headArmor=None, chestArmor=None, armsArmor=None, legsArmor=None, footArmor=None):
        self.objects = objects  # objects is a list of weapons, jewels, armors and consumables
        self.gold = gold
        self.weapon = {"leftHand": leftHand, "rigthHand": rigthHand}     # 2 Slots for weapons in each hand
        self.jewels = {"jewel1": jewel1, "jewel2": jewel2}       # 2 Slots for jewels
        self.armor = {"head": headArmor, "chest": chestArmor, "arms": armsArmor, "legs": legsArmor, "foot": footArmor}       # 5 Slots for armor => head, chest, pants, arms, legs
        

    def showInfo(self):
        return "\nInventory" + "\nGold: "+str(self.gold)+" coins" + "\nObjects: "+str(self.objects) +"\nWeapon: "+str(self.weapon) + "\nJewels: "+str(self.jewels)+" %" + "\nArmor: "+str(self.armor)+ "\n"
