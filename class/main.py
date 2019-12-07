from Inventory import Inventory
from Consumable import Consumable
from Weapon import *
from Player import Player
from Jewels import Jewels
from Armor import Armor
from Monster import *

def main():
    #name = input("Enter your player's name : ")
    player = Player(name="Nico")

    print(player.showInfo())

    weapon = generateWoodenSword()
    print(weapon.showInfo())

    weapon1 = generateGoldenSword()
    print(weapon1.showInfo())

    weapon2 = generateStoneSword()
    print(weapon2.showInfo())

    weapon3 = generateIronSword()
    print(weapon3.showInfo())

    weapon4 = generateDiamondSword()
    print(weapon4.showInfo())

    weapon5 = generateBow()
    print(weapon5.showInfo())

    weapon6 = generateCrossbow()
    print(weapon6.showInfo())

main()