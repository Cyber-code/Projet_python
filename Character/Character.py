class Character():
    """ Constructor """
    def __init__(self, name, health, shield, dodge,
                 parry, criticalHit, mana, damageMin,
                 damageMax, armor, level, xp):
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
        self.max_level = 21


    """ Methods """

    """ When the character earned enought xp, he gained a level """
    def levelUp(self):
        if self.level < self.max_level:
            self.level += 1

        # These stats are doubled (arbitrary)
        self.health *= 1.2
        self.shield *= 1.2
        self.mana *= 1.2
        self.damageMin *= 1.2
        self.damageMax *= 1.2

        # These stats are doubled (arbitrary) whithout exceed 20 % (of the stat)
        if(self.dodge < 20/1*2):
            self.dodge *= 1.2

        if(self.parry < 20/1*2):
            self.parry *= 1.2
        
        if(self.criticalHit < 20/1*2):
            self.criticalHit *= 1.2
        
        if(self.armor < 20/1*2):
            self.armor *= 1.2

    """ 
    This method is called when the character killed
    monsters and he earn some xp
    """
    def addXp(self, xp):
        self.xp += xp

        # This dict corresponds for each level its xp to reach it
        lvl_xp = {1:0, 2:50, 3:100, 4:250, 5:500,
                6:750, 7:1000, 8:2500, 9:5000,
                10:7500, 11:10000, 12:25000, 13:50000,
                14:75000, 15:100000, 16:250000, 17:500000,
                18:750000, 19:1000000, 20:2500000}

        # We verify for each lvl above current level if we have enougth xp to levelup
        xp_temp = self.xp
        while xp_temp - lvl_xp[self.level + 1] > 0:
            if (self.xp >= lvl_xp[self.level + 1]):
                self.levelUp()
                xp_temp -= lvl_xp[self.level + 1]