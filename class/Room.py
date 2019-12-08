from Monster import Monster
from Merchant import Merchant

""" Room class instantiate a room object where the player find a monster or a merchant """
class Room:
    def __init__(self, mob):
        if (mob == 0):
            self.mob = Merchant()
        else:
            self.mob = Monster()