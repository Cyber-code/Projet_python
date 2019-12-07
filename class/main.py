from Inventory import Inventory
from Consumable import *
from Weapon import *
from Player import Player
from Jewels import Jewels
from Armor import *
from Monster import *

def main():
    #name = input("Enter your player's name : ")
    player = Player(name="Nico")
    print(player.showInfo())

    helmet = generateLeatherHelmet()
    print(helmet.showInfo())

    chestplate = generateDiamondChestplate()
    print(chestplate.showInfo())

    armsProtection = generateChainmailArmsProtection()
    print(armsProtection.showInfo())

    leggings = generateIronLeggings()
    print(leggings.showInfo())

    boots = generateGoldenBoots()
    print(boots.showInfo())


main()