from Equipement import Equipement

""" Weapon class instantiate weapon object which is used to increase damage stat of the player"""
class Weapon(Equipement):
    def __init__(self, name="Wooden stick", value=0, damage=1):
        Equipement.__init__(self, name, value)
        self.damage = damage
        
        self.type = "weapon"


    def showInfo(self):
        return "\nWeapon: " + Equipement.showInfo(self) + "\nDamage: +" + str(self.damage) + "\n"


def generateWoodenSword():
    return Weapon(name="Wooden Sword", value = 10, damage=4)

def generateGoldenSword():
    return Weapon(name="Golden Sword", value = 80, damage=4)

def generateStoneSword():
    return Weapon(name="Stone Sword", value = 20, damage=5)

def generateIronSword():
    return Weapon(name="Iron Sword", value = 50, damage=6)

def generateDiamondSword():
    return Weapon(name="Diamond Sword", value = 100, damage=7)

def generateBow():
    return Weapon(name="Bow", value = 200, damage=9)

def generateCrossbow():
    return Weapon(name="Crossbow", value = 300, damage=10)