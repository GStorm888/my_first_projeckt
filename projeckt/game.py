import pygame
from units import Player
class Game():

    def __init__(self):
        pygame.init()

        self.WINDOW_WIDTH = 800
        self.WINDOW_YEIGHT = 800
        self.FPS = 60

        self.main_window = pygame.display.set_mode((self.WINDOW_WIDTH,
                                                     self.WINDOW_YEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True
        self.player = Player("images\green_body.png", (0, 0))


    def process_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                return
        self.plyer.process_input()

    def update_game_state(self):
        self.plyer.update()

    def render(self):
        self.main_window.fill(pygame.color.THECOLORS(["white"]))
        self.plyer.render(self.main_window)
        pygame.display.update()

    def main_loop(self):
        while self.running:
            self.process_input()
            self.update_game_state()
            self.render()
            self.clock.tick(self.FPS)
        pygame.quit()

game = Game()
game.main_loop