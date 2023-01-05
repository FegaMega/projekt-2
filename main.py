import pygame
from pygame.locals import *
from Vehicle import vehicle
from utilities import screen, sx, sy
from button import buttons
pygame.init()
player = vehicle()
settings_button = buttons(sx/2, sy/8, 92, 22, "settings_button.png", 1/8)
scroll = [0, 0]
mouse = [0, 0]
mouse = pygame.mouse.get_pos()
FONT = pygame.font.SysFont("Helvetica-bold", 50)
first_screen = True
r = True
mouse_is_clicked = False
while r == True and first_screen == True:
    screen.fill((0, 0, 0))
    mouse = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == QUIT:
            r = False    
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_is_clicked = True
    settings_button.draw()
   
    pygame.time.Clock().tick(60)
    pygame.display.update()
while r == True:
    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == QUIT:
            r = False
        if event.type == pygame.KEYDOWN:
            if event.key == K_UP:
                player.accelerate = True
            if event.key == K_DOWN:
                player.brake = True
            if event.key == K_RIGHT:
                player.turn_right = True
            if event.key == K_LEFT:
                player.turn_left = True
        if event.type == pygame.KEYUP:
            if event.key == K_RIGHT:
                player.turn_right = False
                player.change_angle = 0
            if event.key == K_LEFT:
                player.turn_left = False
                player.change_angle = 0
            if event.key == K_UP:
                player.accelerate = False
            if event.key == K_DOWN:
                player.brake = False
                
                
    scroll[0] += (player.x-scroll[0] - sy/2)/10
    scroll[1] += (player.y-scroll[1] - sy/2)/10
    if player.accelerate == True:
        player.speed += 2
    if player.brake == True:
        player.speed -= 4
    if player.turn_left == True:
        player.change_angle = 3
    if player.turn_right == True:
        player.change_angle = -3
    if player.brake == False and player.accelerate == False:
        player.speed /= 100
        round(player.speed)
    jumps_left = FONT.render(("speed: " + str(round(player.speed))), 1, (0, 0, 0))
    screen.blit(jumps_left, (10, 10))
    player.move(15, -5)
    player.draw(scroll[0], scroll[1])
    pygame.time.Clock().tick(60)
    pygame.display.update()