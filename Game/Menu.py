from turtle import clear
import pygame
from Settings import *

class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.backround_Rect = pygame.Rect(0, 0, screen_Width, screen_Height)
        self.button_Rect = pygame.Rect(0 , 0 , 200, 100)

    def run(self, events):
        #Draw backround
        pygame.draw.rect(self.screen, '#9b9b9b', self.backround_Rect)

        #Draw Title
        title_Font = pygame.font.SysFont('Cambria', 100)
        title_Text = title_Font.render('Alpha Speed', True, '#000000')
        title_Rect = title_Text.get_rect()
        title_Rect.center = (screen_Width/2, screen_Height/2 - 200)
        self.screen.blit(title_Text, title_Rect)

        #Draw button
        self.button_Rect.center = (screen_Width/3 , (screen_Height/4)*3)
        pygame.draw.rect(self.screen, '#d77467', self.button_Rect)
        button1_text = pygame.font.SysFont('Cambria', 30)
        img = button1_text.render('Start', True, '#000000')
        self.screen.blit(img, (self.button_Rect.x + 70, self.button_Rect.y + 30))

        #Draw button 2
        self.button_Rect2 = self.button_Rect.copy()
        self.button_Rect2.center = ((screen_Width/3)*2,(screen_Height/4)*3)
        pygame.draw.rect(self.screen, '#d77467', self.button_Rect2)
        button2_text = pygame.font.SysFont('Cambria', 30)
        img = button2_text.render('Settings', True, '#000000')
        self.screen.blit(img, (self.button_Rect2.x + 50, self.button_Rect2.y + 30))

        #Check for button click
        for event in events:
            if event.type == pygame.MOUSEBUTTONUP:
                if self.button_Rect.collidepoint(event.pos):
                    return 1
                elif self.button_Rect2.collidepoint(event.pos):
                    return 2

class Settings(Menu):
    def __init__(self, screen):
        super().__init__(screen)
        self.button_Rect = pygame.Rect(0 , 0 , 100, 25)
        self.cursor = pygame.Rect(0, 0, 5, 15)
        self.line = pygame.Rect(0, 0, 300, 2)
    def run(self,events):
        #Draw backround
        pygame.draw.rect(self.screen, '#9b9b9b', self.backround_Rect)
        
        #Draw Title
        title_Font = pygame.font.SysFont('Cambria', 50)
        title_Text = title_Font.render('Settings', True, '#000000')
        title_Rect = title_Text.get_rect()
        title_Rect.center = (screen_Width/2, screen_Height/2 - 250)
        self.screen.blit(title_Text, title_Rect)

        #Draw Screen Resolution Info
        screenRes_text = pygame.font.SysFont('Cambria', 25)
        img = screenRes_text.render('Screen Resolution:', True, '#000000')
        self.screen.blit(img, (screen_Width/4 - 100, screen_Height/2 - 150))

        #Draw Screen Resolution Menu
        self.screenRes_rect = self.button_Rect.copy()
        self.screenRes_rect.center = (screen_Width/4 + 190, screen_Height/2 - 135)
        pygame.draw.rect(self.screen, '#d77467', self.screenRes_rect)

        screenRes_text = pygame.font.SysFont('Cambria', 20)
        res_img = screenRes_text.render(f'{screen_Height}x{screen_Width}', True, '#000000')
        self.screen.blit(res_img, (self.screenRes_rect.x + 10, self.screenRes_rect.y + 2))

        resolution_sizes = [(800,600),(1024,768),(1280,720),(1920,1080)]
        current_res = 0
        
        #Screen Resolution Arrows
        right_arrow = pygame.image.load('graphics/menu_arrow.png')
        right_arrow.convert()

        right_rect = right_arrow.get_rect()
        right_rect.center = (screen_Width/4 + 254, screen_Height/2 - 135)
        pygame.draw.rect(self.screen, '#000000', right_rect)
        self.screen.blit(right_arrow, right_rect)

        left_arrow = pygame.image.load('graphics/menu_arrow_left.png')
        left_arrow.convert()

        left_rect = left_arrow.get_rect()
        left_rect.center = (screen_Width/4 + 125, screen_Height/2 - 135)
        pygame.draw.rect(self.screen, '#000000', left_rect)
        self.screen.blit(left_arrow, left_rect)

        #exit rectangle
        exit = pygame.image.load('graphics/exit.png')
        exit.convert()

        exit_rect = exit.get_rect()
        exit_rect.center = (20, 20)
        pygame.draw.rect(self.screen, "#000000", exit_rect)
        self.screen.blit(exit,exit_rect)

        for event in events:
            if event.type == pygame.MOUSEBUTTONUP:
                if right_rect.collidepoint(event.pos):
                    if current_res == 3:
                        current_res = 0
                    else:
                        current_res += 1
                    self.screen = window.update_screen_res(resolution_sizes[current_res],self.screen)
                    
                elif exit_rect.collidepoint(event.pos):
                    return 1