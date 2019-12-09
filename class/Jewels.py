from Equipement import Equipement

""" Jewels class instantiate jewel object which is used to increase dodge, parry, criticalHit or maxHealth of the player"""
class Jewels(Equipement):
    def __init__(self, name="Pasta necklace", value=0, dodge=0, parry=0, criticalHit=0, maxHealth=0):
        Equipement.__init__(self, name, value, typeObject="jewel")
        self.dodge = dodge
        self.parry = parry
        self.criticalHit = criticalHit
        self.maxHealth = maxHealth


    def showInfo(self):
        return "\nJewel: " + Equipement.showInfo(self) + "\nDodge: +" + str(self.dodge)+" %" + "\nParry: +" + str(self.parry)+" %" + "\nCritical hit: +" + str(self.criticalHit)+" %"+ "\nMaximum Health: +" + str(self.maxHealth)+" %" + "\n"

def generateJewel(name="strenght_necklace"):
    if(name == "strenght_necklace"):
        return Jewels(name="Strength necklace", value=50, criticalHit=10)
    elif(name == "resistance_necklace"):
        return Jewels(name="Resistance necklace", value=50, parry=10)
    elif(name == "anticipation_necklace"):
        return Jewels(name="Anticipation necklace", value=50, dodge=10)
    elif(name == "health_necklace"):
        return Jewels(name="Health necklace", value=50, maxHealth=10)
    else:
        return Jewels(name="Strength necklace", value=50, criticalHit=10)

