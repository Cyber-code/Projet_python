from Map import Map
from Player import Player
from Consumable import generateConsumable
from Weapon import generateWeapon
from Armor import generateArmor
from Jewels import generateJewel
from DBMineRPG import *

def loadDB(player):
    print("Greating for coming back on Mine RPG !")
    playerData = getPlayerData(player.name)
    id_player = playerData[0]
    player.name = playerData[1]
    player.health = playerData[2]
    player.shield = playerData[3]
    player.dodge = playerData[4]
    player.parry = playerData[5]
    player.criticalHit = playerData[6]
    player.mana = playerData[7]
    player.damageMin = playerData[8]
    player.damageMax = playerData[9]
    player.armor = playerData[10]
    player.xp = playerData[11]
    player.level = playerData[12]
    player.maxHealth = playerData[13]
    player.maxShield = playerData[14]
    player.maxMana = playerData[15]

    inventoryData = getInventoryData(id_player)
    player.inventory.gold = inventoryData[1]
    player.inventory.weapon["leftHand"] = generateWeapon(name=inventoryData[2]) if inventoryData[2] != "None" else None
    player.inventory.weapon["rightHand"] = generateWeapon(name=inventoryData[3]) if inventoryData[3] != "None" else None
    player.inventory.jewels["jewel1"] = generateJewel(name=inventoryData[4]) if inventoryData[4] != "None" else None
    player.inventory.jewels["jewel2"] = generateJewel(name=inventoryData[5]) if inventoryData[5] != "None" else None
    player.inventory.armor["head"] = generateArmor(name=inventoryData[6]) if inventoryData[6] != "None" else None
    player.inventory.armor["chest"] = generateArmor(name=inventoryData[7]) if inventoryData[7] != "None" else None
    player.inventory.armor["arms"] = generateArmor(name=inventoryData[8]) if inventoryData[8] != "None" else None
    player.inventory.armor["legs"] = generateArmor(name=inventoryData[9]) if inventoryData[9] != "None" else None
    player.inventory.armor["feet"] = generateArmor(name=inventoryData[10]) if inventoryData[10] != "None" else None
    
    objectsData = getObjectData(id_player)
    for obj in objectsData:
        if(obj[1] in ["potion_healing","potion_mana","piece_shield","potion_regeneration","book_knowledge"]):
            player.inventory.objects.append(generateConsumable(obj[1]))
        elif(obj[1] in ["leather_helmet","leather_chestplate","leather_arms_protection","leather_leggings","leather_boots","golden_helmet","golden_chestplate","golden_arms_protection","golden_leggings","golden_boots","chainmail_helmet","chainmail_chestplate","chainmail_arms_protection","chainmail_leggings","chainmail_boots","iron_helmet","iron_chestplate","iron_arms_protection","iron_leggings","iron_boots","diamond_helmet","diamond_chestplate","diamond_arms_protection","diamond_leggings","diamond_boots"]):
            player.inventory.objects.append(generateArmor(obj[1]))
        elif(obj[1] in ["strenght_necklace","resistance_necklace","anticipation_necklace","health_necklace"]):
            player.inventory.objects.append(generateJewel(obj[1]))
        elif(obj[1] in ["wooden_sword","goldden_sword","stone_sword","iron_sword","diamond_sword","bow","crossbow"]):
            player.inventory.objects.append(generateWeapon(obj[1]))

    statsData = getStatisticsData(id_player)
    player.statistics.monstersKilled = statsData[1]
    player.statistics.merchantsMet = statsData[2]
    player.statistics.chestsFound = statsData[3]
    player.statistics.objectsBought = statsData[4]
    player.statistics.objectsSold = statsData[5]
    player.statistics.consumablesUsed = statsData[6]
    player.statistics.enderDragonsKilled = statsData[7]

    return player


def insertPlayerToDB(player):
    print("Welcome on Mine RPG !")
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
        insertObjectData(getId(player.name), "potion_healing")
        insertObjectData(getId(player.name), "potion_mana")
    if(difficulty < 3):
        player.addItem(generateWeapon(name="wooden_sword"))
        insertObjectData(getId(player.name), "wooden_sword")
    if(difficulty < 2):
        player.addGold(10)

    return player

def main():
    createDB() # Create the Data Base
    name = input("Enter your player's name : ")
    player = Player(name=name)

    # The player is already in the DB
    if(checkPlayer(name)):
        player = loadDB(player)
    # The player is still not in the DB
    else:
        player = insertPlayerToDB(player)

    # Launching of the game
    map = Map(player)
    if(not map.run()):
        #print(player.showStatistics())
        #print(player.showSuccess())
        player.save()
        
main()