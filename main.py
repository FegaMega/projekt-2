import pygame
from pygame.locals import *
from Vehicle import vehicle
from utilities import screen, screen_size, checkCollisions
from button import buttons
pygame.init()
player = vehicle()
settings_button = buttons(screen_size[0] / 2,(3/4) * screen_size[1], 92, 22, "settings_button.png", 2)
back_button = buttons(40, 40, 30, 30, "back_button.png", 2)
play_button = buttons(screen_size[0] / 2, settings_button.y - 32, 92, 22, "play_button.png", 2)
resolution_button = [
    buttons(screen_size[0] / 2, 1/6*screen_size[1], 92, 22, "700x700.png", 2, [700, 700]),
    buttons(screen_size[0] / 2, 1/6*screen_size[1], 92, 22, "720x1280.png", 2, [720, 1280]),
    buttons(screen_size[0] / 2, 1/6*screen_size[1], 92, 22, "1920x1080.png", 2, [1920, 1080]),
    buttons(screen_size[0] / 2, 1/6*screen_size[1], 92, 22, "2560x1440.png", 2, [2560, 1440]),
    buttons(screen_size[0] / 2, 1/6*screen_size[1], 92, 22, "unknown.png", 2, [0, 0])
    
]
chosen_resolution = 0
scroll = [0, 0]
i = 0
mouse = [0, 0]
mouse = pygame.mouse.get_pos()
FONT = pygame.font.SysFont("Helvetica-bold", 50)
first_screen = True
open_settings = False
mouse_is_clicked = False
chose_resolution = False
while first_screen == True or open_settings == True or r == True:
    while first_screen == True:
        screen.fill((20, 20, 20))
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == QUIT:
                r = False
                first_screen = False   
                open_settings = False 
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_is_clicked = True
        if mouse_is_clicked == True and checkCollisions(mouse[0], mouse[1], 1, 1, settings_button.x, settings_button.y, settings_button.xsize, settings_button.ysize) == True:
            open_settings = True
            first_screen = False
            r = False
        if mouse_is_clicked == True and checkCollisions(mouse[0], mouse[1], 1, 1, play_button.x, play_button.y, play_button.xsize, play_button.ysize) == True:
            open_settings = False
            first_screen = False
            r = True
        play_button.draw()
        settings_button.draw()
        pygame.display.update()
        pygame.time.Clock().tick(60)
        mouse_is_clicked = False
    while open_settings == True:
        screen.fill((20, 20, 20))
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == QUIT:
                r = False
                first_screen = False 
                open_settings = False 
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_is_clicked = True
        if mouse_is_clicked == True and checkCollisions(mouse[0], mouse[1], 1, 1, back_button.x, back_button.y, back_button.xsize, back_button.ysize) == True:
            open_settings = False
            first_screen = True
            r = False
        if screen_size[0] == 700 and screen_size[1] == 700:
            chosen_resolution = resolution_button[1]
        elif screen_size[0] == 720 and screen_size[1] == 1280:
            chosen_resolution = resolution_button[1]
        elif screen_size[0] == 1920 and screen_size[1] == 1080:
            chosen_resolution = resolution_button[2]
        elif screen_size[0] == 2560 and screen_size[1] == 1440:
            chosen_resolution = resolution_button[3]
        else:
            chosen_resolution = resolution_button[4]
        if mouse_is_clicked == True and checkCollisions(mouse[0], mouse[1], 1, 1, chosen_resolution.x, chosen_resolution.y, chosen_resolution.xsize, chosen_resolution.ysize) == True:
            chose_resolution = True
        if chose_resolution == True:
            i = 0
            while i < len(resolution_button) - 1:
                if i != 0:
                    resolution_button[i].y = resolution_button[i - 1].y + 44
                resolution_button[i].draw()
                i += 1
            for i in resolution_button:
                if mouse_is_clicked == True and checkCollisions(mouse[0], mouse[1], 1, 1, i.x, i.y, i.xsize, i.ysize) == True:
                    chose_resolution = False
                    chosen_resolution = i
                    screen_size = i.extrainfo
        else:
            chosen_resolution.draw()
            
        back_button.draw()

        pygame.display.update()
        pygame.time.Clock().tick(60)
        mouse_is_clicked = False
    while r == True:
        screen.fill((20, 20, 20))
        for event in pygame.event.get():
            if event.type == QUIT:
                r = False
                first_screen = False
                open_settings = False
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
                if event.key == K_ESCAPE:
                    r = False
                    first_screen = True
                    open_settings = False
                    player.accelerate = False
                    player.brake = False
                    player.turn_left = False
                    player.turn_right = False
                    player.change_angle = 0 

                    
        scroll[0] += (player.x-scroll[0] - screen_size[0]/2)/10
        scroll[1] += (player.y-scroll[1] - screen_size[1]/2)/10
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