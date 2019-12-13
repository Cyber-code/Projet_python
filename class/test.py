import sqlite3

def check(name):
    bdd = sqlite3.connect('DBMineRPG.db')
    cursor = bdd.cursor()
    isInDB = False
    for row in cursor.execute('SELECT * FROM player'):
        print(row)
        if(row[1] == name):
            isInDB = True 
    bdd.commit()
    bdd.close()
    print(isInDB)
def insertPlayerData(name, health, shield, dodge, parry, criticalHit, mana, damageMin, damageMax, armor, xp, level, maxHealth, maxShield, maxMana):
    bdd = sqlite3.connect('DBMineRPG.db')
    cursor = bdd.cursor()
    cursor.execute("""INSERT INTO player(name, health, shield, dodge, parry, criticalHit, mana, damageMin, damageMax, armor, xp, level, maxHealth, maxShield, maxMana) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",(name, health, shield, dodge, parry, criticalHit, mana, damageMin, damageMax, armor, xp, level, maxHealth, maxShield, maxMana))
    bdd.commit()
    bdd.close()

insertPlayerData("clem",0,0,0,0,0,0,0,0,0,0,0,0,0,0)

insertPlayerData("rodo",0,0,0,0,0,0,0,0,0,0,0,0,0,0)
check("rodo")