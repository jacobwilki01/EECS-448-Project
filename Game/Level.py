#from time import sleep
#from turtle import delay
import pygame
from Sprite import Sprite
from Player import Player
from Tile import Tile, Enemy
from Settings import *
from time import *

class Level:
    def __init__(self, window: Window, layout, start_Pos, stats):
        self.window = window
        self.stats = stats

        backround_Rect = pygame.Rect(0, 0, window.width, window.height)
        self.backround_sprite = []

        for i in range(-1,5):
            backround_Rect_temp = backround_Rect.copy()
            backround_Rect_temp.left = backround_Rect.width * i
            self.backround_sprite.append(Sprite(['backround_default.png'], backround_Rect_temp))

        backround_Rect.topleft = (0,0)
        self.backround_Rect = backround_Rect

        self.tiles = []
        self.items = []
        self.goal = []
        self.enemies = []
    
        self.offset = pygame.Vector2(0, 0)
        self.start_pos = start_Pos
        self.player = Player(self.window, self.start_pos)

        self.level_Setup(layout, 64)

        self.dummy = False

    def level_Setup(self, layout, tile_Size):
        bottom_Offset = self.window.height - len(layout)*tile_Size

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
                    self.items.append(tile)
                elif valX == 'C': #1 Coin
                    x = (indX * (tile_Size - 1)) + (tile_Size*(3/8))
                    y = ((indY * (tile_Size - 1)) + (tile_Size*(3/8))) + bottom_Offset
                    tile = Tile('C', tile_Size/4, x, y)
                    self.items.append(tile)
                elif valX == '1': #1-Up
                    x = (indX * (tile_Size - 1)) + (tile_Size*(3/8))
                    y = ((indY * (tile_Size - 1)) + (tile_Size*(3/8))) + bottom_Offset
                    tile = Tile('1', tile_Size/4, x, y)
                    self.items.append(tile)
                
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

                #Enemy Tiles
                elif valX == 'E': #Basic Enemy
                    x = indX * tile_Size
                    y = (indY * tile_Size) + bottom_Offset
                    tile = Enemy('E', tile_Size, x, y)
                    self.enemies.append(tile)
        
        for tile in self.tiles:
            if tile.type == 'R':
                for tile2 in self.tiles:
                    if tile2.type == "P":
                        tile2.goal = tile

        for enemy in self.enemies:
            enemy.set_collision(self.tiles)

        #Centers Camera
        shift = pygame.math.Vector2( (self.window.width/2 - self.start_pos[0]), 0)
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

                if self.player.speed < 0:
                    player.rect.left = tile.rect.right
                    self.player.speed = 0
                elif self.player.speed > 0:
                    player.rect.right = tile.rect.left
                    self.player.speed = 0

        for item in self.items:
            if player.rect.colliderect(item):
                if item.type == 'C' or tile.type == 'A':
                    if item.type == 'A':
                        self.stats.update_coins(1)
                        self.stats.update_score(500)
                    else:
                        self.stats.update_coins(1)
                        self.stats.update_score(100)
                    self.items.remove(item)
                elif item.type == '1':
                    self.stats.update_lives(1)
                    self.items.remove(item)

        for enemy in self.enemies:
            if player.rect.colliderect(enemy):
                if(enemy.type == 'E' and player.direction.y <= 0):
                    self.kill()
                

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

                
                if self.player.direction.y > 0:
                    player.rect.bottom = tile.rect.top
                    self.player.collide_Floor = 1
                    self.player.direction.y = 0
                elif self.player.direction.y < 0:
                    player.rect.top = tile.rect.bottom
                    self.player.direction.y = 0
                
                if tile.type == 'P':
                    self.world_shift(pygame.math.Vector2(self.player.rect.left - tile.goal.x, 0))

        for item in self.items:
            if player.rect.colliderect(item):    
                if item.type == 'C' or item.type == 'A':
                    if item.type == 'A':
                        self.stats.update_coins(1)
                        self.stats.update_score(500)
                    else:
                        self.stats.update_coins(1)
                        self.stats.update_score(100)
                    self.items.remove(item)
                elif item.type == '1':
                    self.stats.update_lives(1)
                    self.stats.update_score(1000)
                    self.items.remove(item)

        for enemy in self.enemies:
            if player.rect.colliderect(enemy):
                if(enemy.type == 'E'):
                    self.enemies.remove(enemy)
                    player.jump()

    def world_shift(self, shift):
        shift = pygame.math.Vector2(int(shift.x), int(shift.y))

        for tile in self.tiles:
            if tile.type == 'P':
                tile.goal.x += shift.x
                tile.goal.y += shift.y
            tile.update(shift)

        for tile in self.goal:
            tile.update(shift)

        for item in self.items:
            item.update(shift)

        for enemy in self.enemies:
            enemy.update(shift)

        for sprite in self.backround_sprite:
            sprite.rect.x += int(shift.x / 4)

        self.offset += shift

    def scroll_x(self):
        speed = self.player.speed
        shift = pygame.math.Vector2(-speed, 0)

        left_Bound = self.window.width / 3
        right_Bound = self.window.width - self.window.width / 3

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
        if(self.player.rect.top > self.window.height):
            self.player.direction.y = 0
            self.player.speed = 0
            self.stats.update_lives(-1)
            self.stats.update_score(-250)
            self.player.rect.topleft = self.start_pos
            self.world_shift(-self.offset)
    
    def kill(self):
        self.player.direction.y = 0
        self.player.speed = 0
        self.stats.update_lives(-1)
        self.stats.update_score(-250)
        self.player.rect.topleft = self.start_pos
        self.world_shift(-self.offset)
    
    def draw_stats(self,lives,coins,score):
        font = pygame.font.SysFont('Cambria', 25)

        lives_text = font.render('Lives: ' + str(lives), True, (0,0,0))
        coins_text = font.render('Coins: ' + str(coins), True, (0,0,0))
        score_text = font.render('Score: ' + str(score), True, (0,0,0))
        
        font = pygame.font.SysFont('Cambria', 25, bold=True)

        level_text = font.render('Level ' + str(self.stats.level + 1), True, (0,0,0))

        self.window.screen.blit(level_text, (10, 10))
        self.window.screen.blit(lives_text, (10, 40))
        self.window.screen.blit(coins_text, (self.window.width-145, 10))
        self.window.screen.blit(score_text, (self.window.width-145, 40))

    def run(self):
        pygame.draw.rect(self.window.screen, '#ffffff', self.backround_Rect)
        for sprite in self.backround_sprite:
            sprite.draw(self.window.screen)

        message_font = pygame.font.SysFont('Cambria', 30, bold=True)

        if self.stats.lives <= 0:
            self.player.rect.topleft = self.start_pos
            self.stats.reset()
            return (True, 'dead')

        self.draw_stats(self.stats.lives, self.stats.coins, self.stats.score)

        for tile in self.tiles:
            #Messages
            if tile.type == '`': #Level 1 (Run-Through Walls)
                #pygame.draw.rect(self.window.screen, '#000000', tile.rect)
                message = message_font.render('Run Fast!', True, (0,0,0))
                self.window.screen.blit(message, (tile.rect.x, tile.rect.y))
            elif tile.type == '@': #Level 2 (Lava)
                #pygame.draw.rect(self.window.screen, '#cdcdcd', tile.rect)
                message = message_font.render('Jump High!', True, (0,0,0))
                self.window.screen.blit(message, (tile.rect.x, tile.rect.y))
            elif tile.type == '$': #Level 3 (Wall Climb)
                #pygame.draw.rect(self.window.screen, '#cdcdcd', tile.rect)
                message = message_font.render('Climb Up!', True, (0,0,0))
                self.window.screen.blit(message, (tile.rect.x, tile.rect.y))
            elif tile.type == '#': #Level 4 (Giant Gap)
                #pygame.draw.rect(self.window.screen, '#cdcdcd', tile.rect)
                message = message_font.render('Jump as Far as You Can!', True, (0,0,0))
                self.window.screen.blit(message, (tile.rect.x, tile.rect.y))
            #------Below Not Implemented------#
            elif tile.type == '%': #Level 5 (Teleporters)
                #pygame.draw.rect(self.window.screen, '#cdcdcd', tile.rect)
                message = message_font.render('Touch to Teleport!', True, (0,0,0))
                self.window.screen.blit(message, (tile.rect.x, tile.rect.y))
            elif tile.type == '^': #Level 6 (Super Jump)
                #pygame.draw.rect(self.window.screen, '#cdcdcd', tile.rect)
                message = message_font.render('Jump Higher!', True, (0,0,0))
                self.window.screen.blit(message, (tile.rect.x, tile.rect.y))
            elif tile.type == '&': #Level 7 (Disappearing Platforms)
                #pygame.draw.rect(self.window.screen, '#cdcdcd', tile.rect)
                message = message_font.render("Don't Stay Too Long!", True, (0,0,0)) 
                self.window.screen.blit(message, (tile.rect.x, tile.rect.y))
            elif tile.type == '*': #Level x (First Enemy)
                #pygame.draw.rect(self.window.screen, '#cdcdcd', tile.rect)
                message = message_font.render('Avoid the Enemies!', True, (0,0,0))
                self.window.screen.blit(message, (tile.rect.x, tile.rect.y))
            elif tile.type == '(': #Level x (Second Enemy)
                #pygame.draw.rect(self.window.screen, '#cdcdcd', tile.rect)
                message = message_font.render('Jump on their Heads!', True, (0,0,0))
                self.window.screen.blit(message, (tile.rect.x, tile.rect.y))
            #Everyother type of tile
            else:
                tile.draw(self.window.screen)

        for item in self.items:
            item.draw(self.window.screen)

        for tile in self.goal:
            if tile.type == 'G':
                tile.draw(self.window.screen)

        for enemy in self.enemies:
            enemy.draw(self.window.screen)
            enemy.move()


        update = self.player.update()
        if type(update) == tuple:
            if update[0]:
                return update
        
        self.horizontal_movement_collision()
        self.vertical_movement_collision()
        self.scroll_x()

        self.check_Death()

        #pygame.draw.line(self.window.screen, '#ffffff', (0, 536), (self.window.width, 536))
        #pygame.draw.line(self.window.screen, '#ffffff', (self.window.width - self.window.width / 3, 0), (self.window.width - self.window.width / 3, self.window.hieght))

        #pygame.draw.rect(self.window.screen, '#c73c3e', self.player.rect)
        self.player.draw(self.window.screen)

        if self.check_Complete():
            self.player.speed = 0
            self.player.rect.topleft = self.start_pos
            self.stats.update_score(1000)
            self.world_shift(-self.offset)
            return True
        else: 
            return False