import sqlite3

def createDB():
    bdd = sqlite3.connect('DBMineRPG.db')
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
    bdd = sqlite3.connect('DBMineRPG.db')
    cursor = bdd.cursor()
    cursor.execute("""INSERT INTO player(name, health, shield, dodge, parry, criticalHit, mana, damageMin, damageMax, armor, xp, level, maxHealth, maxShield, maxMana) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",(name, health, shield, dodge, parry, criticalHit, mana, damageMin, damageMax, armor, xp, level, maxHealth, maxShield, maxMana))
    bdd.commit()
    bdd.close()


def insertInventoryData(id_player, gold, leftHand, rightHand, jewel1, jewel2, head, chest, arms, legs, feet):
    bdd = sqlite3.connect('DBMineRPG.db')
    cursor = bdd.cursor()
    cursor.execute("""INSERT INTO inventory(id_player, gold, leftHand, rightHand, jewel1, jewel2, head, chest, arms, legs, feet) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",(id_player, gold, leftHand, rightHand, jewel1, jewel2, head, chest, arms, legs, feet))
    bdd.commit()
    bdd.close()


def insertObjectData(id_player, name):
    bdd = sqlite3.connect('DBMineRPG.db')
    cursor = bdd.cursor()
    cursor.execute("""INSERT INTO objects(id_player, name) VALUES(?, ?)""",(id_player, name))
    bdd.commit()
    bdd.close()

def insertStatisticsData(id_player, monstersKilled, merchantsMet, chestsFound, objectsBought, objectsSold, consumablesUsed, enderDragonsKilled):
    bdd = sqlite3.connect('DBMineRPG.db')
    cursor = bdd.cursor()
    cursor.execute("""INSERT INTO statistics(id_player, monstersKilled, merchantsMet, chestsFound, objectsBought, objectsSold, consumablesUsed, enderDragonsKilled) VALUES(?, ?, ?, ?, ?, ?, ?, ?)""",(id_player, monstersKilled, merchantsMet, chestsFound, objectsBought, objectsSold, consumablesUsed, enderDragonsKilled))
    bdd.commit()
    bdd.close()



def getPlayerData(name):
    bdd = sqlite3.connect('DBMineRPG.db')
    cursor = bdd.cursor()
    """
    data = tuple()
    for row in cursor.execute('SELECT * FROM player'):
        if(row[1] == name):
            data = row
    """
    data = []
    for row in cursor.execute('SELECT * FROM player'):
        data.append(row)
    bdd.commit()
    bdd.close()
    return data


def getId(name):
    bdd = sqlite3.connect('DBMineRPG.db')
    cursor = bdd.cursor()
    data = tuple()
    for row in cursor.execute('SELECT * FROM player'):
        if(row[0] == name):
            data = row
    bdd.commit()
    bdd.close()
    return data


def getInventoryData(id_player):
    bdd = sqlite3.connect('DBMineRPG.db')
    cursor = bdd.cursor()
    """
    data = tuple()
    for row in cursor.execute('SELECT * FROM inventory'):
        if(row[0] == id_player):
            data = row
    """
    data = []
    for row in cursor.execute('SELECT * FROM inventory'):
        data.append(row)
    bdd.commit()
    bdd.close()
    return data


def getObjectData(id_player):
    bdd = sqlite3.connect('DBMineRPG.db')
    cursor = bdd.cursor()
    """
    data = tuple()
    for row in cursor.execute('SELECT * FROM objects'):
        if(row[0] == id_player):
            data = row
    """
    data = []
    for row in cursor.execute('SELECT * FROM objects'):
        data.append(row)
    bdd.commit()
    bdd.close()
    return data

def getStatisticsData(id_player):
    bdd = sqlite3.connect('DBMineRPG.db')
    cursor = bdd.cursor()
    """
    data = []
    for row in cursor.execute('SELECT * FROM statistics'):
        if(row[0] == id_player):
            data.append(row)
    """
    data = []
    for row in cursor.execute('SELECT * FROM statistics'):
        data.append(row)
    bdd.commit()
    bdd.close()
    return data