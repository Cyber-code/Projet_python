from Inventory import Inventory
from Consumable import Consumable
from Weapon import Weapon
from Player import Player
from Jewels import Jewels
from Armor import Armor
from Monster import Monster

def main():
    """
    print("-------------------------Test Character----------------------------")
    ch = Character(name = "Nico", health=100, shield=50, dodge=1, parry=1, criticalHit=1, mana=10, damageMin=1, damageMax=10, armor=0, level=1, xp=0, inventory=Inventory([], 0, None, None, None, None, None, None, None, None, None))
    print(ch.showInfo())

    print("-------------------------Test Inventory----------------------------")
    inventory = Inventory(objects=[], gold=0, leftHand=None, rigthHand=None, jewel1=None, jewel2=None, headArmor=None, chestArmor=None, pantsArmor=None, armsArmor=None, legsArmor=None)
    print(inventory.showInfo())

    print("-------------------------Test Object----------------------------")
    obj = Object(name="Potion de vie", value=100)
    print(obj.showInfo())

    inventory.objects.append(obj)
    print(inventory.showInfo())
    """

    print("-------------------------Test Player----------------------------")
    player = Player(name="Nico")
    print(player.showInfo())

    print("-------------------------Test Consumable----------------------------")
    bottle = Consumable()
    print(bottle.showInfo())

    print("-------------------------Test Weapon----------------------------")
    woodenSword = Weapon(name="Wooden Sword", value=10, damage=4)
    print(woodenSword.showInfo())

    print("-------------------------Test Jewel----------------------------")
    jewels = Jewels()
    print(jewels.showInfo())

    print("-------------------------Test Armor----------------------------")
    armor = Armor(name="Diamond Helmet", value=1000, armor=50, armorType="head")
    print(armor.showInfo())

    print(player.showInventory())

    player.addItem(bottle)

    player.addItem(armor)

    player.addItem(jewels)

    player.addItem(woodenSword)

    print(player.showInventory())

    print("-------------------------Test Monster----------------------------")
    monster = Monster()
    print(monster.showInfo())

    player.setLeftWeapon(woodenSword)

    print(player.showInventory())

    print(player.showBars())

main()