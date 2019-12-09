from Object import Object

""" Equipement class is the super class of Weapon, Armor and Jewels classes"""
class Equipement(Object):
    def __init__(self, name, value, typeObject):
        Object.__init__(self, name, value, typeObject)

    def showInfo(self):
        return Object.showInfo(self)