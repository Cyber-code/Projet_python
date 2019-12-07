from Inventory import Inventory
from Consumable import Consumable
from Weapon import Weapon
from Player import Player
from Jewels import Jewels
from Armor import Armor
from Monster import *

def main():
    #name = input("Enter your player's name : ")
    player = Player(name="Nico")

    print(player.showBars())

    monster = generateBlaze()
    print(monster.showInfo())

    monster2 = generateBowmanSkeleton()
    print(monster2.showInfo())
    
    monster23 = generateEnderDragon()
    print(monster23.showInfo())

    monster24 = generateEnderman()
    print(monster24.showInfo())

    monster5 = generateGhast()
    print(monster5.showInfo())

    monster6 = generateSpider()
    print(monster6.showInfo())

    monster7 = generateSwordmanSkeleton()
    print(monster7.showInfo())

    monster8 = generateZombie()
    print(monster8.showInfo())

    monster9 = generateZombiePigman()
    print(monster9.showInfo())

main()