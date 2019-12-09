from Equipement import Equipement

""" Armor class instantiate armor object (headArmor, chestArmor, armsArmor, legsArmor, footArmor) which is used to increase armor stat of the player"""
class Armor(Equipement):
    def __init__(self, name="Colander", value=10, armor=1, armorType="head"):
        if (armorType.lower() not in ["head", "chest", "arms", "legs", "feet"]):
            raise ValueError("The armor type is not conform, please choose armorType equals at head, chest, arms, legs or feet.")

        Equipement.__init__(self, name, value, typeObject=armorType)
        self.armor = armor    # Percentage of reducing damages


    def showInfo(self):
        return Equipement.showInfo(self) + "Armor protection: +" + str(self.armor)+" %)"

def generateArmor(name="leather_helmet"):
    if(name == "leather_helmet"):
        return Armor(name="Leather Helmet", value=10, armor=2, armorType="head")
    elif(name == "leather_chestplate"):
        return Armor(name="Leather Chestplate", value=10, armor=10, armorType="chest")
    elif(name == "leather_arms_protection"):
        return Armor(name="Leather Arms Protection", value=10, armor=4, armorType="arms")
    elif(name == "leather_leggings"):
        return Armor(name="Leather Leggings", value=10, armor=6, armorType="legs")
    elif(name == "leather_boots"):
        return Armor(name="Leather Boots", value=10, armor=2, armorType="feet")

    elif(name == "golden_helmet"):
        return Armor(name="Golden Helmet", value=20, armor=6, armorType="head")
    elif(name == "golden_chestplate"):
        return Armor(name="Golden Chestplate", value=20, armor=18, armorType="chest")
    elif(name == "golden_arms_protection"):
        return Armor(name="Golden Arms Protection", value=20, armor=8, armorType="arms")
    elif(name == "golden_leggings"):
        return Armor(name="Golden Leggings", value=20, armor=10, armorType="legs")
    elif(name == "golden_boots"):
        return Armor(name="Golden Boots", value=20, armor=2, armorType="feet")

    elif(name == "chainmail_helmet"):
        return Armor(name="Chainmail Helmet", value=50, armor=6, armorType="head")
    elif(name == "chainmail_chestplate"):
        return Armor(name="Chainmail Chestplate", value=50, armor=18, armorType="chest")
    elif(name == "chainmail_arms_protection"):
        return Armor(name="Chainmail Arms Protection", value=50, armor=10, armorType="arms")
    elif(name == "chainmail_leggings"):
        return Armor(name="Chainmail Leggings", value=50, armor=14, armorType="legs")
    elif(name == "chainmail_boots"):
        return Armor(name="Chainmail Boots", value=50, armor=2, armorType="feet")

    elif(name == "iron_helmet"):
        return Armor(name="Iron Helmet", value=100, armor=6, armorType="head")
    elif(name == "iron_chestplate"):
        return Armor(name="Iron Chestplate", value=100, armor=22, armorType="chest")
    elif(name == "iron_arms_protection"):
        return Armor(name="Iron Arms Protection", value=100, armor=12, armorType="arms")
    elif(name == "iron_leggings"):
        return Armor(name="Iron Leggings", value=100, armor=18, armorType="legs")
    elif(name == "iron_boots"):
        return Armor(name="Iron Boots", value=100, armor=6, armorType="feet")
    
    elif(name == "diamond_helmet"):
        return Armor(name="Diamond Helmet", value=200, armor=10, armorType="head")
    elif(name == "diamond_chestplate"):
        return Armor(name="Diamond Chestplate", value=200, armor=30, armorType="chest")
    elif(name == "diamond_arms_protection"):
        return Armor(name="Diamond Arms Protection", value=200, armor=16, armorType="arms")
    elif(name == "diamond_leggings"):
        return Armor(name="Diamond Leggings", value=200, armor=22, armorType="legs")
    elif(name == "diamond_boots"):
        return Armor(name="Diamond Boots", value=200, armor=10, armorType="feet")

    else:
        return Armor(name="Leather Helmet", value=10, armor=2, armorType="head")