from Room import Room
from Merchant import generateMerchant
from Monster import generateMonster
from random import randint, expovariate

class Map:
    """ Map class instantiate a map object where rooms are generated. """
    def __init__(self, player):
        self.player = player

    def generateRoom(self):
        """ This method generates a room where there are a number of chance that the player could meet a Monster, a Merchant or finding a chest. """
        rnd = randint(0,99)
        # 70 % of chance to enter in a battle
        if(rnd < 70):
            # The generation of monster follow an exponential law i.e monsters who have their name are in the left of the list below have more chance to be generated.
            name = ["zombie","bowman_skeleton","swordman_skeleton","spider","enderman","zombie_pigman","ghast","blaze","ender_dragon"]
            mob = generateMonster(name=name[int(expovariate(1/(len(name)//4))) % len(name)])
        # 20 % of chance to meet a merchant
        elif(rnd < 90):
            name = ["consumable_merchant","jewels_merchant","weapon_merchant","armor_merchant"]
            mob = generateMerchant(name=name[randint(0,len(name)-1)])
        # 10 % of chance to find a chest
        else:
            mob = None
        return Room(self.player, mob)

    def run(self):
        """ This method generates rooms while the player is alive. """
        while(True):
            room = self.generateRoom()
            print(self.player.maxHealth)
            self.player.updateSuccess()
            if(room.run() in [False, "exit"]):
                self.player.updateSuccess()
                break