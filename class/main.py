from Map import Map
from Player import Player

""" Entry point of the game """
def main():
    name = input("Enter your player's name : ")
    player = Player(name=name)
    map = Map(player)
    if(not map.run()):
        print("Game Over !")

main()