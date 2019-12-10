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

def main():
    #name = input("Enter your player's name : ")
    player = Player(name="Nico")
    player.addGold(100)
    player.addItem(generateConsumable())
    merchant = generateMerchant("consumable_merchant")
    transaction = Transaction(player=player, merchant=merchant)
    transaction.run()

    print(player.showInfo())

main()