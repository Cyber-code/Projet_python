from Map import Map
from Player import Player
from Consumable import generateConsumable
from Weapon import generateWeapon
from Armor import generateArmor
from Jewels import generateJewel
from DBMineRPG import *

def main():
    createDB() # Create the Data Base
    name = input("Enter your player's name : ")
    player = Player(name=name)
    if(checkPlayer(name)):
        data = getPlayerData(name)
        id_player = data[0]
        player.name = data[1]
        player.health = data[2]
        player.shield = data[3]
        player.dodge = data[4]
        player.parry = data[5]
        player.criticalHit = data[6]
        player.mana = data[7]
        player.damageMin = data[8]
        player.damageMax = data[9]
        player.armor = data[10]
        player.xp = data[11]
        player.level = data[12]
        player.maxHealth = data[12]
        player.maxShield = data[14]
        player.maxMana = data[15]

        data2 = getInventoryData(id_player)
        player.inventory.gold = data2[1]
        player.inventory.weapon["leftHand"] = generateWeapon(name=data2[2]) if data2[2] != "None" else None
        player.inventory.weapon["rightHand"] = generateWeapon(name=data2[3]) if data2[3] != "None" else None
        player.inventory.jewels["jewel1"] = generateJewel(name=data2[4]) if data2[4] != "None" else None
        player.inventory.jewels["jewel2"] = generateJewel(name=data2[5]) if data2[5] != "None" else None
        player.inventory.armor["head"] = generateArmor(name=data2[6]) if data2[6] != "None" else None
        player.inventory.armor["chest"] = generateArmor(name=data2[7]) if data2[7] != "None" else None
        player.inventory.armor["arms"] = generateArmor(name=data2[8]) if data2[8] != "None" else None
        player.inventory.armor["legs"] = generateArmor(name=data2[9]) if data2[9] != "None" else None
        player.inventory.armor["feet"] = generateArmor(name=data2[10]) if data2[10] != "None" else None

        data3 = getObjectData(id_player)
        for obj in data3:
            player.inventory.objects.append(obj[1])

        data4 = getStatisticsData(id_player)
        player.statistics.monstersKilled = data4[1]
        player.statistics.merchantsMet = data4[2]
        player.statistics.chestsFound = data4[3]
        player.statistics.objectsBought = data4[4]
        player.statistics.objectsSold = data4[5]
        player.statistics.consumablesUsed = data4[6]
        player.statistics.enderDragonsKilled = data4[7]
    else:
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
        insertInventoryData(getId(player.name), player.inventory.gold, leftHand, rightHand, jewel1, jewel2, head, chest, arms, legs, feet)
        insertStatisticsData(getId(player.name), player.statistics.monstersKilled, player.statistics.merchantsMet, player.statistics.chestsFound, player.statistics.objectsBought, player.statistics.objectsSold, player.statistics.consumablesUsed, player.statistics.enderDragonsKilled)
        for obj in player.inventory.objects:
            insertObjectData(getId(player.name), obj.libelle)

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

        print(getPlayerData(player.name))
        print(getInventoryData(getId(player.name)))
        print(getStatisticsData(getId(player.name)))
        print(getObjectData(getId(player.name)))
        
main()