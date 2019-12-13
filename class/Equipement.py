from Object import Object

class Equipement(Object):
    """ Equipement class is the super class of Weapon, Armor and Jewels classes. """
    def __init__(self, name, value, typeObject, libelle):
        Object.__init__(self, name, value, typeObject, libelle)

    def showInfo(self):
        return Object.showInfo(self)