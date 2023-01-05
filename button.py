import pygame
from utilities import screen, sx, sy 
class buttons:
    def __init__(self, x, y, xsize, ysize, picture, scale_to_screen):
        self.x = x
        self.y = y
        self.xsize = xsize * abs(scale_to_screen)
        self.ysize = ysize * abs(scale_to_screen)
        self.rect = pygame.Rect(self.x, self.y, self.xsize, self.ysize)
        self.og_surf = pygame.image.load(picture)
        self.surf = pygame.transform.scale(self.og_surf, (self.xsize, self.ysize))
    def draw(self):
        screen.blit(self.surf, (self.x, self.y), self.rect)
