#from time import sleep
#from turtle import delay
import pygame
from Player import Player
from Tile import Tile
from Settings import *



class Level:
    def __init__(self, screen, layout, start_Pos):
        self.screen = screen

        self.backround_Rect = pygame.Rect(0, 0, screen_Width, screen_Hieght)
        self.tiles = []
        self.goal = []
    
        self.offset = pygame.Vector2(0, 0)
        self.start_pos = start_Pos
        self.player = Player(screen, start_Pos)

        self.level_Setup(layout, 64)

    def level_Setup(self, layout, tile_Size):
        bottom_Offset = screen_Hieght - len(layout)*tile_Size

        #Initializes the tiles
        for indY, valY in enumerate(layout):
            for indX, valX in enumerate(valY):
                if valX == 'X':
                    x = indX * tile_Size
                    y = (indY * tile_Size) + bottom_Offset
                    tile = Tile('X', tile_Size, x, y)
                    self.tiles.append(tile)
                elif valX == 'G':
                    x = indX * tile_Size
                    y = (indY * tile_Size) + bottom_Offset
                    tile = Tile('G', tile_Size, x, y)
                    self.goal.append(tile)
                elif valX == 'L':
                    x = indX * tile_Size
                    y = (indY * tile_Size) + bottom_Offset
                    tile = Tile('L', tile_Size, x, y)
                    self.tiles.append(tile)

        #Centers Camera
        shift = pygame.math.Vector2( (screen_Width/2 - self.start_pos[0]), 0)
        self.player.rect.left += shift.x
        self.start_pos += shift
        self.world_shift(shift)
        self.offset *= 0

    def horizontal_movement_collision(self):
        player = self.player

        for tile in self.tiles:
            if player.rect.colliderect(tile):
                if tile.type == 'L' and self.player.speed >= self.player.max_Speed: continue

                if self.player.speed < 0:
                    player.rect.left = tile.rect.right
                    self.player.speed = 0
                elif self.player.speed > 0:
                    player.rect.right = tile.rect.left
                    self.player.speed = 0

    def vertical_movement_collision(self):
        player = self.player
        self.player.apply_gravity()
        self.player.collide_Floor = 0

        for tile in self.tiles:
            if tile.type == 'L' and self.player.speed >= self.player.max_Speed: continue

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

        for tile in self.goal:
            tile.update(shift)

        self.offset += shift

    def scroll_x(self):
        player = self.player
        speed = self.player.speed
        shift = pygame.math.Vector2(-speed, 0)

        left_Bound = screen_Width / 3
        right_Bound = screen_Width - screen_Width / 3

        if self.player.rect.left < left_Bound and speed < 0:
            self.world_shift(shift)
            self.player.rect.left = left_Bound
        elif self.player.rect.right > right_Bound and speed > 0:
            self.world_shift(shift)
            self.player.rect.right = right_Bound

    def check_Complete(self):
        for tile in self.goal:
            if self.player.rect.colliderect(tile.rect):
                return True
            else: 
                return False

    def check_Death(self):

        if(self.player.rect.top > screen_Hieght):
            self.player.direction.y = 0
            self.player.speed = 0
            self.player.rect.topleft = self.start_pos
            self.world_shift(-self.offset)

    def run(self):
        pygame.draw.rect(self.screen, '#cdcdcd', self.backround_Rect)

        for tile in self.tiles:
            if tile.type == 'X':
                pygame.draw.rect(self.screen, '#363636', tile.rect)
            elif tile.type == 'L':
                pygame.draw.rect(self.screen, '#222222', tile.rect)


        for tile in self.goal:
            pygame.draw.rect(self.screen, '#9ae7c0', tile.rect)
    
        self.player.update()
        self.scroll_x()
        self.horizontal_movement_collision()
        self.vertical_movement_collision()

        self.check_Death()

        #pygame.draw.line(self.screen, '#ffffff', (screen_Width / 3, 0), (screen_Width / 3, screen_Hieght))
        #pygame.draw.line(self.screen, '#ffffff', (screen_Width - screen_Width / 3, 0), (screen_Width - screen_Width / 3, screen_Hieght))

        pygame.draw.rect(self.screen, '#c73c3e', self.player.rect)

        if(self.check_Complete()): 
            return(True)
        else: 
            return False

        
        