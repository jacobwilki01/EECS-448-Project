import pygame
from Sprite import Sprite

class Tile():
    def __init__(self, type, size, x, y, p=None):
        if type != 'B':
            self.rect = pygame.Rect(x, y, size, size)
        else:
            self.rect = pygame.Rect(x, y+8, size, size-8)
        self.type = type
        self.x = x
        self.y = y

        self.sprite = None
        self.tile_image_initialization()

        if self.type == 'P':
            self.make_teleporter()
        elif self.type == 'R' and p != None:
            p.goal = self
        
        if self.type == 'V':
            self.been_touched = False
            self.timer = 0


    def update(self, shift):
        self.rect.topleft += shift
    
    def make_teleporter(self):
        self.goal = None
    
    def touched(self):
        if self.type == 'V':
            self.been_touched = True
    
    def __str__(self):
        return f"({self.x}, {self.y})"

    def draw(self, screen):
        self.sprite.draw(screen)

    #Initializes the various tiles to their respective images
    def tile_image_initialization(self):
        #Basics
                if self.type == 'X': #Floor
                    image = ['missing.png']
                    self.sprite = Sprite(image, self.rect)

                    #Remove the below code when we have an image for this tile
                    temp_surface = pygame.Surface(self.rect.size)
                    temp_surface.fill('#363636')
                    self.sprite.states = temp_surface

                elif self.type == 'G': #Goal
                    image = ['exit_32.png']
                    self.sprite = Sprite(image, self.rect)

                    #Remove the below code when we have an image for this tile
                    #temp_surface = pygame.Surface(self.rect.size)
                    #temp_surface.fill('#9ae7c0')
                    #self.sprite.states = temp_surface
                
                #Features
                elif self.type == 'L': #Run-Through Wall
                    image = ['missing.png']
                    self.sprite = Sprite(image, self.rect)

                    #Remove the below code when we have an image for this tile
                    temp_surface = pygame.Surface(self.rect.size)
                    temp_surface.fill('#222222')
                    self.sprite.states = temp_surface
                elif self.type == 'W': #Wall Climb
                    image = ['missing.png']
                    self.sprite = Sprite(image, self.rect)

                    #Remove the below code when we have an image for this tile
                    temp_surface = pygame.Surface(self.rect.size)
                    temp_surface.fill('#919191')
                    self.sprite.states = temp_surface
                elif self.type == 'B': #Lava
                    image = ['missing.png']
                    self.sprite = Sprite(image, self.rect)

                    #Remove the below code when we have an image for this tile
                    temp_surface = pygame.Surface(self.rect.size)
                    temp_surface.fill('#ff0000')
                    self.sprite.states = temp_surface
                elif self.type == 'P': #Portal Entrance
                    image = ['teleporter_128.png']
                    self.sprite = Sprite(image, self.rect)

                    #Remove the below code when we have an image for this tile
                    #temp_surface = pygame.Surface(self.rect.size)
                    #temp_surface.fill('#59bfff')
                    #self.sprite.states = temp_surface
                elif self.type == 'R': #Portal Exit
                    image = ['teleporter_exit_128.png']
                    self.sprite = Sprite(image, self.rect)

                    #Remove the below code when we have an image for this tile
                    #temp_surface = pygame.Surface(self.rect.size)
                    #temp_surface.fill('#ff8e59')
                    #self.sprite.states = temp_surface
                elif self.type == 'M': #Super Jump
                    image = ['missing.png']
                    self.sprite = Sprite(image, self.rect)

                    #Remove the below code when we have an image for this tile
                    temp_surface = pygame.Surface(self.rect.size)
                    temp_surface.fill('#33ff33')
                    self.sprite.states = temp_surface
                elif self.type == 'V': #Disappearing Platform
                    image = ['missing.png']
                    self.sprite = Sprite(image, self.rect)

                    #Remove the below code when we have an image for this tile
                    temp_surface = pygame.Surface(self.rect.size)
                    temp_surface.fill('#cce6ff')
                    self.sprite.states = temp_surface

                #Items (Coins / 1-Ups)
                elif self.type == 'A': #5 Coin
                    image = ['coin_5_32.png']
                    self.sprite = Sprite(image, self.rect)

                    #Remove the below code when we have an image for this tile
                    #temp_surface = pygame.Surface(self.rect.size)
                    #temp_surface.fill('#59bfff')
                    #self.sprite.states = temp_surface
                elif self.type == 'C': #1 Coin
                    image = ['coin_32.png']
                    self.sprite = Sprite(image, self.rect)

                    #Remove the below code when we have an image for this tile
                    #temp_surface = pygame.Surface(self.rect.size)
                    #temp_surface.fill('#f7c65c')
                    #self.sprite.states = temp_surface
                elif self.type == '1': #1-Up
                    image = ['1_up_32.png']
                    self.sprite = Sprite(image, self.rect)

                    #Remove the below code when we have an image for this tile
                    #temp_surface = pygame.Surface(self.rect.size)
                    #temp_surface.fill('#00c213')
                    #self.sprite.states = temp_surface