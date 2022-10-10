from time import sleep
from turtle import delay
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
    
        self.player = Player(screen, (252,0))

    def level_Setup(self, layout, tile_Size):
        bottom_Offset = screen_Hieght - len(layout)*tile_Size

        for indY, valY in enumerate(layout):
            for indX, valX in enumerate(valY):
                if valX == 'X':
                    x = indX * tile_Size
                    y = (indY * tile_Size) + bottom_Offset
                    tile = Tile(tile_Size, x, y)
                    self.tiles.append(tile)

    def horizontal_movement_collision(self):
        player = self.player
        player.rect.x += self.player.direction.x * self.player.speed

        for tile in self.tiles:
            if player.rect.colliderect(tile):
                if self.player.direction.x < 0:
                    player.rect.left = tile.rect.right
                elif self.player.direction.x > 0:
                    player.rect.right = tile.rect.left

    def vertical_movement_collision(self):
        player = self.player
        self.player.apply_gravity()
        self.player.collide_Floor = 0

        for tile in self.tiles:
            if player.rect.colliderect(tile):
                if self.player.direction.y > 0:
                    player.rect.bottom = tile.rect.top
                    self.player.collide_Floor = 1
                    self.player.direction.y = 0
                elif self.player.direction.y < 0:
                    player.rect.top = tile.rect.bottom
                    self.player.direction.y = 0

    def world_shift(self, shift):
        for tile in self.tiles:
            tile.update(shift)

    def scroll_x(self):
        player = self.player
        player_x = player.rect.centerx
        direction_x = player.direction.x
        shift = pygame.math.Vector2(8, 0)

        if player_x < screen_Width / 4 and direction_x < 0:
            self.world_shift(shift)
            self.player.speed = 0
        elif player_x > screen_Width - screen_Width / 4 and direction_x > 0:
            self.world_shift(-shift)
            self.player.speed = 0
        else:
            self.world_shift(0*shift)
            self.player.speed = 8

    def run(self):
        pygame.draw.rect(self.screen, '#8cbd9c', self.backround_Rect)

        for tile in self.tiles:
            pygame.draw.rect(self.screen, '#c8c8c8', tile.rect)
    

        self.player.update()
        self.scroll_x()
        self.horizontal_movement_collision()
        self.vertical_movement_collision()
        
        pygame.draw.rect(self.screen, '#c73c3e', self.player.rect)
        