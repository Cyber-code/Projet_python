import sqlite3
import os
database_url = os.path.join(os.getcwd(),'DBMineRPG.db')

def checkPlayer(name):
    bdd = sqlite3.connect(database_url)
    cursor = bdd.cursor()
    isInDB = False
    for row in cursor.execute('SELECT * FROM player'):
        if(row[1] == name):
            isInDB = True
    bdd.commit()
    bdd.close()
    return isInDB

def clearDB():
    bdd = sqlite3.connect(database_url)
    cursor = bdd.cursor()
    cursor.execute('DELETE FROM player')
    cursor.execute('DELETE FROM inventory')
    cursor.execute('DELETE FROM objects')
    cursor.execute('DELETE FROM statistics')
    bdd.commit()
    bdd.close()

def createDB():
    bdd = sqlite3.connect(database_url)
    cursor = bdd.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS player(
        id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
        name TEXT,
        health INTEGER,
        shield INTEGER,
        dodge INTEGER,
        parry INTEGER,
        criticalHit INTEGER,
        mana INTEGER,
        damageMin INTEGER,
        damageMax INTEGER,
        armor INTEGER,
        xp INTEGER,
        level INTEGER,
        maxHealth INTEGER,
        maxShield INTEGER,
        maxMana INTEGER
    )
    """)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS inventory(
        id_player INTEGER,
        gold INTEGER,
        leftHand TEXT,
        rightHand TEXT,
        jewel1 TEXT,
        jewel2 TEXT,
        head TEXT,
        chest TEXT,
        arms TEXT,
        legs TEXT,
        feet TEXT
    )
    """)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS objects(
        id_player INTEGER,
        name TEXT
    )
    """)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS statistics(
        id_player INTEGER,
        monstersKilled INTEGER,
        merchantsMet INTEGER,
        chestsFound INTEGER,
        objectsBought INTEGER,
        objectsSold INTEGER,
        consumablesUsed INTEGER,
        enderDragonsKilled INTEGER
    )
    """)
    bdd.commit()
    bdd.close()


