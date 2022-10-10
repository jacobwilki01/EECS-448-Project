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

    def player_Collision(self):
        #self.player.correction_Vec *= 0
        #correction_Vec = pygame.math.Vector2(0, 0)

        self.player.collide_Left = 0
        self.player.collide_Right = 0
        self.player.collide_Floor = 0
        self.player.collide_Ceiling = 0

        bound_Box = pygame.Rect(self.player.rect.left-100, self.player.rect.top - 100, 200, 300)
        tiles = []
        for tile in self.tiles:
            if tile.rect.colliderect(bound_Box):
                tiles.append(tile)

        p = [self.player.rect.topleft, self.player.rect.topright, self.player.rect.bottomright, self.player.rect.bottomleft]
        pV = self.player.velocity

        for tile in tiles:
            g = [tile.rect.topleft, tile.rect.topright, tile.rect.bottomright, tile.rect.bottomleft]
            gV = [0, 0, 0, 0]
            gV_Perp = [0, 0, 0, 0]
            for i in range(0, 4):
                gV[i] =  pygame.math.Vector2(g[(i+1)%4]) - pygame.math.Vector2(g[i])
                gV_Perp[i] = pygame.math.Vector2(gV[i].y, -(gV[i].x))
        
            for i in range(0, 4):
                pV = self.player.velocity
                for j in range(0, 4):
            

                    denomCross = pV.cross(gV[j])
                    temp = pygame.math.Vector2(g[j]) - pygame.math.Vector2(p[i])
                    
                    if denomCross != 0 :
                        t = temp.cross(gV[j]) / denomCross
                        u = temp.cross(pV) / denomCross
                        
                        if t >= 0 and t <= 1 and abs(u - (1/2)) <= 1/2:
                            #perp_Vec = -1 if(self.player.collide_Floor) else 1
                            #print(t, gV_Perp[j], self.player.velocity.y*t, self.player.velocity.y, (self.player.velocity.y*t + p[i][1]) - (self.player.velocity.y + p[i][1]))
                            if (self.player.velocity.y * (gV_Perp[j][1]) <= 0):
                                self.player.velocity.y += (self.player.velocity.y*t + p[i][1]) - (self.player.velocity.y + p[i][1])
                                #self.player.velocity.x += (self.player.velocity.x*t + p[i][0]) - (self.player.velocity.x + p[i][0])
                            elif (self.player.velocity.x * (gV_Perp[j][0]) <= 0):
                                self.player.velocity.x += (self.player.velocity.x*t + p[i][0]) - (self.player.velocity.x + p[i][0])
                            
                            print(gV_Perp[j])
                            if gV_Perp[j][0] == 0:
                                if gV_Perp[j][1] < 0:
                                    self.player.collide_Floor = 1  
                                else:
                                    self.player.collide_Ceiling = 1
                            else:
                                if gV_Perp[j][0] < 0:
                                    self.player.collide_Right = 1
                                else:
                                    self.player.collide_Left = 1
                            break
                    

        '''
        p = pygame.math.Vector2(self.player.rect.bottomleft)
        pV = self.player.velocity
        g = pygame.math.Vector2(0, screen_Hieght)
        gV = pygame.math.Vector2(screen_Width, 0)

        denomCross = pV.cross(gV)
        temp = g - p
        if denomCross != 0:
            t = temp.cross(gV) / denomCross
            u = temp.cross(pV) / denomCross
            if abs(t - (1/2)) <= 1/2 and abs(u - (1/2)) <= 1/2:
                self.player.velocity = self.player.velocity * t
                self.player.collide_Floor = 1
        '''
        #print(self.player.collide_Floor, self.player.collide_Ceiling, self.player.collide_Left, self.player.collide_Right)
        #self.player.correction(correction_Vec)



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
        pygame.draw.line(self.screen, '#ffffff', self.player.rect.topleft, self.player.rect.topleft + self.player.velocity,2)
        
        self.player.update()
        self.player_Collision()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LSHIFT]:
            self.player.velocity *= 0
        self.player.move()
        #self.player.correction()
        