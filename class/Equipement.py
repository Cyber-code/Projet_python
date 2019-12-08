from Object import Object

""" Equipement class is the super class of Weapon, Armor and Jewels classes"""
class Equipement(Object):
    def __init__(self, name, value):
        Object.__init__(self, name, value)

    def showInfo(self):
        return Object.showInfo(self)