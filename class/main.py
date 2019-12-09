from Inventory import Inventory
from Consumable import *
from Weapon import *
from Player import Player
from Jewels import *
from Armor import *
from Monster import *
from Spell import *
from Battle import Battle

def main():
    #name = input("Enter your player's name : ")
    player = Player(name="Nico")
    player.setWeapon(generateStoneSword())
    monster = generateZombie()
    battle = Battle(player, monster)

    battle.run()


main()