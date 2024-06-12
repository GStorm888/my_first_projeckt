import pygame
from units import Player
from cell import Cell
from ground import Ground
import settings
from camera import Camera
from units import Object
class Game():

    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Agar.io Mini")
        
        self.clock = pygame.time.Clock()
        self.running = True
        self.player = Player(0)


    def process_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                return
        self.player.process_input()

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWNE:
                    if event.key == pygame.K_SPACE:
                        del(camera)
                    if event.key == pygame.K_w:
                        list.split()
                if event.type == pygame.QUIT:
                    pygame.QUIT
                    quit()

    def update_game_state(self):
        self.player.update()

    def render(self):
        settings.MAIN_WINDOW.fill(pygame.color.THECOLORS(["white"]))
        self.player.render(settings.MAIN_WINDOW)
        pygame.display.update() 

    def main_loop(self):
        camera = Camera()
        ground = Ground(settings.MAIN_WINDOW, camera)
        cell = Cell(settings.MAIN_WINDOW, camera, 2000)
        player = Player(settings.MAIN_WINDOW, camera, "Player")

        object = Object()
        object.add(ground)
        object.add(cell)
        object.add(player)   

        self.process_input

        list.move()
        list.eating_food(list(cell))
        camera.update(list)
        settings.MAIN_WINDOW.fill((242,251,255))
        object.paint()
        pygame.display.flip()

game = Game()
game.main_loop
