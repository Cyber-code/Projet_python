from Monster import Monster
from Merchant import Merchant
from Battle import Battle
from Transaction import Transaction
from Armor import generateArmor
from Consumable import generateConsumable
from Jewels import generateJewel
from Weapon import generateWeapon
from random import expovariate, randint

class Room:
    def __init__(self, player, mob):
        self.player = player
        self.mob = mob

    def run(self):
        """
        Return True id the player is alive, False otherwise.
        The player enters in a room and either he engages a battle if the mob is a monster or he does a transaction if the mob is a merchant or
        he takes items in a chest if he finds one.
        """
        if(type(self.mob) == Monster):
            battle = Battle(self.player, self.mob)
            return battle.run()
        elif(type(self.mob) == Merchant):
            transaction = Transaction(self.player, self.mob)
            return transaction.run()
        else:
            print("You find a chest !")
            items = generateChest()
            for objects in items:
                print("{} got {}.".format(self.player.name, objects.showInfo()))
                self.player.inventory.objects.append(objects)
            return True


def generateChest():
    """
    Return a chest with n items.
    n is generate with an exponential law. By default, lamb=0.5 i.e the average item number generated by expovariate is 2.
    Add 1 to have one item at least, thus the n average is 3.
    """
    n = int(expovariate(0.5)) + 1
    random = 0
    chest = []
    for i in range(n):
        random = randint(0,99)
        # 25 % of chance to append an armor
        if(random < 25):
            chest.append(generateArmor())
        # 25 % of chance to append a consumable
        elif(random < 50):
            chest.append(generateConsumable())
        # 25 % of chance to append a jewel
        elif(random < 75):
            chest.append(generateJewel())
        # 25 % of chance to append a weapon
        else:
            chest.append(generateWeapon())
    return chest
