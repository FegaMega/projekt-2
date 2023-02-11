import pygame
from pygame.locals import *
from Vehicle import vehicle
from utilities import screen, screen_size, bakround_color, checkCollisions
from button import buttons
import utilities
pygame.init()
level = [

]
player = vehicle()
settings_button = buttons(screen_size[0] / 2 - 11,(3/4) * screen_size[1], 92, 22, "settings_button.png", 2)
back_button = buttons(40, 40, 30, 30, "back_button.png", 2)
play_button = buttons(screen_size[0] / 2 - 11, settings_button.y - 32, 92, 22, "play_button.png", 2)
resolution_button = [
    buttons(screen_size[0] / 2, 1/6*screen_size[1], 92, 22, "700x700.png", 2, [700, 700]),
    buttons(screen_size[0] / 2, 1/6*screen_size[1], 92, 22, "720x1280.png", 2, [1280, 720]),
    buttons(screen_size[0] / 2, 1/6*screen_size[1], 92, 22, "1920x1080.png", 2, [1920, 1080]),
    buttons(screen_size[0] / 2, 1/6*screen_size[1], 92, 22, "2560x1440.png", 2, [2560, 1440]),
    buttons(screen_size[0] / 2, 1/6*screen_size[1], 92, 22, "unknown.png", 2, [700, 700])
    
]
dark_or_light_mode_buttons = [
    buttons(screen_size[0] / 2, resolution_button[0].y + 22, 92, 22, "light.png", 2, ["light", (255, 255, 255)]),
    buttons(screen_size[0] / 2, resolution_button[0].y + 22, 92, 22, "dark.png", 2, ["dark", (20, 20, 20)])
]
chose_dol_mode = False
chosen_dol_mode = 0
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
        screen.fill(bakround_color)
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
        settings_button.change_pos(screen_size[0] / 2 - (settings_button.xsize / 2),(3/4) * screen_size[1])
        play_button.change_pos(screen_size[0] / 2 - (play_button.xsize / 2), settings_button.y - play_button.ysize - 10)
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
            chosen_resolution = resolution_button[0]
        elif screen_size[0] == 1280 and screen_size[1] == 720:
            chosen_resolution = resolution_button[1]
        elif screen_size[0] == 1920 and screen_size[1] == 1080:
            chosen_resolution = resolution_button[2]
        elif screen_size[0] == 2560 and screen_size[1] == 1440:
            chosen_resolution = resolution_button[3]
        else:
            chosen_resolution = resolution_button[4]
        if bakround_color == (255, 255, 255):
            chosen_dol_mode = dark_or_light_mode_buttons[0]
        elif bakround_color == (20, 20, 20):
            chosen_dol_mode = dark_or_light_mode_buttons[1]
        else:
            bakround_color = (20, 20, 20)
            chosen_dol_mode = dark_or_light_mode_buttons[1]
        if mouse_is_clicked == True and checkCollisions(mouse[0], mouse[1], 1, 1, chosen_resolution.x, chosen_resolution.y, chosen_resolution.xsize, chosen_resolution.ysize) == True and chose_dol_mode == False:
            chose_resolution = True
            mouse_is_clicked = False
        if mouse_is_clicked == True and checkCollisions(mouse[0], mouse[1], 1, 1, chosen_dol_mode.x, chosen_dol_mode.y, chosen_dol_mode.xsize, chosen_dol_mode.ysize) == True and chose_resolution == False:
            chose_dol_mode = True
            mouse_is_clicked = False

            
        back_button.draw()
        chosen_dol_mode.draw()
        if chose_resolution == True:
            i = 0
            while i < len(resolution_button) - 1:
                if i == 0:
                    resolution_button[i].x = screen_size[0]/2 - resolution_button[i].xsize/2
                else:
                    resolution_button[i].change_pos(resolution_button[i - 1].x, resolution_button[i - 1].y + 22)


                resolution_button[i].draw()
                i += 1
            for i in resolution_button:
                if mouse_is_clicked == True and checkCollisions(mouse[0], mouse[1], 1, 1, i.x, i.y, i.xsize, i.ysize) == True:
                    chose_resolution = False
                    chosen_resolution = i
                    screen_size = i.extrainfo
                    utilities.screen = pygame.display.set_mode((screen_size[0], screen_size[1]), 0, 32)
                    
        elif chose_dol_mode:
            chosen_resolution.change_pos(screen_size[0] / 2, 1/6*screen_size[1])
            chosen_resolution.draw()
        if chose_dol_mode == True:
            i = 0
            mouse_is_clicked = False
            while i < len(dark_or_light_mode_buttons) - 1:
                if i == 0:
                    dark_or_light_mode_buttons[i].x = screen_size[0]/2 - dark_or_light_mode_buttons[i].xsize/2
                if i != 0:
                    dark_or_light_mode_buttons[i].change_pos(dark_or_light_mode_buttons[i - 1].x + 92, dark_or_light_mode_buttons[i - 1].y + 66)


                dark_or_light_mode_buttons[i].draw()
                i += 1
            for i in dark_or_light_mode_buttons:
                if mouse_is_clicked == True and checkCollisions(mouse[0], mouse[1], 1, 1, i.x, i.y, i.xsize, i.ysize) == True:
                    chose_resolution = False
                    chosen_dol_mode = i
                    utilities.bakround_color = i.extrainfo
        elif chose_resolution:
            chosen_resolution.change_pos(screen_size[0] / 2, 1/6*screen_size[1])
            chosen_resolution.draw()
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
            player.speed += 1
        if player.brake == True:
            player.speed -= 1.5
        if player.turn_left == True:
            player.change_angle = 3
        if player.turn_right == True:
            player.change_angle = -3
        if player.brake == False and player.accelerate == False:
            player.speed -= player.speed / 50
            round(player.speed)
        player.move(15, 0)
        jumps_left = FONT.render(("speed: " + str(round(player.speed))), 1, (0, 0, 0))
        screen.blit(jumps_left, (10, 10))
        player.draw(scroll[0], scroll[1])
        pygame.time.Clock().tick(60)
        pygame.display.update()