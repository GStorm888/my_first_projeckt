import pygame as pg
from hero import Hero
class Game:
    def __init__(self, width, height) -> None:
        self._width = width
        self._height = height
        self._screen = pg.display.set_mode((width, height))
        self._running = True
        self._game_odjects = [Hero(100, 100, "image.png", "GStorm888")]

    def process_input(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self._running = False
            elif event.type == pg.MOUSEBUTTONDOWN:
                for obj in self._game_odjects:
                    obj.process_input(event)

    def update(self):
        pass

    def render(self):
        self._screen.fill(pg.color.THECOLORS["azure"])
        for obj in self._game_odjects:
            obj.render(self._screen)
        pg.display.flip()

    def run(self):
        while self._running:
            self.process_input()
            self.update()
            self.render()
        pg.quit()

game = Game(500, 500)
game.run()
