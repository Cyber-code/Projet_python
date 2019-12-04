from Object import Object

class Equipement(Object):
    def __init__(self, name, value):
        Object.__init__(self, name, value)

    def showInfo(self):
        return Object.showInfo(self)