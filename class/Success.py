class Success:
    """ Success are unlocked if the player did required conditions to unlock it."""

    def __init__(self, name):
        self.name = name
        self.unlock = False

    def showInfo(self):
        """ This method return a string containing success's parameters. """
        statut = "locked"
        if(self.unlock):
            statut = "unlocked"
        return "\n{} {}.".format(self.name, statut)