""" Object class is the super class of Consumable and Equipement classes"""
class Object:
    def __init__(self, name, value, typeObject):
        self.name = name
        self.value = value
        self.type = typeObject

    def showInfo(self):
        return self.name + " (Value: "+ str(self.value)+" gold, "