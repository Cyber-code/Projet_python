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