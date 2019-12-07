from Inventory import Inventory
from Consumable import *
from Weapon import *
from Player import Player
from Jewels import *
from Armor import *
from Monster import *

def main():
    #name = input("Enter your player's name : ")
    player = Player(name="Nico", dodge=25, parry=25)
    print(player.showInfo())

    player.getDamages(10)
    print(player.showBars())

main()