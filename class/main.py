from Inventory import Inventory, generateInventory
from Consumable import Consumable, generateConsumable
from Weapon import Weapon, generateWeapon
from Player import Player
from Jewels import Jewels, generateJewel
from Armor import Armor, generateArmor
from Monster import Monster, generateMonster
from Spell import Spell, generateSpell
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
    monster.inventory = generateInventory()
    battle = Battle(player, monster)

    battle.run()


main()
