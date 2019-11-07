class MapObject(object):
    token = str
    color = 0
    drawing = ''
    ch_number = 0

    def __init__(self, y, x):
        self.y, self.x = y, x

    def place(self, game_map):  # game_map is instance of `Map`
        game_map.objects[self.y, self.x] = self

class Floor(MapObject):
    token = ' '
    color = 0
    drawing = ' '
    ch_number = 32

class VerticalDoor(MapObject):
    token = '|'
    color = 233
    drawing = '▒'
    ch_number = 4194401

class HorizontalDoor(MapObject):
    token = '-'
    color = 233
    drawing = '▒'
    ch_number = 4194401

