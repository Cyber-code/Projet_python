from Equipement import Equipement
from random import randint

class Jewels(Equipement):
    """ Jewels class instantiate jewel object which is used to increase dodge, parry, criticalHit or maxHealth of the character. """
    def __init__(self, name="Pasta necklace", value=0, dodge=0, parry=0, criticalHit=0, maxHealth=0):
        Equipement.__init__(self, name, value, typeObject="jewel")
        self.dodge = dodge
        self.parry = parry
        self.criticalHit = criticalHit
        self.maxHealth = maxHealth


    def showInfo(self):
        """ Return a string which are precised parameters of the jewel object. """
        return Equipement.showInfo(self) + "Dodge: +" + str(self.dodge)+" %, " + "Parry: +" + str(self.parry)+" %, " + "Critical hit: +" + str(self.criticalHit)+" %, "+ "Maximum Health: +" + str(self.maxHealth)+" %)"

def generateJewel(name=""):
    """ Return a Jewels object. """
    if(name == "strenght_necklace"):
        return Jewels(name="Strength necklace", value=50, criticalHit=10)
    elif(name == "resistance_necklace"):
        return Jewels(name="Resistance necklace", value=50, parry=10)
    elif(name == "anticipation_necklace"):
        return Jewels(name="Anticipation necklace", value=50, dodge=10)
    elif(name == "health_necklace"):
        return Jewels(name="Health necklace", value=50, maxHealth=10)
    else:
        items = ["strenght_necklace","resistance_necklace","anticipation_necklace","health_necklace"]
        return generateJewel(name=items[randint(0,len(items)-1)])