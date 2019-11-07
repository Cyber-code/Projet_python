class Character():
    """ Constructor """
    def __init__(self, name, health, shield, dodge,
                 parry, criticalHit, mana, damageMin,
                 damageMax, armor, level, xp):
        self.name = name
        self.health = health
        self.shield = shield    
        self.dodge = dodge      # Chance of dodge (%) to avoid attacks (damages are nullfied)
        self.parry = parry      # Change of parry (%) to reduce amount of damage by 70%
        self.criticalHit = criticalHit  # Chance of critical hit (%) to double the amount of damage inflicted
        self.mana = mana        # Magic point, to use spells
        self.damageMin = damageMin      # Mininum damage that the character is able to inflict
        self.damageMax = damageMax      # Maximum damage "                                   "
        self.armor = armor      # Armor point, reduced incoming damage by a percentage
        self.level = level      # Level, each leave increase a small of the characteristics above
        self.xp = xp            # Experience bar, when filled, increase cureent level by one


    """ Methods """

    """ When the character earned enought xp, he gained a level """
    def levelUp(self):
        self.level += 1

        # These stats are doubled (arbitrary)
        self.health *= 2
        self.shield *= 2
        self.mana *= 2
        self.damageMin *= 2
        self.damageMax *= 2

        # These stats are doubled (arbitrary) whithout exceed 20 % (of the stat)
        if(self.dodge < 10):
            self.dodge *= 2

        if(self.parry < 10):
            self.parry *= 2
        
        if(self.criticalHit < 10):
            self.criticalHit *= 2
        
        if(self.armor < 10):
            self.armor *= 2