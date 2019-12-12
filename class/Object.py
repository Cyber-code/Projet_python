class Object:
    """ Object class is the super class of Consumable and Equipement classes. """
    def __init__(self, name, value, typeObject):
        self.name = name
        self.value = value
        self.type = typeObject

    def showInfo(self):
        """ Return a string which are precised common parameters of object. """
        return self.name + " (Value: "+ str(self.value)+" gold, "