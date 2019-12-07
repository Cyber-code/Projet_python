from Inventory import Inventory
from Consumable import *
from Weapon import *
from Player import Player
from Jewels import Jewels
from Armor import Armor
from Monster import *

def main():
    #name = input("Enter your player's name : ")
    player = Player(name="Nico")
    print(player.showInfo())

    conso =  generatePotionHealing()
    print(conso.showInfo())
    conso2 = generatePotionMana()
    print(conso2.showInfo())
    conso3 = generatePotionRegeneration()
    print(conso3.showInfo())
    conso4 = generatShieldPiece()
    print(conso4.showInfo())
    conso5 = generateKnowledgeBook()
    print(conso5.showInfo())


main()