import random
import pygame

class Cell:    
    CELL_COLORS = [
    (80,252,54),
    (36,244,255),
    (243,31,46),
    (4,39,243),
    (254,6,178),
    (255,211,7),
    (216,6,254),
    (145,255,7),
    (7,255,182),
    (255,6,86),
    (147,7,255)]

    def __init__(self, surface, camera):
        self.surface = surface
        self.camera = camera

        self.x = random.randint(20, 1900)
        self.y = random.randint(20, 1900)
        self.mass = 8
        self.color = random.choice(Cell.CELL_COLORS)

    def draw(self):
        zoom = self.camera.zoom
        x,y = self.camera.x, self.camera.y
        center = self.x*zoom + x, self.y*zoom + y
        pygame.draw.circle(self.surface, self.color, center, int(self.mass*zoom))


class CellList:
    def __init__(self, surface, camera, count_cells):
        self.surface = surface
        self.camera = camera
        self.count_cells = count_cells
        self.count_cells_list = []
        for i in range(self.count):
            self.count_cells_list.append(Cell(self.surface, self.camera))

    def draw(self):
        for cell in self.list:
            cell.draw()
