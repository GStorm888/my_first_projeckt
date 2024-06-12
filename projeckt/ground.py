import pygame

class Ground:

    def __init__(self, surface, camera):
        self.surface = surface
        self.camera = camera
        self.color = (230,240,240)

    def draw(self):
        zoom = self.camera.zoom
        x, y = self.camera.x, self.camera.y
        for i in range(0,2001,25):
            pygame.draw.line(self.surface,  self.color, (x, i * zoom + y), (2001 * zoom + x, i * zoom + y), 3)
            pygame.draw.line(self.surface, self.color, (i * zoom + x, y), (i * zoom + x, 2001 * zoom + y), 3)
