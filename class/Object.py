""" Object class is the super class of Consumable and Equipement classes"""
class Object:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def showInfo(self):
        return self.name + " (Value: "+ str(self.value)+" gold, "