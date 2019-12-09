from Merchant import Merchant
from Player import Player

""" Transaction class instantiate a transaction object where the player buy or objects with a merchant """
class Transaction:
    def __init__(self, player, merchant):
        self.player = player
        self.merchant = merchant

    def run(self):
        print("You meet a {}.".format(self.merchant.name.upper()))
        while(True):
            pass

        return True

    """ This method allows the player to choose an action during a transaction """
    def selectAction(self):
        print("\nSelect your action")
        print("1 - Buy an item")
        print("2 - Throw a spell")
        print("3 - Use a consumable")
        print("4 - Show bars (health, shield, mana)")
        print("5 - Do nothing")