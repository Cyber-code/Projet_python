from Character import Character
from Inventory import Inventory
from Consumable import generateConsumable
from Jewels import generateJewel
from Weapon import generateWeapon
from Armor import generateArmor
from random import randint

class Merchant(Character):
    """ Merchant class instantiate a merchant object that the player can interact with him in order to buy or sell objects. """
    def __init__(self, name="Merchant", health=20, shield=0, dodge=0,
                 parry=0, criticalHit=1, mana=10, damageMin=1,
                 damageMax=2, armor=0, xp=0, inventory=Inventory(),
                 maxHealth=20):
        Character.__init__(self, name, health, shield, dodge, parry, criticalHit, mana, damageMin, damageMax, armor, xp, inventory)

    def showInfo(self):
        """ Return a string which are precised parameters of the jewel object. """
        return "\nMerchant: "+ Character.showInfo(self) + "\nMaximum health: "+str(self.maxHealth)+ "\n"


def generateMerchant(name=""):
    """ Return a Merchant object. """
    if(name == "consumable_merchant"):
        merchant = Merchant(name="Consumable Merchant")
        merchant.addItem(generateConsumable(name="potion_mana"))
        merchant.addItem(generateConsumable(name="potion_healing"))
        merchant.addItem(generateConsumable(name="potion_regeneration"))
        merchant.addItem(generateConsumable(name="piece_shield"))
        merchant.addItem(generateConsumable(name="book_knowledge"))

    elif(name == "jewels_merchant"):
        merchant = Merchant(name="Jewels Merchant")
        merchant.addItem(generateJewel(name="strenght_necklace"))
        merchant.addItem(generateJewel(name="resistance_necklace"))
        merchant.addItem(generateJewel(name="anticipation_necklace"))
        merchant.addItem(generateJewel(name="health_necklace"))

    elif(name == "weapon_merchant"):
        merchant = Merchant(name="Weapon Merchant")
        merchant.addItem(generateWeapon(name="wooden_sword"))
        merchant.addItem(generateWeapon(name="goldden_sword"))
        merchant.addItem(generateWeapon(name="stone_sword"))
        merchant.addItem(generateWeapon(name="iron_sword"))
        merchant.addItem(generateWeapon(name="diamond_sword"))
        merchant.addItem(generateWeapon(name="bow"))
        merchant.addItem(generateWeapon(name="crossbow"))

    elif(name == "armor_merchant"):
        merchant = Merchant(name="Armor Merchant")
        merchant.addItem(generateArmor(name="leather_helmet"))
        merchant.addItem(generateArmor(name="leather_chestplate"))
        merchant.addItem(generateArmor(name="leather_arms_protection"))
        merchant.addItem(generateArmor(name="leather_leggings"))
        merchant.addItem(generateArmor(name="leather_boots"))

        merchant.addItem(generateArmor(name="golden_helmet"))
        merchant.addItem(generateArmor(name="golden_chestplate"))
        merchant.addItem(generateArmor(name="golden_arms_protection"))
        merchant.addItem(generateArmor(name="golden_leggings"))
        merchant.addItem(generateArmor(name="golden_boots"))

        merchant.addItem(generateArmor(name="chainmail_helmet"))
        merchant.addItem(generateArmor(name="chainmail_chestplate"))
        merchant.addItem(generateArmor(name="chainmail_arms_protection"))
        merchant.addItem(generateArmor(name="chainmail_leggings"))
        merchant.addItem(generateArmor(name="chainmail_boots"))

        merchant.addItem(generateArmor(name="iron_helmet"))
        merchant.addItem(generateArmor(name="iron_chestplate"))
        merchant.addItem(generateArmor(name="iron_arms_protection"))
        merchant.addItem(generateArmor(name="iron_leggings"))
        merchant.addItem(generateArmor(name="iron_boots"))

        merchant.addItem(generateArmor(name="diamond_helmet"))
        merchant.addItem(generateArmor(name="diamond_chestplate"))
        merchant.addItem(generateArmor(name="diamond_arms_protection"))
        merchant.addItem(generateArmor(name="diamond_leggings"))
        merchant.addItem(generateArmor(name="diamond_boots"))
    else:
        items = ["consumable_merchant","jewels_merchant","weapon_merchant","armor_merchant"]
        return generateMerchant(name=items[randint(0,len(items)-1)])
    return merchant