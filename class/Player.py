from Character import Character
from Inventory import Inventory

""" Player class instantiate a player object controled by the user """
class Player(Character):
    def __init__(self, name="Player", health=20, shield=0, dodge=0,
                 parry=0, criticalHit=1, mana=10, damageMin=1,
                 damageMax=1, armor=0, level=1, xp=0, inventory=Inventory()):
        Character.__init__(self, name, health, shield, dodge, parry, criticalHit, mana, damageMin, damageMax, armor, level, xp, inventory)

    def showInfo(self):
        return "\nPlayer: "+ Character.showInfo(self) + "\n"