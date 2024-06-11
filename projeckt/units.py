import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, image_file, position):
        pygame.sprite.Sprite.__init__(self)
        self.image_file = pygame.image.load(image_file).convert_alpha()
        
    def render(self, window):
        window.blit(self.image, self.rect)