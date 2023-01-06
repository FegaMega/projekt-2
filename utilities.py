import pygame
screen_size = [700, 700]

screen = pygame.display.set_mode((screen_size[0], screen_size[1]), 0, 32)
def checkCollisions(a_x, a_y, a_width, a_height, b_x, b_y, b_width, b_height):
    return (a_x + a_width > b_x) and (a_x < b_x + b_width) and (a_y + a_height > b_y) and (a_y < b_y + b_height)
