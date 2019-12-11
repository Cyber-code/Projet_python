from Room import Room
from Merchant import generateMerchant
from Monster import generateMonster
from random import randint

""" Map class instantiate a map object where there are rooms """
class Map:
    def __init__(self, player):
        self.player = player

    def generateRoom(self):
        rnd = randint(0,2)
        if(rnd < 7):
            name = ["zombie","bowman_skeleton","swordman_skeleton","spider","enderman","zombie_pigman","ghast","blaze","ender_dragon"]
            mob = generateMonster(name=name[randint(0,len(name)-1)])
        elif(rnd < 9):
            name = ["consumable_merchant","jewels_merchant","weapon_merchant","armor_merchant"]
            mob = generateMerchant(name=name[randint(0,len(name)-1)])
        else:
            mob = None
        return Room(self.player, mob)

    def run(self):
        while(True):
            room = self.generateRoom()
            if(not room.run()):
                break