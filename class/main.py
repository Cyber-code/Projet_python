from Character import Character
from Inventory import Inventory
from Object import Object
from Consumable import Consumable

def main():

    print("-------------------------Test Character----------------------------")
    perso = Character(name = "Nico", health=100, shield=50, dodge=1, parry=1, criticalHit=1, mana=10, damageMin=1, damageMax=10, armor=0, level=1, xp=0, inventory=Inventory([], 0, None, None, None, None, None, None, None, None, None))
    print(perso.showInfo())

    print("-------------------------Test Inventory----------------------------")
    inventory = Inventory(objects=[], gold=0, leftHand=None, rigthHand=None, jewel1=None, jewel2=None, headArmor=None, chestArmor=None, pantsArmor=None, armsArmor=None, legsArmor=None)
    print(inventory.showInfo())

    print("-------------------------Test Object----------------------------")
    obj = Object(name="Potion de vie", value=100)
    print(obj.showInfo())

    inventory.objects.append(obj)
    print(inventory.showInfo())

    print("-------------------------Test Consumable----------------------------")
    con = Consumable(name="Potion de mana", value=100)
    print(Object.showInfo(con))

main()