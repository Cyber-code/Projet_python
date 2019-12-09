from Equipement import Equipement

""" Armor class instantiate armor object (headArmor, chestArmor, armsArmor, legsArmor, footArmor) which is used to increase armor stat of the player"""
class Armor(Equipement):
    def __init__(self, name="Colander", value=10, armor=1, armorType="head"):
        if (armorType.lower() not in ["head", "chest", "arms", "legs", "feet"]):
            raise ValueError("The armor type is not conform, please choose armorType equals at head, chest, arms, legs or feet.")

        Equipement.__init__(self, name, value, typeObject=armorType)
        self.armor = armor    # Percentage of reducing damages


    def showInfo(self):
        return "\nArmor: " + Equipement.showInfo(self) + "\nArmor protection: +" + str(self.armor)+" %" + "\n"


def generateLeatherHelmet():
    return Armor(name="Leather Helmet", value=10, armor=2, armorType="head")

def generateLeatherChestplate():
    return Armor(name="Leather Chestplate", value=10, armor=10, armorType="chest")

def generateLeatherArmsProtection():
    return Armor(name="Leather Arms Protection", value=10, armor=4, armorType="arms")

def generateLeatherLeggings():
    return Armor(name="Leather Leggings", value=10, armor=6, armorType="legs")

def generateLeatherBoots():
    return Armor(name="Leather Boots", value=10, armor=2, armorType="feet")


def generateGoldenHelmet():
    return Armor(name="Golden Helmet", value=20, armor=6, armorType="head")

def generateGoldenChestplate():
    return Armor(name="Golden Chestplate", value=20, armor=18, armorType="chest")

def generateGoldenArmsProtection():
    return Armor(name="Golden Arms Protection", value=20, armor=8, armorType="arms")

def generateGoldenLeggings():
    return Armor(name="Golden Leggings", value=20, armor=10, armorType="legs")

def generateGoldenBoots():
    return Armor(name="Golden Boots", value=20, armor=2, armorType="feet")


def generateChainmailHelmet():
    return Armor(name="Chainmail Helmet", value=50, armor=6, armorType="head")

def generateChainmailChestplate():
    return Armor(name="Chainmail Chestplate", value=50, armor=18, armorType="chest")

def generateChainmailArmsProtection():
    return Armor(name="Chainmail Arms Protection", value=50, armor=10, armorType="arms")

def generateChainmailLeggings():
    return Armor(name="Chainmail Leggings", value=50, armor=14, armorType="legs")

def generateChainmailBoots():
    return Armor(name="Chainmail Boots", value=50, armor=2, armorType="feet")


def generateIronHelmet():
    return Armor(name="Iron Helmet", value=100, armor=6, armorType="head")

def generateIronChestplate():
    return Armor(name="Iron Chestplate", value=100, armor=22, armorType="chest")

def generateIronArmsProtection():
    return Armor(name="Iron Arms Protection", value=100, armor=12, armorType="arms")

def generateIronLeggings():
    return Armor(name="Iron Leggings", value=100, armor=18, armorType="legs")

def generateIronBoots():
    return Armor(name="Iron Boots", value=100, armor=6, armorType="feet")


def generateDiamondHelmet():
    return Armor(name="Diamond Helmet", value=200, armor=10, armorType="head")

def generateDiamondChestplate():
    return Armor(name="Diamond Chestplate", value=200, armor=30, armorType="chest")

def generateDiamondArmsProtection():
    return Armor(name="Diamond Arms Protection", value=200, armor=16, armorType="arms")

def generateDiamondLeggings():
    return Armor(name="Diamond Leggings", value=200, armor=22, armorType="legs")

def generateDiamondBoots():
    return Armor(name="Diamond Boots", value=200, armor=10, armorType="feet")