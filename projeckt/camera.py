import settings
from units import Player

class Camera:

    def __init__(self):
        self.x = 0
        self.y = 0
        self.width = settings.WINDOW_WIDTH
        self.height = settings.WINDOW_HEIGHT
        self.zoom = 0.5

    
    def centre(self, position):
        if isinstance(position, Player):
            x, y = position.x, position.y
            self.x = x - (x * self.zoom) - x + settings.WINDOW_WIDTH / 2
            self.y = y - (y * self.zoom) - y + settings.WINDOW_HEIGHT / 2
        elif type(position) == tuple:
            self.x, self.y = position


    def update(self, target):
        self.zoom = 100 / (target.mass) + 0.3
        self.centre(list)
