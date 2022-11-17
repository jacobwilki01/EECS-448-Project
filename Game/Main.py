import pygame
from Menu import *
from World import World
from Level import Level
from sys import exit
from Settings import *

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

    tile_Size = 64
#temp variables end

#Pygame setup
pygame.init()

#Display screen setup
screen = pygame.display.set_mode((screen_Width, screen_Height))
clock = pygame.time.Clock()

#Game Initialization
game_State = 0
main_Menu = Menu(screen)
settings_Menu = Settings(screen)

level0 = Level(screen, Temp.layout0, (128, 0),main_Menu,settings_Menu)
level1 = Level(screen, Temp.layout1, (128, 0),main_Menu,settings_Menu)

world1_Levels = [ level0, level1]
world1 = World(world1_Levels)

# Run until the user asks to quit
running = True
while running:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
            exit()
            # "Exit" closes the window without any errors
    
    if game_State == 0:
        opt = main_Menu.run(events)
        if opt == 1:
            game_State = 1
        elif opt == 2:
            game_State = 2
    elif game_State == 1:
        world1.run()
    elif game_State == 2:
        settings = settings_Menu.run(events)
        if settings:
            game_State = 0

    pygame.display.update()
    clock.tick(frame_Rate)


