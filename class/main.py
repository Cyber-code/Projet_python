from Inventory import Inventory
from Consumable import *
from Weapon import *
from Player import Player
from Jewels import *
from Armor import *
from Monster import *

def main():
    #name = input("Enter your player's name : ")
    player = Player(name="Nico")
    print(player.showInfo())

    jewel1 = generateStrengthNecklace()
    print(jewel1.showInfo())
    jewel2 = generateResistanceNecklace()
    print(jewel2.showInfo())
    jewel3 = generateAnticipationNecklace()
    print(jewel3.showInfo())
    jewel4 = generateHealthNecklace()
    print(jewel4.showInfo())


main()