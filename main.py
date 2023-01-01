import pygame
from pygame.locals import *
from Vehicle import vehicle
pygame.init()
player = vehicle()
sx = 700
sy = 700
screen = pygame.display.set_mode((sx, sy), 0, 32)
scroll = [0,0]
FONT = pygame.font.SysFont("Helvetica-bold", 50)
r = True
while r:
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