from Equipement import Equipement
from random import randint, expovariate

""" Weapon class instantiate weapon object which is used to increase damage stat of the player"""
class Weapon(Equipement):
    def __init__(self, name="Wooden stick", value=0, damage=1, libelle="woodens_tick"):
        Equipement.__init__(self, name, value, typeObject="weapon", libelle=libelle)
        self.damage = damage

    def showInfo(self):
        """ This method return a string containing weapon's parameters. """
        return Equipement.showInfo(self) + "Damage: +" + str(self.damage) + ")"

def generateWeapon(name=""):
    """ Return a Weapon object. """
    if(name == "wooden_sword"):
        return Weapon(name="Wooden Sword", value = 10, damage=4, libelle="wooden_sword")
    elif(name == "goldden_sword"):
        return Weapon(name="Golden Sword", value = 1000, damage=4, libelle="goldden_sword")
    elif(name == "stone_sword"):
        return Weapon(name="Stone Sword", value = 500, damage=5, libelle="stone_sword")
    elif(name == "iron_sword"):
        return Weapon(name="Iron Sword", value = 2000, damage=6, libelle="iron_sword")
    elif(name == "diamond_sword"):
        return Weapon(name="Diamond Sword", value = 5000, damage=7, libelle="diamond_sword")
    elif(name == "bow"):
        return Weapon(name="Bow", value = 7500, damage=9, libelle="bow")
    elif(name == "crossbow"):
        return Weapon(name="Crossbow", value = 10000, damage=10, libelle="crossbow")
    else:
        items = ["wooden_sword","goldden_sword","stone_sword","iron_sword","diamond_sword","bow","crossbow"]
        return generateWeapon(name=items[int(expovariate(1/(len(items)//4))) % len(items)])