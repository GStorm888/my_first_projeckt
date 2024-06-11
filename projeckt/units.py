import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, image_file, position):
        pygame.sprite.Sprite.__init__(self)
        self.image_file = pygame.image.load(image_file).convert_alpha()
        self.rect = self.image.get_rect(topleft=position)
        self.move_x = 0
        self.move_y = 0
        
    def render(self, window):
        window.blit(self.image, self.rect)

    def process_input(self):
        pos = pygame.mouse.get_pos()
        self.rect.midtop = pos
        if self.punching:
            self.rect.move_ip(10, 10)

    def update(self):
        self.rect.x += self.move_x
        self.rect.y += self.move_y 