from random import randint
from Armor import generateArmor
from Consumable import generateConsumable
from Jewels import generateJewel
from Weapon import generateWeapon

""" Inventory class instantiate a inventory object which is a character's caracteristic """
class Inventory:
    def __init__(self, objects=[], gold=0, leftHand=None, rigthHand=None, jewel1=None, jewel2=None, headArmor=None, chestArmor=None, armsArmor=None, legsArmor=None, feetArmor=None):
        self.objects = []  # objects is a list of weapons, jewels, armors and consumables
        self.gold = gold
        self.weapon = {"leftHand": leftHand, "rightHand": rigthHand}     # 2 Slots for weapons in each hand
        self.jewels = {"jewel1": jewel1, "jewel2": jewel2}       # 2 Slots for jewels
        self.armor = {"head": headArmor, "chest": chestArmor, "arms": armsArmor, "legs": legsArmor, "feet": feetArmor}       # 5 Slots for armor => head, chest, arms, legs, feet


    def showInfo(self):
        return "\nInventory" + "\nGold: "+str(self.gold)+" coins" + "\nObjects: "+str(self.objects) +"\nWeapon: "+str(self.weapon) + "\nJewels: "+str(self.jewels)+" %" + "\nArmor: "+str(self.armor)+ "\n"

# Under construction, it is used for tests
def generateInventory():
    objects = [generateArmor(), generateConsumable(), generateJewel(), generateWeapon()]
    return Inventory(objects=objects, gold=randint(0, 10))