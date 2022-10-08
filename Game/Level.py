import pygame
from Player import Player
from Tile import Tile
from Settings import *



class Level:
    def __init__(self, screen):
        self.screen = screen

        self.floor_Rect = pygame.Rect(0, screen_Hieght-100, screen_Width, 100)
        self.backround_Rect = pygame.Rect(0, 0, screen_Width, screen_Hieght)
        self.tiles = []
    
        self.player = Player(screen, (512,0))
        self.player.rect.bottom = screen_Hieght-100

    def playerCollision(self):
        self.player.correction_Vec *= 0

        self.player.collide_Left = 0
        self.player.collide_Right = 0
        self.player.collide_Floor = 0
        self.player.collide_Ceiling = 0

        for tile in self.tiles:
            if self.player.rect.colliderect(tile.rect):
                if self.player.velocity.x < 0:
                    self.player.collide_Left = 1
                    self.player.correction_Vec.x = tile.rect.right - self.player.rect.left

                elif self.player.velocity.x > 0:
                    self.player.collide_Right = 1
                    self.player.correction_Vec.x = tile.rect.left - self.player.rect.right

                elif self.player.velocity.y >= 0:
                    self.player.collide_Floor = 1
                    self.player.correction_Vec.y = tile.rect.top - self.player.rect.bottom   
            
                
        if self.player.rect.bottom >= screen_Hieght:
            self.player.collide_Floor = 1
            self.player.correction_Vec.y = (screen_Hieght) - self.player.rect.bottom 
        

        
            
        

    def level_Setup(self, layout, tile_Size):
        bottom_Offset = screen_Hieght - len(layout)*tile_Size

        for indY, valY in enumerate(layout):
            for indX, valX in enumerate(valY):
                if valX == 'X':
                    x = indX * tile_Size
                    y = (indY * tile_Size) + bottom_Offset
                    tile = Tile(tile_Size, x, y)
                    self.tiles.append(tile)



    def run(self, events):
        pygame.draw.rect(self.screen, '#8cbd9c', self.backround_Rect)
        #pygame.draw.rect(self.screen, '#c8c8c8', self.floor_Rect)

        for tile in self.tiles:
            pygame.draw.rect(self.screen, '#c8c8c8', tile.rect)

        pygame.draw.rect(self.screen, '#c73c3e', self.player.rect)

        self.player.update()
        self.playerCollision()
        self.player.correction()
        