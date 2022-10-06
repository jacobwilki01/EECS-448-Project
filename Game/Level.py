import pygame
from Player import *
from Settings import *

class Level:
    def __init__(self, screen):
        self.screen = screen
        self.floor_Rect = pygame.Rect(0, screen_Hieght-100, screen_Width, 100)
        self.backround_Rect = pygame.Rect(0, 0, screen_Width, screen_Hieght)
        self.player = Player(screen, (0,screen_Hieght-100))
        self.player.rect.bottom = screen_Hieght-100

    def playerCollision(self):
        if self.player.rect.left <= 0:
            self.player.collide_Left = 1
        else:
            self.player.collide_Left = 0

        if self.player.rect.right >= screen_Width:
            self.player.collide_Right = 1
        else:
            self.player.collide_Right = 0
        
        if self.player.rect.bottom >= screen_Hieght-100:
            self.player.collide_Floor = 1
        else:
            self.player.collide_Floor = 0
        

    def run(self, events):
        pygame.draw.rect(self.screen, '#8cbd9c', self.backround_Rect)
        pygame.draw.rect(self.screen, '#c8c8c8', self.floor_Rect)

        pygame.draw.rect(self.screen, '#c73c3e', self.player.rect)

        self.playerCollision()
        self.player.update(events)
        