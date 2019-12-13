from Map import Map
from Player import Player
from Consumable import generateConsumable
from Weapon import generateWeapon
from DBMineRPG import *

def main():
    createDB() # Create the Data Base
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

        leftHand="None" 
        rightHand="None"
        jewel1="None"
        jewel2="None"
        head="None"
        chest="None" 
        arms="None"
        legs="None"
        feet="None"

        if(player.inventory.weapon["leftHand"] != None):
            leftHand = player.inventory.weapon["leftHand"].libelle
        if(player.inventory.weapon["rightHand"] != None):
            rightHand = player.inventory.weapon["rightHand"].libelle
        if(player.inventory.jewels["jewel1"] != None):
            jewel1 = player.inventory.jewels["jewel1"].libelle
        if(player.inventory.jewels["jewel2"] != None):
            jewel2 = player.inventory.jewels["jewel2"].libelle
        if(player.inventory.armor["head"] != None):
            head = player.inventory.armor["head"].libelle
        if(player.inventory.armor["chest"] != None):
            chest = player.inventory.armor["chest"].libelle
        if(player.inventory.armor["arms"] != None):
            arms = player.inventory.armor["arms"].libelle
        if(player.inventory.armor["legs"] != None):
            legs = player.inventory.armor["legs"].libelle
        if(player.inventory.armor["feet"] != None):
            feet = player.inventory.armor["feet"].libelle

        insertPlayerData(player.name, player.health, player.shield, player.dodge, player.parry, player.criticalHit, player.mana, player.damageMin, player.damageMax, player.armor, player.xp, player.level, player.maxHealth, player.maxShield, player.maxMana)
        #insertInventoryData(getId(player.name), player.inventory.gold, leftHand, rightHand, jewel1, jewel2, head, chest, arms, legs, feet)
        #insertStatisticsData(getId(player.name), player.statistics.monstersKilled, player.statistics.merchantsMet, player.statistics.chestsFound, player.statistics.objectsBought, player.statistics.objectsSold, player.statistics.consumablesUsed, player.statistics.enderDragonsKilled)
        #for obj in player.inventory.objects:
        #    insertObjectData(getId(player.name), obj.libelle)

        print(getPlayerData(player.name))
        #print(getInventoryData(getId(player.name)))
        #print(getStatisticsData(getId(player.name)))
        #print(getObjectData(getId(player.name)))
        
main()