from Object import Object

class Equipement(Object):
    """ Equipement class is the super class of Weapon, Armor and Jewels classes. """
    def __init__(self, name, value, typeObject):
        Object.__init__(self, name, value, typeObject)

    def showInfo(self):
        return Object.showInfo(self)