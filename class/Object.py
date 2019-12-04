class Object:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def showInfo(self):
        return "\nName: " + self.name + "\nValue: "+ str(self.value)+" gold"