def insertPlayerData(name, health, shield, dodge, parry, criticalHit, mana, damageMin, damageMax, armor, xp, level, maxHealth, maxShield, maxMana):
    bdd = sqlite3.connect(database_url)
    cursor = bdd.cursor()
    cursor.execute("""INSERT INTO player(name, health, shield, dodge, parry, criticalHit, mana, damageMin, damageMax, armor, xp, level, maxHealth, maxShield, maxMana) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",(name, health, shield, dodge, parry, criticalHit, mana, damageMin, damageMax, armor, xp, level, maxHealth, maxShield, maxMana))
    bdd.commit()
    bdd.close()


def insertInventoryData(id_player, gold, leftHand, rightHand, jewel1, jewel2, head, chest, arms, legs, feet):
    bdd = sqlite3.connect(database_url)
    cursor = bdd.cursor()
    cursor.execute("""INSERT INTO inventory(id_player, gold, leftHand, rightHand, jewel1, jewel2, head, chest, arms, legs, feet) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",(id_player, gold, leftHand, rightHand, jewel1, jewel2, head, chest, arms, legs, feet))
    bdd.commit()
    bdd.close()


def insertObjectData(id_player, name):
    bdd = sqlite3.connect(database_url)
    cursor = bdd.cursor()
    cursor.execute("""INSERT INTO objects(id_player, name) VALUES(?, ?)""", (id_player, name))
    bdd.commit()
    bdd.close()

def insertStatisticsData(id_player, monstersKilled, merchantsMet, chestsFound, objectsBought, objectsSold, consumablesUsed, enderDragonsKilled):
    bdd = sqlite3.connect(database_url)
    cursor = bdd.cursor()
    cursor.execute("""INSERT INTO statistics(id_player, monstersKilled, merchantsMet, chestsFound, objectsBought, objectsSold, consumablesUsed, enderDragonsKilled) VALUES(?, ?, ?, ?, ?, ?, ?, ?)""",(id_player, monstersKilled, merchantsMet, chestsFound, objectsBought, objectsSold, consumablesUsed, enderDragonsKilled))
    bdd.commit()
    bdd.close()



def getPlayerData(name):
    bdd = sqlite3.connect(database_url)
    cursor = bdd.cursor()
    data = tuple()
    for row in cursor.execute('SELECT * FROM player'):
        if(row[1] == name):
            data = row
    bdd.commit()
    bdd.close()
    return data


def getId(name):
    bdd = sqlite3.connect(database_url)
    cursor = bdd.cursor()
    data = tuple()
    for row in cursor.execute('SELECT * FROM player'):
        if(row[1] == name):
            data = row[0]
    bdd.commit()
    bdd.close()
    return data


def getInventoryData(id_player):
    bdd = sqlite3.connect(database_url)
    cursor = bdd.cursor()
    data = tuple()
    for row in cursor.execute('SELECT * FROM inventory'):
        if(row[0] == id_player):
            data = row
    bdd.commit()
    bdd.close()
    return data


def getObjectData(id_player):
    bdd = sqlite3.connect(database_url)
    cursor = bdd.cursor()
    data = [tuple]
    for row in cursor.execute('SELECT * FROM objects'):
        if(row[0] == id_player):
            data.append(row)
    bdd.commit()
    bdd.close()
    return []

def getStatisticsData(id_player):
    bdd = sqlite3.connect(database_url)
    cursor = bdd.cursor()
    data = tuple()
    for row in cursor.execute('SELECT * FROM statistics'):
        if(row[0] == id_player):
            data = row
    bdd.commit()
    bdd.close()
    return data


def updatePlayerData(name, health, shield, dodge, parry, criticalHit, mana, damageMin, damageMax, armor, xp, level, maxHealth, maxShield, maxMana):
    bdd = sqlite3.connect(database_url)
    cursor = bdd.cursor()
    cursor.execute("""UPDATE player SET health=?, shield=?, dodge=?, parry=?, criticalHit=?, mana=?, damageMin=?, damageMax=?, armor=?, xp=?, level=?, maxHealth=?, maxShield=?, maxMana=? WHERE name=?""",(health, shield, dodge, parry, criticalHit, mana, damageMin, damageMax, armor, xp, level, maxHealth, maxShield, maxMana, name))
    bdd.commit()
    bdd.close()


def updateInventoryData(id_player, gold, leftHand, rightHand, jewel1, jewel2, head, chest, arms, legs, feet):
    bdd = sqlite3.connect(database_url)
    cursor = bdd.cursor()
    cursor.execute("""UPDATE inventory SET gold=?,leftHand=?,rightHand=?,jewel1=?,jewel2=?,head=?,chest=?,arms=?,legs=?,feet=? WHERE id_player=?""",(gold, leftHand, rightHand, jewel1, jewel2, head, chest, arms, legs, feet, id_player))
    bdd.commit()
    bdd.close()


def updateObjectData(id_player, name):
    bdd = sqlite3.connect(database_url)
    cursor = bdd.cursor()
    cursor.execute("""UPDATE objects SET name=? WHERE id_player=?""",(name, id_player))
    bdd.commit()
    bdd.close()

def updateStatisticsData(id_player, monstersKilled, merchantsMet, chestsFound, objectsBought, objectsSold, consumablesUsed, enderDragonsKilled):
    bdd = sqlite3.connect(database_url)
    cursor = bdd.cursor()
    cursor.execute("""UPDATE statistics SET monstersKilled=?,merchantsMet=?,chestsFound=?,objectsBought=?,objectsSold=?,consumablesUsed=?,enderDragonsKilled=? WHERE id_player=?""",(monstersKilled, merchantsMet, chestsFound, objectsBought, objectsSold, consumablesUsed, enderDragonsKilled, id_player))
    bdd.commit()
    bdd.close()

#clearDB()