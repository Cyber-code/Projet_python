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

    spell = generateFireball()
    print(spell.showInfo())

main()