import pygame
from Menu import *
from World import World
from sys import exit
from Settings import *
from time import *

#temprory variables, move later
class Temp: 
    layout0 = [
    '                                       ',   
    '                                    XXX',
    '                              XXX      ',
    '                                       ',
    ' XX    XXXX            LXXX           G',
    ' XX                    L             XX',
    ' XXXX                  L       XXXXX   ',
    ' XXXX                  L               ',
    ' XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX        ']

    layout1 = [
    '                                    XXX',
    '                 XXXX         XX       ',
    '                                  L    ',
    ' XX                               L    ',
    ' XX                               L   G',
    ' XXXX   XXX   XXX  XXXXXXXXXXXXXXXX   X',
    '              XXX                      ',
    '              XXX                      ']

    
#temp variables end

#Pygame setup
pygame.init()

#Display screen setup
screen = pygame.display.set_mode((screen_Width, screen_Height))
clock = pygame.time.Clock()

#Game Initialization
main_Menu = Menu(screen)
settings_Menu = Settings(screen)

#world1 = World(['levels/world1-level1.txt','levels/world1-level2.txt','levels/world1-level3.txt'],screen)
world1 = World(['levels/world1-level3.txt'],screen)

level_save = None

# Run until the user asks to quit
running = True
while running:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
            exit()
            # "Exit" closes the window without any errors
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_m:
                game_State = 0
    
    if game_State == 0:
        opt = main_Menu.run(events)
        if opt == 1:
            game_State = 1
        elif opt == 2:
            game_State = 2
    elif game_State == 1:
        world_run = world1.run()
        if world_run != None:
            if world_run[1] == 'quit':
                game_State = 0
            elif world_run[1] == 'settings':
                game_State = 2
                level_save = world_run[2]
            elif world_run[1] == "exception":
                game_State = 0
    elif game_State == 2:
        settings = settings_Menu.run(events)
        if settings:
            if level_save != None:
                game_State = 1
            else:
                game_State = 0

    pygame.display.update()
    clock.tick(frame_Rate)


