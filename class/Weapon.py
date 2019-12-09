from Equipement import Equipement

""" Weapon class instantiate weapon object which is used to increase damage stat of the player"""
class Weapon(Equipement):
    def __init__(self, name="Wooden stick", value=0, damage=1):
        Equipement.__init__(self, name, value, typeObject="weapon")
        self.damage = damage

    def showInfo(self):
        return Equipement.showInfo(self) + "Damage: +" + str(self.damage) + ")"

def generateWeapon(name="wooden_sword"):
    if(name == "wooden_sword"):
        return Weapon(name="Wooden Sword", value = 10, damage=4)
    elif(name == "goldden_sword"):
        return Weapon(name="Golden Sword", value = 80, damage=4)
    elif(name == "stone_sword"):
        return Weapon(name="Stone Sword", value = 20, damage=5)
    elif(name == "iron_sword"):
        return Weapon(name="Iron Sword", value = 50, damage=6)
    elif(name == "diamond_sword"):
        return Weapon(name="Diamond Sword", value = 100, damage=7)
    elif(name == "bow"):
        return Weapon(name="Bow", value = 200, damage=9)
    elif(name == "crossbow"):
        return Weapon(name="Crossbow", value = 300, damage=10)
    else:
        return Weapon(name="Wooden Sword", value = 10, damage=4)