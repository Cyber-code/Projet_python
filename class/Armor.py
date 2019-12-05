from Equipement import Equipement

""" Armor class instantiate armor object (headArmor, chestArmor, armsArmor, legsArmor, footArmor) which is used to increase armor stat of the player"""
class Armor(Equipement):
    def __init__(self, name="Colander", value=10, armor=1, armorType="head"):
        if (armorType.lower() not in ["head", "chest", "arms", "legs", "feet"]):
            raise ValueError("The armor type is not conform, please choose armorType equals at head, chest, arms, legs or feet.")

        Equipement.__init__(self, name, value)
        self.armor = armor
        self.armorType = armorType # This parameter is used to specify where the player have to wear this armor (head, chest, arms, legs, feet)


    def showInfo(self):
        return "\nArmor: " + Equipement.showInfo(self) + "\n{} armor protection: +".format(self.armorType.capitalize()) + str(self.armor)+" %" + "\n"