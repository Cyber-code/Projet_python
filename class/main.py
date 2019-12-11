from Inventory import Inventory, generateInventory
from Consumable import Consumable, generateConsumable
from Weapon import Weapon, generateWeapon
from Player import Player
from Jewels import Jewels, generateJewel
from Armor import Armor, generateArmor
from Monster import Monster, generateMonster
from Spell import Spell, generateSpell
from Battle import Battle
from Merchant import generateMerchant
from Transaction import Transaction
from Map import Map

def main():
    name = input("Enter your player's name : ")
    player = Player(name=name)
    map = Map(player)
    if(not map.run()):
        print("Game Over !")

main()