import pygame
from Settings import *

class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.backround_Rect = pygame.Rect(0, 0, screen_Width, screen_Hieght)
        self.button_Rect = pygame.Rect(0 , 0 , 200, 100)

    def run(self, events):
        #Draw backround
        pygame.draw.rect(self.screen, '#9b9b9b', self.backround_Rect)

        #Draw button
        self.button_Rect.center = (screen_Width/2 , screen_Hieght/2)
        pygame.draw.rect(self.screen, '#d77467', self.button_Rect)

        #Check for button click
        for event in events:
            if event.type == pygame.MOUSEBUTTONUP:
                if self.button_Rect.collidepoint(event.pos):
                    return 1