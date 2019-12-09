from Character import Character
from Inventory import Inventory
from Consumable import generateConsumable
from Jewels import generateJewel
from Weapon import generateWeapon
from Armor import generateArmor

""" Merchant class instantiate a merchant object that the player can interact with him in order to buy or sell objects """
class Merchant(Character):
    def __init__(self, name="Merchant", health=20, shield=0, dodge=0,
                 parry=0, criticalHit=1, mana=10, damageMin=1,
                 damageMax=2, armor=0, xp=0, inventory=Inventory(),
                 maxHealth=20):
        Character.__init__(self, name, health, shield, dodge, parry, criticalHit, mana, damageMin, damageMax, armor, xp, inventory)

    def showInfo(self):
        return "\nMerchant: "+ Character.showInfo(self) + "\nMaximum health: "+str(self.maxHealth)+ "\n"


def generateMerchant(name="consumable_merchant"):
    inventory = Inventory(gold=1000)
    if(name == "consumable_merchant"):
        inventory.objects.append(generateConsumable(name="potion_mana"))
        inventory.objects.append(generateConsumable(name="potion_healing"))
        inventory.objects.append(generateConsumable(name="potion_regeneration"))
        inventory.objects.append(generateConsumable(name="piece_shield"))
        inventory.objects.append(generateConsumable(name="book_knowledge"))
        return Merchant(name="Consumable Merchant", inventory=inventory)
    elif(name == "jewels_merchant"):
        inventory.objects.append(generateJewel(name="strenght_necklace"))
        inventory.objects.append(generateJewel(name="resistance_necklace"))
        inventory.objects.append(generateJewel(name="anticipation_necklace"))
        inventory.objects.append(generateJewel(name="health_necklace"))
        return Merchant(name="Jewels Merchant", inventory=inventory)
    elif(name == "weapon_merchant"):
        inventory.objects.append(generateWeapon(name="wooden_sword"))
        inventory.objects.append(generateWeapon(name="goldden_sword"))
        inventory.objects.append(generateWeapon(name="stone_sword"))
        inventory.objects.append(generateWeapon(name="iron_sword"))
        inventory.objects.append(generateWeapon(name="diamond_sword"))
        inventory.objects.append(generateWeapon(name="bow"))
        inventory.objects.append(generateWeapon(name="crossbow"))
        return Merchant(name="Weapon Merchant", inventory=inventory)
    else:
        inventory.objects.append(generateArmor(name="leather_helmet"))
        inventory.objects.append(generateArmor(name="leather_chestplate"))
        inventory.objects.append(generateArmor(name="leather_arms_protection"))
        inventory.objects.append(generateArmor(name="leather_leggings"))
        inventory.objects.append(generateArmor(name="leather_boots"))

        inventory.objects.append(generateArmor(name="golden_helmet"))
        inventory.objects.append(generateArmor(name="golden_chestplate"))
        inventory.objects.append(generateArmor(name="golden_arms_protection"))
        inventory.objects.append(generateArmor(name="golden_leggings"))
        inventory.objects.append(generateArmor(name="golden_boots"))

        inventory.objects.append(generateArmor(name="chainmail_helmet"))
        inventory.objects.append(generateArmor(name="chainmail_chestplate"))
        inventory.objects.append(generateArmor(name="chainmail_arms_protection"))
        inventory.objects.append(generateArmor(name="chainmail_leggings"))
        inventory.objects.append(generateArmor(name="chainmail_boots"))

        inventory.objects.append(generateArmor(name="iron_helmet"))
        inventory.objects.append(generateArmor(name="iron_chestplate"))
        inventory.objects.append(generateArmor(name="iron_arms_protection"))
        inventory.objects.append(generateArmor(name="iron_leggings"))
        inventory.objects.append(generateArmor(name="iron_boots"))

        inventory.objects.append(generateArmor(name="diamond_helmet"))
        inventory.objects.append(generateArmor(name="diamond_chestplate"))
        inventory.objects.append(generateArmor(name="diamond_arms_protection"))
        inventory.objects.append(generateArmor(name="diamond_leggings"))
        inventory.objects.append(generateArmor(name="diamond_boots"))
        return Merchant(name="Armor Merchant", inventory=inventory)