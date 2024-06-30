import pygame as pg
from data_base import Database
class Hero:
    def __init__(self, x, y, image_path, name, score: int = 0):
        self._image = pg.image.load(image_path)
        self._image = pg.transform.scale(self._image,(300, 300))
        self._rect = self._image.get_rect(topleft=(x, y))
        self._score = score
        self._name = name
        self.create_table()
    
    def create_table(self):
        stmt = '''
        CREATE TABLE IF NOT EXISTS heroes(
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(200) UNIQUE,
        score INT UNSIGNED
        )
        '''
        Database.cursor().execute(stmt, [])

    def create_hero(self):
        stmt = f'''
        INSERT INTO heroes (name, score)
        VALUES (%s, %s)
        '''
        Database.cursor().execute(stmt, [self._name, self._score])

    def render(self, surface:pg.Surface):
        surface.blit(self._image, self._rect)
    
    def update(self):
        pass

    def is_cliked(self, pos):
        return self._rect.collidepoint(pos)

    def process_input(self, event):
            if event.type == pg.MOUSEBUTTONDOWN:
                if self.is_cliked(event.pos):
                    print(self._score)
                    self.add_score(1)
                    
    
    def add_score(self, num):
        stmt = '''
        SELECT * FROM heroes WHERE name=%s
        '''
        Database.cursor().execute(stmt, [self._name])
        results = Database.cursor().fetchall()
        print(results)
        if len(results) == 0:
            self.create_hero()

        self._score += num
        stmt = f'''
        UPDATE heroes
        SET score={self._score}
        WHERE name=%s;
        '''
        Database.cursor().execute(stmt, [self._name])
