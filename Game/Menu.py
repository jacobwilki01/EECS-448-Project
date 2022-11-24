from turtle import clear
import pygame
from Settings import *

class Menu:
    def __init__(self, window: Window):
        self.window = window
        self.backround_Rect = pygame.Rect(0, 0, window.width, window.height)
        self.button_Rect = pygame.Rect(0 , 0 , 200, 100)
        self.button_Rect_small = pygame.Rect(0, 0, 100, 32.5)

    def run(self, events, load_error):
        #Draw background
        pygame.draw.rect(self.window.screen, '#9b9b9b', self.backround_Rect)

        #Draw Title
        title_Font = pygame.font.SysFont('Cambria', 100)
        title_Text = title_Font.render('Alpha Speed', True, '#000000')
        title_Rect = title_Text.get_rect()
        title_Rect.center = (self.window.width/2, self.window.height/2 - 200)
        self.window.screen.blit(title_Text, title_Rect)

        #Draw New
        self.new_button = self.button_Rect.copy()
        self.new_button.center = (self.window.width/4 - 50, (self.window.height/4)*3)
        pygame.draw.rect(self.window.screen, '#d77467', self.new_button)
        button1_text = pygame.font.SysFont('Cambria', 30)
        new = button1_text.render('New Game', True, '#000000')
        self.window.screen.blit(new, (self.new_button.x + 30, self.new_button.y + 30))

        #Draw Load
        self.load_button = self.button_Rect.copy()
        self.load_button.center = (self.window.width/2 , (self.window.height/4)*3)
        pygame.draw.rect(self.window.screen, '#d77467', self.load_button)
        button2_text = pygame.font.SysFont('Cambria', 30)
        load = button2_text.render('Load Game', True, '#000000')
        self.window.screen.blit(load, (self.load_button.x + 30, self.load_button.y + 30))

        #Draw Quit
        self.quit_button = self.button_Rect.copy()
        self.quit_button.center = ((self.window.width/4)*3 + 50,(self.window.height/4)*3)
        pygame.draw.rect(self.window.screen, '#d77467', self.quit_button)
        button2_text = pygame.font.SysFont('Cambria', 30)
        quit = button2_text.render('Quit', True, '#000000')
        self.window.screen.blit(quit, (self.quit_button.x + 70, self.quit_button.y + 30))

        #Draw Settings
        self.settings_button = self.button_Rect_small.copy()
        self.button_Rect_small.center = (self.load_button.center[0], self.load_button.center[1] + 90)
        pygame.draw.rect(self.window.screen, '#d77467', self.settings_button)
        button2_text = pygame.font.SysFont('Cambria', 20)
        settings = button2_text.render('Settings', True, '#000000')
        self.window.screen.blit(settings, (self.settings_button.x + 15, self.settings_button.y + 5))

        #Draw Load Error Text
        if load_error:
            error_text = pygame.font.SysFont('Cambria', 20)
            load_error = error_text.render('No save file found', True, '#000000')
            self.window.screen.blit(load_error, (self.load_button.x + 25, self.load_button.y + 70))

        #Check for button click
        for event in events:
            if event.type == pygame.MOUSEBUTTONUP:
                if self.new_button.collidepoint(event.pos):
                    return 1
                elif self.load_button.collidepoint(event.pos):
                    return 2
                elif self.quit_button.collidepoint(event.pos):
                    return 3
                elif self.settings_button.collidepoint(event.pos):
                    return 4
                

