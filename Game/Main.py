import pygame
from Menu import *
from World import World
from sys import exit
from Settings import *
from time import *

#Pygame setup
pygame.init()
pygame.display.set_caption('Alpha Speed')
#need to add icon

#Display screen setup
clock = pygame.time.Clock()

#Game Initialization
main_Menu = Menu(screen)
settings_Menu = Settings(screen)

#Misc. Extra Variables
has_died = True
level_save = None
load_error = False

#Running Loop
running = True
while running:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT or game_State == 3:
            running = False
            world.stats.write_save_file()
            exit()
    
    if has_died:
        world = World(['levels/world1-level1.txt','levels/world1-level2.txt','levels/world1-level3.txt','levels/world1-level4.txt'],screen)
        #world = World(['levels/superjumptest.txt'],screen)
        has_died = False

    if game_State == 0:
        opt = main_Menu.run(events,load_error)
        if opt != None:
            game_State = opt
    elif game_State == 1:
        world.stats.reset()
        load_error = False
        game_State = 5
    elif game_State == 2:
        if not world.stats.has_updated:
            game_State = 0
            load_error = True
        else:
            game_State = 5
    elif game_State == 4:
        settings = settings_Menu.run(events)
        if settings:
            if level_save != None:
                game_State = 1
            else:
                game_State = 0
    elif game_State == 5:
        world_run = world.run()
        if world_run != None:
            if world_run[1] == 'quit':
                game_State = 0
            elif world_run[1] == 'settings':
                game_State = 4
                level_save = world_run[2]
            elif world_run[1] == "exception":
                game_State = 0
            elif world_run[1] == "dead":
                game_State = 0
                has_died = True

    pygame.display.update()
    clock.tick(frame_Rate)