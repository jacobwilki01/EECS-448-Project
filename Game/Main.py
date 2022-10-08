import pygame
from Menu import *
from Level import *
from sys import exit
from Settings import screen_Width, screen_Hieght, frame_Rate

#temprory variables, move later
class Temp: 
    layout = [
    '                          ',
    '                          ',
    '                          ',
    ' XX    XXXX             XX',
    ' XX                       ',
    ' XXXX              XXX    ',
    ' XXXX         XXX         ',
    ' XXXXXXXXXX   XXX   XXXXXX']
    tile_Size = 64
#temp variables end

#Pygame setup
pygame.init()

#Display screen setup
screen = pygame.display.set_mode((screen_Width, screen_Hieght))
clock = pygame.time.Clock()

#Game setup
game_State = 0
main_Menu = Menu(screen)
level = Level(screen)
level.level_Setup(Temp.layout, Temp.tile_Size)

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
        level.run(events)

    pygame.display.update()
    clock.tick(frame_Rate)


