from Inventory import Inventory
from Consumable import *
from Weapon import *
from Player import Player
from Jewels import *
from Armor import *
from Monster import *

def main():
    #name = input("Enter your player's name : ")
    player = Player(name="Nico")
    print(player.showInfo())

    player.getDamages(40)
    print(player.showBars())
    print("Alive:", player.isAlive())
    
    for i in range(32):
        player.getDamages(1)
        print(player.showBars())
        print("Alive:", player.isAlive())
    

main()