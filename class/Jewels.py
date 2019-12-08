from Equipement import Equipement

""" Jewels class instantiate jewel object which is used to increase dodge, parry, criticalHit or maxHealth of the player"""
class Jewels(Equipement):
    def __init__(self, name="Pasta necklace", value=0, dodge=0, parry=0, criticalHit=0, maxHealth=0):
        Equipement.__init__(self, name, value)
        self.dodge = dodge
        self.parry = parry
        self.criticalHit = criticalHit
        self.maxHealth = maxHealth
        
        self.type = "jewel"


    def showInfo(self):
        return "\nJewel: " + Equipement.showInfo(self) + "\nDodge: +" + str(self.dodge)+" %" + "\nParry: +" + str(self.parry)+" %" + "\nCritical hit: +" + str(self.criticalHit)+" %"+ "\nMaximum Health: +" + str(self.maxHealth)+" %" + "\n"


def generateStrengthNecklace():
    return Jewels(name="Strength necklace", value=50, criticalHit=10)

def generateResistanceNecklace():
    return Jewels(name="Resistance necklace", value=50, parry=10)

def generateAnticipationNecklace():
    return Jewels(name="Anticipation necklace", value=50, dodge=10)

def generateHealthNecklace():
    return Jewels(name="Health necklace", value=50, maxHealth=10)
