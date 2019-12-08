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
    print(player.showInventory())

    helmet = generateDiamondHelmet()
    chestPlate = generateDiamondChestplate()
    arms = generateDiamondArmsProtection()
    leggings = generateDiamondLeggings()
    boots = generateDiamondBoots()

    player.setArmor(helmet)
    player.setArmor(chestPlate)
    player.setArmor(arms)
    player.setArmor(leggings)
    player.setArmor(boots)

    print(player.showInfo())
    print(player.showInventory())

    player.getDamages(100)
    print(player.showBars())



main()