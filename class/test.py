import sqlite3

def check(name):
    bdd = sqlite3.connect('DBMineRPG.db')
    cursor = bdd.cursor()
    isInDB = False
    for row in cursor.execute('SELECT * FROM player'):
        print(row)
        if(row[1] == name):
            isInDB = True 

    for row in cursor.execute('SELECT * FROM inventory'):
        print(row)

    for row in cursor.execute('SELECT * FROM objects'):
        print(row)

    for row in cursor.execute('SELECT * FROM statistics'):
        print(row)

    bdd.commit()
    bdd.close()
    print(isInDB)
def insertPlayerData(name, health, shield, dodge, parry, criticalHit, mana, damageMin, damageMax, armor, xp, level, maxHealth, maxShield, maxMana):
    bdd = sqlite3.connect('DBMineRPG.db')
    cursor = bdd.cursor()
    cursor.execute("""INSERT INTO player(name, health, shield, dodge, parry, criticalHit, mana, damageMin, damageMax, armor, xp, level, maxHealth, maxShield, maxMana) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",(name, health, shield, dodge, parry, criticalHit, mana, damageMin, damageMax, armor, xp, level, maxHealth, maxShield, maxMana))
    bdd.commit()
    bdd.close()

def insertObjectData(id_player, name):
    bdd = sqlite3.connect("DBMineRPG.db")
    cursor = bdd.cursor()
    cursor.execute("""INSERT INTO objects(id_player, name) VALUES(?, ?)""", (id_player, name))
    bdd.commit()
    bdd.close()

def deleteObjectData(id_player):
    bdd = sqlite3.connect("DBMineRPG.db")
    cursor = bdd.cursor()
    cursor.execute("""DELETE FROM objects WHERE id_player=?""", (id_player,))
    bdd.commit()
    bdd.close()

#insertPlayerData("clem",0,0,0,0,0,0,0,0,0,0,0,0,0,0)
#insertPlayerData("rodo",0,0,0,0,0,0,0,0,0,0,0,0,0,0)

#insertObjectData(1, "wooden_sword")
deleteObjectData(1)
check("rodo")