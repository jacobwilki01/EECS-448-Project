#from time import sleep
#from turtle import delay
import pygame
from Player import Player
from Tile import Tile
from Settings import *
from time import *

class Level:
    def __init__(self, screen, layout, start_Pos, stats):
        self.screen = screen
        self.stats = stats

        self.backround_Rect = pygame.Rect(0, 0, screen_Width, screen_Height)
        self.tiles = []
        self.removed_coins = []
        self.goal = []
        self.enemies = []
    
        self.offset = pygame.Vector2(0, 0)
        self.start_pos = start_Pos
        self.player = Player(screen, self.start_pos)

        self.level_Setup(layout, 64)

        self.dummy = False

    def level_Setup(self, layout, tile_Size):
        bottom_Offset = screen_Height - len(layout)*tile_Size

        #Initializes the tiles
        for indY, valY in enumerate(layout):
            for indX, valX in enumerate(valY):
                #Basics
                if valX == 'X': #Floor
                    x = indX * tile_Size
                    y = (indY * tile_Size) + bottom_Offset
                    tile = Tile('X', tile_Size, x, y)
                    self.tiles.append(tile)
                elif valX == 'G': #Goal
                    x = indX * tile_Size
                    y = (indY * tile_Size) + bottom_Offset
                    tile = Tile('G', tile_Size, x, y)
                    self.goal.append(tile)
                
                #Features
                elif valX == 'L': #Run-Through Wall
                    x = indX * tile_Size
                    y = (indY * tile_Size) + bottom_Offset
                    tile = Tile('L', tile_Size, x, y)
                    self.tiles.append(tile)
                elif valX == 'W': #Wall Climb
                    x = indX * tile_Size
                    y = (indY * tile_Size) + bottom_Offset
                    tile = Tile('W', tile_Size, x, y)
                    self.tiles.append(tile)
                elif valX == 'B': #Lava
                    x = indX * tile_Size
                    y = (indY * tile_Size) + bottom_Offset
                    tile = Tile('B', tile_Size, x, y)
                    self.tiles.append(tile)
                elif valX == 'P': #Portal Entrance
                    x = indX * tile_Size
                    y = (indY * tile_Size) + bottom_Offset
                    tile = Tile('P', tile_Size, x, y)
                    self.tiles.append(tile)
                elif valX == 'R': #Portal Exit
                    x = indX * tile_Size
                    y = (indY * tile_Size) + bottom_Offset
                    tile = Tile('R', tile_Size, x, y)
                    self.tiles.append(tile)
                elif valX == 'M': #Super Jump
                    x = indX * tile_Size
                    y = (indY * tile_Size) + bottom_Offset
                    tile = Tile('M', tile_Size, x, y)
                    self.tiles.append(tile)
                elif valX == 'V': #Disappearing Platform
                    x = indX * tile_Size
                    y = (indY * tile_Size) + bottom_Offset
                    tile = Tile('V', tile_Size, x, y)
                    self.tiles.append(tile)

                #Items (Coins / 1-Ups)
                elif valX == 'A': #5 Coin
                    x = (indX * (tile_Size - 1)) + (tile_Size*(3/8))
                    y = ((indY * (tile_Size - 1)) + (tile_Size*(3/8))) + bottom_Offset
                    tile = Tile('A', tile_Size/4, x, y)
                    self.tiles.append(tile)
                elif valX == 'C': #1 Coin
                    x = (indX * (tile_Size - 1)) + (tile_Size*(3/8))
                    y = ((indY * (tile_Size - 1)) + (tile_Size*(3/8))) + bottom_Offset
                    tile = Tile('C', tile_Size/4, x, y)
                    self.tiles.append(tile)
                elif valX == '1': #1-Up
                    x = (indX * (tile_Size - 1)) + (tile_Size*(3/8))
                    y = ((indY * (tile_Size - 1)) + (tile_Size*(3/8))) + bottom_Offset
                    tile = Tile('1', tile_Size/4, x, y)
                    self.tiles.append(tile)
                
                #message tiles
                elif valX == '`': #Level 1 Message
                    x = indX * tile_Size
                    y = (indY * tile_Size) + bottom_Offset
                    tile = Tile('`', tile_Size, x, y)
                    self.tiles.append(tile)
                elif valX == '@': #Level 2 Message
                    x = indX * tile_Size
                    y = (indY * tile_Size) + bottom_Offset
                    tile = Tile('@', tile_Size, x, y)
                    self.tiles.append(tile)
                elif valX == '$': #Level 3 Message
                    x = indX * tile_Size
                    y = (indY * tile_Size) + bottom_Offset
                    tile = Tile('$', tile_Size, x, y)
                    self.tiles.append(tile)
                elif valX == '#': #Level 4 Message
                    x = indX * tile_Size
                    y = (indY * tile_Size) + bottom_Offset
                    tile = Tile('#', tile_Size, x, y)
                    self.tiles.append(tile)
        
        for tile in self.tiles:
            if tile.type == 'R':
                for tile2 in self.tiles:
                    if tile2.type == "P":
                        tile2.goal = tile

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
                
                if tile.type == '`' or tile.type == '@' or tile.type == '$' or tile.type == '#': continue

                if tile.type == 'W':
                    player.get_up_input()

                if tile.type == 'C' or tile.type == 'A':
                    if tile.type == 'A':
                        self.stats.update_coins(1)
                        self.stats.update_score(500)
                    else:
                        self.stats.update_coins(1)
                        self.stats.update_score(100)
                    self.removed_coins.append(tile)
                    self.tiles.remove(tile)
                elif tile.type == '1':
                    self.stats.update_lives(1)
                    self.removed_coins.append(tile)
                    self.tiles.remove(tile)
                elif self.player.speed < 0:
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
            if player.rect.colliderect(tile):
                if self.player.jump_Speed == -24 and tile.type != 'M':
                    self.player.jump_Speed = -16

                if tile.type == 'L' and self.player.speed >= self.player.max_Speed: continue
                
                if tile.type == '`' or tile.type == '@' or tile.type == '$' or tile.type == '#': continue

                if tile.type == 'B':
                    self.kill()
                    return
                
                if tile.type == 'M':
                    self.player.jump_Speed = -24

                if tile.type == 'V':
                    if not tile.been_touched:
                        tile.touched()
                    else:
                        tile.timer += 1
                    if tile.timer > 25:
                        self.tiles.remove(tile)

                if tile.type == 'C' or tile.type == 'A':
                    if tile.type == 'A':
                        self.stats.update_coins(1)
                        self.stats.update_score(500)
                    else:
                        self.stats.update_coins(1)
                        self.stats.update_score(100)
                    self.removed_coins.append(tile)
                    self.tiles.remove(tile)
                elif tile.type == '1':
                    self.stats.update_lives(1)
                    self.removed_coins.append(tile)
                    self.tiles.remove(tile)
                elif self.player.direction.y > 0:
                    player.rect.bottom = tile.rect.top
                    self.player.collide_Floor = 1
                    self.player.direction.y = 0
                elif self.player.direction.y < 0:
                    player.rect.top = tile.rect.bottom
                    self.player.direction.y = 0
                
                if tile.type == 'P':
                    self.world_shift(pygame.math.Vector2(self.player.rect.left - tile.goal.x, 0))
                    

    def world_shift(self, shift):
        for tile in self.tiles:
            if tile.type == 'P':
                tile.goal.x += shift.x
                tile.goal.y += shift.y
            tile.update(shift)

        for tile in self.goal:
            tile.update(shift)

        self.offset += shift

    def scroll_x(self):
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
                return (True)
            else: 
                return (False)

    def check_Death(self):
        if(self.player.rect.top > screen_Height):
            self.player.direction.y = 0
            self.player.speed = 0
            self.stats.update_lives(-1)
            self.player.rect.topleft = self.start_pos
            self.world_shift(-self.offset)
    
    def kill(self):
        self.player.direction.y = 0
        self.player.speed = 0
        self.stats.update_lives(-1)
        self.player.rect.topleft = self.start_pos
        self.world_shift(-self.offset)
    
    def draw_stats(self,lives,coins,score):
        font = pygame.font.SysFont('Cambria', 25)

        lives_text = font.render('Lives: ' + str(lives), True, (0,0,0))
        coins_text = font.render('Coins: ' + str(coins), True, (0,0,0))
        score_text = font.render('Score: ' + str(score), True, (0,0,0))
        
        font = pygame.font.SysFont('Cambria', 25, bold=True)

        level_text = font.render('Level ' + str(self.stats.level + 1), True, (0,0,0))

        screen.blit(level_text, (10, 10))
        screen.blit(lives_text, (110, 10))
        screen.blit(coins_text, (screen_Width-245, 10))
        screen.blit(score_text, (screen_Width-135, 10))

    def run(self):
        pygame.draw.rect(self.screen, '#cdcdcd', self.backround_Rect)
        message_font = pygame.font.SysFont('Cambria', 30, bold=True)

        if self.stats.lives <= 0:
            self.player.rect.topleft = self.start_pos
            self.stats.reset()
            return (True, 'dead')

        self.draw_stats(self.stats.lives, self.stats.coins, self.stats.score)

        for tile in self.tiles:
            if tile.type == 'X':
                pygame.draw.rect(self.screen, '#363636', tile.rect)
            elif tile.type == 'L':
                pygame.draw.rect(self.screen, '#222222', tile.rect)
            elif tile.type == 'W':
                pygame.draw.rect(self.screen, '#919191', tile.rect)
            elif tile.type == 'A':
                pygame.draw.rect(self.screen, '#59bfff', tile.rect)
            elif tile.type == 'C':
                pygame.draw.rect(self.screen, '#f7c65c', tile.rect)
            elif tile.type == 'B':
                pygame.draw.rect(self.screen, '#ff0000', tile.rect)
            elif tile.type == 'P':
                pygame.draw.rect(self.screen, '#59bfff', tile.rect)
            elif tile.type == 'R':
                pygame.draw.rect(self.screen, '#ff8e59', tile.rect)
            elif tile.type == '1':
                pygame.draw.rect(self.screen, '#00c213', tile.rect)
            elif tile.type == 'M':
                pygame.draw.rect(self.screen, '#33ff33', tile.rect)
            elif tile.type == 'V':
                pygame.draw.rect(self.screen, '#cce6ff', tile.rect)
            elif tile.type == '`':
                pygame.draw.rect(self.screen, '#cdcdcd', tile.rect)
                message = message_font.render('Run Fast!', True, (0,0,0))
                screen.blit(message, (tile.rect.x, tile.rect.y))
            elif tile.type == '@':
                pygame.draw.rect(self.screen, '#cdcdcd', tile.rect)
                message = message_font.render('Jump High!', True, (0,0,0))
                screen.blit(message, (tile.rect.x, tile.rect.y))
            elif tile.type == '$':
                pygame.draw.rect(self.screen, '#cdcdcd', tile.rect)
                message = message_font.render('Climb Up!', True, (0,0,0))
                screen.blit(message, (tile.rect.x, tile.rect.y))
            elif tile.type == '#':
                pygame.draw.rect(self.screen, '#cdcdcd', tile.rect)
                message = message_font.render('Jump as Far as You Can!', True, (0,0,0))
                screen.blit(message, (tile.rect.x, tile.rect.y))

        for tile in self.goal:
            if tile.type == 'G':
                pygame.draw.rect(self.screen, '#9ae7c0', tile.rect)

        update = self.player.update()
        if type(update) == tuple:
            if update[0]:
                return update
        
        self.horizontal_movement_collision()
        self.vertical_movement_collision()
        self.scroll_x()

        self.check_Death()

        #pygame.draw.line(self.screen, '#ffffff', (0, 536), (screen_Width, 536))
        #pygame.draw.line(self.screen, '#ffffff', (screen_Width - screen_Width / 3, 0), (screen_Width - screen_Width / 3, screen_Hieght))

        pygame.draw.rect(self.screen, '#c73c3e', self.player.rect)

        if self.check_Complete():
            self.player.speed = 0
            self.player.rect.topleft = self.start_pos
            self.world_shift(-self.offset)
            return True
        else: 
            return False