from Inventory import Inventory, generateInventory
from Consumable import Consumable, generateConsumable
from Weapon import Weapon, generateWeapon
from Player import Player
from Jewels import Jewels, generateJewel
from Armor import Armor, generateArmor
from Monster import Monster, generateMonster
from Spell import Spell, generateSpell
from Battle import Battle
from Merchant import Merchant, generateMerchant

def main():
    #name = input("Enter your player's name : ")
    
    player = Player(name="Nico")
    player.addGold(100)
    print(player.showInventory())
    weapon = generateWeapon()
    weapon2= generateWeapon(name="diamond_sword")
    print(weapon.showInfo())
    player.buyItem(weapon)
    print(player.showInventory())
    player.buyItem(weapon2)
    print(player.showInventory())
    


main()
