import pygame
from utilities import screen
class buttons:
    def __init__(self, x, y, xsize, ysize, picture, scale_to_screen, extrainformation=[0]):
        self.picture = picture
        self.scale_to_screen = scale_to_screen
        self.extrainfo = extrainformation
        self.xsize = xsize * abs(scale_to_screen)
        self.ysize = ysize * abs(scale_to_screen)
        self.x: int = x - (self.xsize/2)
        self.y: int = y - (self.ysize/2)
        self.rect = pygame.Rect(self.x, self.y, self.xsize, self.ysize)
        self.og_surf = pygame.image.load(self.picture)
        self.surf = pygame.transform.scale(self.og_surf, (self.xsize, self.ysize))
    def change_pos(self, x, y):
        self.x: int = x
        self.y: int = y
    def draw(self):
        screen.blit(self.surf, (self.x, self.y))
        self.rect = pygame.Rect(self.x, self.y, self.xsize, self.ysize)
        self.og_surf = pygame.image.load(self.picture)
        self.surf = pygame.transform.scale(self.og_surf, (self.xsize, self.ysize))
