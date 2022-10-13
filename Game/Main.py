import pygame
from Menu import *
from World import World
from Level import Level
from sys import exit
from Settings import screen_Width, screen_Hieght, frame_Rate

#temprory variables, move later
class Temp: 
    layout0 = [
    '                                      G',   
    '                                    XXX',
    '                              XXX      ',
    '                                       ',
    ' XX    XXXX             XXX            ',
    ' XX                                    ',
    ' XXXX              XXX         XXXXX   ',
    ' XXXX         XXX                      ',
    ' XXXXXXXXXX   XXX   XXXXXXXXXXXXXXXXXXX']

    layout1 = [
    '                                    XXX',
    '                 XXXX         XX       ',
    '        XXXX                           ',
    ' XX                                    ',
    ' XX                                   G',
    ' XXXX   XXX   XXX  XXX X X X X XXXX   X',
    '              XXX                      ',
    '              XXX                      ']

    tile_Size = 64
#temp variables end

#Pygame setup
pygame.init()

#Display screen setup
screen = pygame.display.set_mode((screen_Width, screen_Hieght))
clock = pygame.time.Clock()

#Game Initialization
game_State = 0
main_Menu = Menu(screen)

level0 = Level(screen, Temp.layout0, (128, 0))
level1 = Level(screen, Temp.layout1, (128, 0))

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
        if opt:
            game_State = 1
    else:
        world1.run()

    pygame.display.update()
    clock.tick(frame_Rate)


