from Equipement import Equipement

""" Armor class instantiate armor object (headArmor, chestArmor, armsArmor, legsArmor, footArmor) which is used to increase armor stat of the player"""
class Armor(Equipement):
    def __init__(self, name="Colander", value=10, armor=1):
        Equipement.__init__(self, name, value)
        self.armor = armor


    def showInfo(self):
        return "\nArmor: " + Equipement.showInfo(self) + "\nArmor protection: +" + str(self.armor)+" %" + "\n"