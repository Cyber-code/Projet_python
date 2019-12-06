from Monster import Monster
from Player import Player

""" Battle class instantiate a battle object where the player figth a monster """
class Battle:
    def __init__(self, player, monster):
        self.player = player
        self.monster = monster

    """ This method launch the battle """
    def run(self):
        while(self.monster.isAlive):
            pass
            #Under construction
        items = self.monster.dropItems()