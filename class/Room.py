from Monster import Monster
from Merchant import Merchant
from Battle import Battle
from Transaction import Transaction
from Armor import generateArmor
from Consumable import generateConsumable
from Jewels import generateJewel
from Weapon import generateWeapon

""" Room class instantiate a room object where the player find a monster or a merchant """
class Room:
    def __init__(self, player, mob):
        self.player = player
        self.mob = mob

    def run(self):
        if(type(self.mob) == Monster):
            battle = Battle(self.player, self.mob)
            return battle.run()
        elif(type(self.mob) == Merchant):
            transaction = Transaction(self.player, self.mob)
            return transaction.run()
        else:
            print("You find a chest !")
            items = [generateConsumable(name="potion_healing"), generateWeapon("wooden_sword")]
            for objects in items:
                print("{} got {}.".format(self.player.name, objects.showInfo()))
                self.player.inventory.objects.append(objects)
            return True