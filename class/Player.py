from Character import Character
from Inventory import Inventory

""" Player class instantiate a player object controled by the user """
class Player(Character):
    def __init__(self, name="Player", health=20, shield=10, dodge=0,
                 parry=0, criticalHit=1, mana=10, damageMin=1,
                 damageMax=2, armor=0, xp=0, inventory=Inventory()):
        Character.__init__(self, name, health, shield, dodge, parry, criticalHit, mana, damageMin, damageMax, armor, xp, inventory)

    """ When the player uses a consumable which regerate his health """
    def addHealth(self, health):
        if(self.health + health >= self.maxHealth):
            self.health = self.maxHealth
        else:
            self.health += health

    """ This method is used to add an item/object to the player's inventory """
    def addItem(self, item):
        self.inventory.objects.append(item)

    """ When the player uses a consumable which regerate his mana (magic points) """
    def addMana(self, mana):
        if(self.mana + mana >= self.maxMana):
            self.mana = self.maxMana
        else:
            self.mana += mana

    """ When the player uses a consumable which regerate his shield """
    def addShield(self, shield):
        if(self.shield + shield >= self.maxShield):
            self.shield = self.maxShield
        else:
            self.shield += shield

    """ When the player earned enought xp, he gained a level """
    def levelUp(self):
        if self.level < self.maxLevel:
            self.level += 1
        
        croissance = 1.2

        # These stats are increase about 20% (arbitrary)
        self.maxHealth = int(croissance*self.maxHealth)
        self.health = int(croissance*self.health)
        self.maxShield = int(croissance*self.maxShield)
        self.shield = int(croissance*self.shield)
        self.maxMana = int(croissance*self.maxMana)
        self.mana = int(croissance*self.mana)
        self.damageMin = int(croissance*self.damageMin)
        self.damageMax = int(croissance*self.damageMax)

        # These stats are inscrease (arbitrary) whithout exceed 20 (of the stat)
        if(self.dodge < 20/croissance):
            self.dodge = int(croissance*self.dodge)

        if(self.parry < 20/croissance):
            self.parry = int(croissance*self.parry)
        
        if(self.criticalHit < 20/croissance):
            self.criticalHit = int(croissance*self.criticalHit)
        
        if(self.armor < 20/croissance):
            self.armor = int(croissance*self.armor)