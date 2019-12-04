from Equipement import Equipement

class Armor(Equipement):
    def __init__(self, name, value, armor):
        Equipement.__init__(self, name, value)
        self.armor = armor