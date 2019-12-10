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
    print("---------------------------------- TEST ---------------------------------------------")
    inventory = Inventory()
    for elt in inventory.objects:
        print(elt.name)
    player = Player(name="Nico")
    print(player.showInventory())
    #player.setWeapon(generateWeapon())
    #player.setArmor(generateArmor())
    #player.setJewel(generateJewel())
    #player.addItem(generateConsumable())
    merchant = generateMerchant("consumable_merchant")
    print(merchant.showInventory())
    print(player.showInventory())
    for elt in inventory.objects:
        print(elt.name)
    """
    transaction = Transaction(player=player, merchant=merchant)
    transaction.run()
    print(player.showInventory())
    """

main()
