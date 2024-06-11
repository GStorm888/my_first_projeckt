import pygame
import random
from different_functions import get_distance 
import math
# from game import Game

class Player(pygame.sprite.Sprite):
    def __init__(self, image_file, position):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file).convert_alpha()
        self.up_image = self.image
        self.rect = self.image.get_rect(topleft=position)
        self.x = random.randint(100, 400)
        self.y = random.randint(100, 400)
        self.speed = 8
        self.mass = 28
        
    def render(self, window):
        window.blit(self.image, self.rect)
        player = pygame.draw.circle(self.surface, self.outlineColor, self.x, 20)
        return player

    def process_input(self):
        pass
    def update(self):
        self.rect.x += self.move_x
        self.rect.y += self.move_y 

    def set_field(self, field):
        self.field = field

    def set_position(self, position):
        self.position = position

    def eating_food(self, food):
        for eat in food:
            if get_distance((eat.x, eat.y), (self.x, self.y)) <= self.mass / 2:
                self.mass += 0,5
                food.remove(eat)

    def move(self):
        x, y, = pygame.mouse.get_pos()
        math.atan2(y - float(self.WINDOW_HEIGHT)/2, x - float(self.WINDOW_WIDTH)/2)
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