class Settings(Menu):
    def __init__(self, window: Window, current_res):
        super().__init__(window)
        self.button_Rect = pygame.Rect(0 , 0 , 110, 25)
        self.cursor = pygame.Rect(0, 0, 5, 15)
        self.line = pygame.Rect(0, 0, 300, 2)

        self.update = [False, self.window.current_res]
        

    def run(self,events):
        #Draw backround
        pygame.draw.rect(self.window.screen, '#9b9b9b', self.backround_Rect)
        
        #Draw Title
        title_Font = pygame.font.SysFont('Cambria', 50)
        title_Text = title_Font.render('Settings', True, '#000000')
        title_Rect = title_Text.get_rect()
        title_Rect.center = (self.window.width/2, self.window.height/2 - 250)
        self.window.screen.blit(title_Text, title_Rect)

        #Draw Screen Resolution Info
        screenRes_text = pygame.font.SysFont('Cambria', 25)
        img = screenRes_text.render('Screen Resolution:', True, '#000000')
        self.window.screen.blit(img, (self.window.width/2 - 170, self.window.height/2 - 150))

        #Draw Screen Resolution Menu
        resolution_sizes = [(800,600),(1024,768),(1280,720),(1920,1080)]
        current_res = self.update[1]

        self.screenRes_rect = self.button_Rect.copy()
        #self.screenRes_rect.width += 10*current_res
        self.screenRes_rect.center = (self.window.width/2 + 120, self.window.height/2 - 135)
        pygame.draw.rect(self.window.screen, '#d77467', self.screenRes_rect)

        screenRes_text = pygame.font.SysFont('Cambria', 20)
        res_img = screenRes_text.render(f'{self.window.width}x{self.window.height}', True, '#000000')

        text_center = ((len(str(self.window.width)) + len(str(self.window.height))) - 6) * 3.5

        self.window.screen.blit(res_img, (self.screenRes_rect.x + 15 - text_center, self.screenRes_rect.y + 2))
        
        #Screen Resolution Arrows
        right_arrow = pygame.image.load('graphics/menu_arrow.png')
        right_arrow.convert()

        right_rect = right_arrow.get_rect()
        right_rect.center = (self.window.width/2 + 189, self.window.height/2 - 135)
        pygame.draw.rect(self.window.screen, '#000000', right_rect)
        self.window.screen.blit(right_arrow, right_rect)

        left_arrow = pygame.image.load('graphics/menu_arrow_left.png')
        left_arrow.convert()

        left_rect = left_arrow.get_rect()
        left_rect.center = (self.window.width/2 + 50, self.window.height/2 - 135)
        pygame.draw.rect(self.window.screen, '#000000', left_rect)
        self.window.screen.blit(left_arrow, left_rect)

        #Draw Jump Button Key Button
        jump_button_text = pygame.font.SysFont('Cambria', 25)
        jump_button_img = jump_button_text.render('Jump Key:', True, '#000000')
        self.window.screen.blit(jump_button_img, (self.window.width/2 - 170, self.window.height/2 - 100))

        self.jump_button_rect = self.button_Rect.copy()
        self.jump_button_rect.center = (self.window.width/2 + 120, self.window.height/2 - 85)
        pygame.draw.rect(self.window.screen, '#d77467', self.jump_button_rect)

        #Draw Left Button Key Button
        left_button_text = pygame.font.SysFont('Cambria', 25)
        left_button_img = left_button_text.render('Left Key:', True, '#000000')
        self.window.screen.blit(left_button_img, (self.window.width/2 - 170, self.window.height/2 - 50))

        self.left_button_rect = self.button_Rect.copy()
        self.left_button_rect.center = (self.window.width/2 + 120, self.window.height/2 - 35)
        pygame.draw.rect(self.window.screen, '#d77467', self.left_button_rect)

        #Draw Right Button Key Button
        right_button_text = pygame.font.SysFont('Cambria', 25)
        right_button_img = right_button_text.render('Right Key:', True, '#000000')
        self.window.screen.blit(right_button_img, (self.window.width/2 - 170, self.window.height/2))

        self.right_button_rect = self.button_Rect.copy()
        self.right_button_rect.center = (self.window.width/2 + 120, self.window.height/2 + 15)
        pygame.draw.rect(self.window.screen, '#d77467', self.right_button_rect)

        #exit rectangle
        exit = pygame.image.load('graphics/exit.png')
        exit.convert()

        exit_rect = exit.get_rect()
        exit_rect.center = (20, 20)
        pygame.draw.rect(self.window.screen, "#000000", exit_rect)
        self.window.screen.blit(exit,exit_rect)

        for event in events:
            if event.type == pygame.MOUSEBUTTONUP:
                #Below is some fun boolean math to prevent the need for multiple if statements
                #Ask Ian for clarification if needed
                right_collide = right_rect.collidepoint(event.pos)
                left_collide = -(left_rect.collidepoint(event.pos))
                collide = right_collide + left_collide
                if collide:
                    if self.window.current_res == (3*collide + 3)/2:
                        self.window.current_res = int((-3*collide + 3)/2)
                    else:
                        self.window.current_res += collide
                    self.window.update_screen_res(resolution_sizes[self.window.current_res])
                    self.update = [True, self.window.current_res]
                    
                elif exit_rect.collidepoint(event.pos):
                    return 1