import pygame
from Menu import *
from World import World
from sys import exit
from Settings import *
from time import *

#Pygame setup
pygame.init()
pygame.display.set_caption('Alpha Speed')
pygame.display.set_icon(pygame.image.load("graphics/player_idle.png"))

window = Window()

level_files =  ['levels/world1-level1.txt',
                'levels/world1-level2.txt',
                'levels/world1-level3.txt',
                'levels/world1-level4.txt',
                'levels/world1-level5.txt',
                'levels/world1-level6.txt',
                'levels/world1-level7.txt',
                'levels/world1-level8.txt',
                'levels/world1-level9.txt',
                'levels/game-complete.txt',]

#Try loading user settings
try:
    file = open("saves/settings.txt", "r")
    window.update_screen_res((int(file.readline()), int(file.readline())))
    window.current_res = int(file.readline())
    file.close()
except:
    pass

#Try loading user keybinds
try:
    file = open("saves/keybinds.txt", "r")
    window.set_keys([int(file.readline()), int(file.readline()), int(file.readline())])
    file.close()
except:
    pass

#Display screen setup
clock = pygame.time.Clock()

#Game Initialization
main_Menu = Menu(window)
settings_Menu = Settings(window, window.current_res)

#Misc. Extra Variables
has_died = True
level_save = None
load_error = False

#Running Loop
running = True
while running:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT or window.game_state == 3:
            running = False
            world.stats.write_save_file()
            window.save_settings()
            window.save_keybinds()
            exit()
    
    if has_died:
        world = World(level_files, window)
        loading = False
        has_died = False

    if window.game_state == 0:
        opt = main_Menu.run(events,load_error)
        if opt != None:
            window.game_state = opt
    elif window.game_state == 1:
        world.stats.reset()
        load_error = False
        window.game_state = 5
    elif window.game_state == 2:
        if not world.stats.has_updated:
            window.game_state = 0
            load_error = True
        else:
            window.game_state = 5
    elif window.game_state == 4:
        settings = settings_Menu.run(events)

        #Checks to see if the settings menu has updated the resolution
        if settings_Menu.update[0]:
            current_res = settings_Menu.update[1]
            #if so re-initializes all menus and levels to the new window
            main_Menu = Menu(window)
            settings_Menu = Settings(window, current_res)
            world = World(level_files, window)
            #settings_Menu.update = False

        if settings:
            if level_save != None:
                window.game_state = 2
            else:
                window.game_state = 0

    elif window.game_state == 5:
        world_run = world.run()
        if world_run != None:
            if world_run[1] == 'quit':
                window.game_state = 0
                level_save = None
            elif world_run[1] == 'settings':
                window.game_state = 4
                level_save = world_run[2]
            elif world_run[1] == "finished":
                window.game_state = 6
            elif world_run[1] == "dead":
                window.game_state = 0
                has_died = True
    elif window.game_state == 6:
        world.stats.write_save_file()
        window.game_state = 0
        has_died = True

    pygame.display.update()
    clock.tick(window.frame_rate)