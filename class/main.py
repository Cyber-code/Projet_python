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
    player.setWeapon(generateWeapon(name="golden_sword"))
    player.addItem(generateConsumable(name="potion_mana"))
    player.addItem(generateConsumable(name="potion_mana"))
    player.addItem(generateConsumable(name="potion_mana"))
    player.addItem(generateWeapon())
    player.addItem(generateConsumable(name="potion_mana"))
    monster = generateMonster(name="zombie")
    battle = Battle(player, monster)

    battle.run()


main()
