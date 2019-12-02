class Inventory:
    def __init__(self):
        self.objects = []
        self.gold = 0
        self.weapon = {"leftHand": None, "rigthHand": None}     # 2 Slots for weapons in each hand
        self.jewels = {"jewel1": None, "jewel2": None}       # 2 Slots for jewels
        self.armor = {"head": None, "chest": None, "pants": None, "arms": None, "legs": None}       # 5 Slots for armor => head, chest, pants, arms, legs
        
