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

    weapon = generateBow()
    weapon2 = generateCrossbow()
    print(player.showInventory())
    print(player.setWeapon(weapon, hand="leftHand"))
    print(player.showInventory())
    print(player.setWeapon(weapon2, hand="rightHand"))
    print(player.showInventory())


main()