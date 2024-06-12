import pygame
import random
from different_functions import get_distance 
import math
from cell import Cell


class Player():
    def __init__(self, surface, camera, name = "Denis"):
        self.surface = surface
        self.camera = camera

        self.speed = 8
        self.mass = 18

        self.x = random.randint(100, 400)
        self.y = random.randint(100, 400)

        color = random.choice(Cell.CELL_COLORS)


    def render(self, window):
        window.blit(self.image, self.rect)
        player = pygame.draw.circle(self.surface, self.outlineColor, self.x, 20)
        

    def update(self):
        self.rect.x += self.move_x
        self.rect.y += self.move_y 

    def eating_food(self, food):
        for eat in food:
            if get_distance((eat.x, eat.y), (self.x, self.y)) <= self.mass / 2:
                self.mass += 0,5
                food.remove(eat)

    def move(self):
        x, y, = pygame.mouse.get_pos()
        rotation = math.atan2(y - float(self.WINDOW_HEIGHT)/2,
                    x - float(self.WINDOW_WIDTH)/2)
        rotation *= 180/math.pi
        normalized = (90 - math.fabs(rotation))/90
        buf_x = self.speed*normalized
        buf_y = 0
        if rotation < 0:
            buf_y = -self.speed + math.fabs(buf_x)
        else:
            buf_y = self.speed - math.fabs(buf_x)
        self.x = self.x + buf_x
        self.y = self.y + buf_y

    def draw(self):
        zoom = self.camera.zoom
        x, y = self.camera.x, self.camera.y
        center = self.x * zoom + x, self.y * zoom + y
        pygame.draw.circle(self.surface, self.outlineColor, center, int((self.mass/2 + 3)*zoom))
        pygame.draw.circle(self.surface, self.color, center, int(self.mass/2*zoom))



class Object:
    def __init__(self):
        self.objects = []

    def add(self, object):
        self.objects.append(object)

    def draw(self):
        for object in self.objects:
            object.draw()
