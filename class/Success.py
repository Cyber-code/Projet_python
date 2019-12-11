class Success:
    def __init__(self, name):
        self.name = name
        self.unlock = False

    def showInfo(self):
        statut = "locked"
        if(self.unlock):
            statut = "unlocked"
        return "\n{} {}.".format(self.name, statut)