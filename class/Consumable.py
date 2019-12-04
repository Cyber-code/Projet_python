from Object import Object

class Consumable(object):
    def __init__(self, name, value):
        Object.__init__(self, name, value)
        # Add effect(s) of the potion