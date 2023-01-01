import pygame, math
sx = 700
sy = 700
screen = pygame.display.set_mode((sx, sy), 0, 32)
class vehicle:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.xsize = 70
        self.ysize = 20
        self.angle = 0
        self.speed = 0
        self.rect = pygame.Rect(self.x, self.y, self.xsize, self.ysize)
        self.og_surf = pygame.transform.smoothscale(pygame.image.load("sprite-0001.jpeg").convert_alpha(), (self.xsize, self.ysize))
        self.surf = self.og_surf
        self.change_angle = 0
        self.speed_change = 0
        self.turn_left: bool = False
        self.turn_right: bool = False
        self.accelerate: bool = False
        self.brake: bool = False
    def draw(self, scroll_x, scroll_y):

        self.rect = pygame.Rect(self.x - scroll_x, self.y - scroll_y, self.xsize, self.ysize)
        screen.blit(self.surf, (self.x - scroll_x, self.y - scroll_y))
    def move(self, max_speed, reverse_max_speed):
        self.angle += self.change_angle
        self.speed += self.speed_change
        if self.speed > max_speed:
            self.speed = max_speed
        if self.speed < reverse_max_speed:
            self.speed = reverse_max_speed
        self.angle += self.change_angle
        self.angle = self.angle % 360
        self.rect = self.surf.get_rect(center=self.rect.center)
        self.surf = pygame.transform.rotate(self.og_surf, self.angle)
        self.x += math.cos(math.radians(self.angle)) * self.speed
        self.y -= math.sin(math.radians(self.angle)) * self.speed