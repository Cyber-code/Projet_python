from Inventory import Inventory
from Consumable import *
from Weapon import *
from Player import Player
from Jewels import *
from Armor import *
from Monster import *
from Spell import *

def main():
    #name = input("Enter your player's name : ")
    player = Player(name="Nico")
    print(player.showInfo())

    jewel = generateResistanceNecklace()
    jewel2 = generateAnticipationNecklace()
    print(player.showInventory())
    print(player.setJewel(jewel, slot="jewel1"))
    print(player.showInventory())
    print(player.setJewel(jewel2, slot="jewel2"))
    print(player.showInventory())
    print(player.showInfo())
    print(player.showInventory())
    print(player.showInfo())


main()