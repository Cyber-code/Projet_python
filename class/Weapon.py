from Equipement import Equipement

""" Weapon class instantiate weapon object which is used to increase damage stat of the player"""
class Weapon(Equipement):
    def __init__(self, name="Wooden stick", value=0, damage=2):
        Equipement.__init__(self, name, value)
        self.damage = damage


    def showInfo(self):
        return "\nWeapon: " + Equipement.showInfo(self) + "\nDamage: +" + str(self.damage) + "\n"