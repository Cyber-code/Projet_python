from Map import Map
from Player import Player
from Consumable import generateConsumable
from Weapon import generateWeapon

def main():
    name = input("Enter your player's name : ")
    player = Player(name=name)

    # The player choose the difficulty
    print("\nSelect the difficulty:")
    print("1 - Easy")
    print("2 - Medium")
    print("3 - Hard")
    print("4 - Hardcore")
    difficulty = str()
    while(difficulty not in ["1","2","3","4"]):
        difficulty = input("Difficulty: ")
    print("--------------------------------------------------")
    difficulty = int(difficulty)

    if(difficulty < 4):
        player.addItem(generateConsumable(name="potion_healing"))
        player.addItem(generateConsumable(name="potion_mana"))
    if(difficulty < 3):
        player.addItem(generateWeapon(name="wooden_sword"))
    if(difficulty < 2):
        player.addGold(10)

    # Launching of the game
    map = Map(player)
    if(not map.run()):
        print("Game Over !")
        print(player.showStatistics())
        print(player.showSuccess())

main()