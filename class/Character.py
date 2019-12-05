from Inventory import Inventory

class Character:
    def __init__(self, name, health, shield, dodge,
                 parry, criticalHit, mana, damageMin,
                 damageMax, armor, level, xp, inventory):
        self.name = name
        self.health = health
        self.shield = shield    
        self.dodge = dodge              # Chance of dodge (%) to avoid attacks (damages are nullfied)
        self.parry = parry              # Change of parry (%) to reduce amount of damage by 70%
        self.criticalHit = criticalHit  # Chance of critical hit (%) to double the amount of damage inflicted
        self.mana = mana                # Magic point, to use spells
        self.damageMin = damageMin      # Mininum damage that the character is able to inflict
        self.damageMax = damageMax      # Maximum damage "                                   "
        self.armor = armor              # Armor point, reduced incoming damage by a percentage
        self.level = level              # Level, each leave increase a small of the characteristics above
        self.xp = xp                    # Experience bar, when filled, increase cureent level by one
        self.maxLevel = 21

        self.inventory = inventory

        self.isAlive = True


    def showInfo(self):
        return "\nName: "+ self.name + "\nHealth: "+str(self.health)+" PV"  +"\nShield: "+str(self.shield) + "\nDodge: "+str(self.dodge)+" %" + "\nParry: "+str(self.parry)+" %"  + "\nCritical Hit: "+str(self.criticalHit)+" %" + "\nMana: "+str(self.mana)+" MP" + "\nMinimum Damage: "+str(self.damageMin) + "\nMaximum Damage: "+str(self.damageMax) + "\nArmor: "+str(self.armor)+" AP" + "\nLevel: "+str(self.level)+" lvl" + "\nExperience: "+str(self.xp)+" xp" + "\nLevel Max: "+str(self.maxLevel) + "\nInventory: "+str(self.inventory) + "\n"