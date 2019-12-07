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

    print(player.showInfo())

main()