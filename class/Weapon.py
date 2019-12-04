from Equipement import Equipement

class Weapon(Equipement):
    def __init__(self, name="Wooden stick", value=0, damage=2):
        Equipement.__init__(self, name, value)
        self.damage = damage

    def showInfo(self):
        return "\nWeapon: " + Equipement.showInfo(self) + "\nDamage: " + str(self.damage) + "\n"