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
                    image = ['missing.png']
                    self.sprite = Sprite(image, self.rect)

                    #Remove the below code when we have an image for this tile
                    temp_surface = pygame.Surface(self.rect.size)
                    temp_surface.fill('#9ae7c0')
                    self.sprite.states = temp_surface
                
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
                    image = ['missing.png']
                    self.sprite = Sprite(image, self.rect)

                    #Remove the below code when we have an image for this tile
                    temp_surface = pygame.Surface(self.rect.size)
                    temp_surface.fill('#59bfff')
                    self.sprite.states = temp_surface
                elif self.type == 'R': #Portal Exit
                    image = ['missing.png']
                    self.sprite = Sprite(image, self.rect)

                    #Remove the below code when we have an image for this tile
                    temp_surface = pygame.Surface(self.rect.size)
                    temp_surface.fill('#ff8e59')
                    self.sprite.states = temp_surface
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
                    image = ['missing.png']
                    self.sprite = Sprite(image, self.rect)

                    #Remove the below code when we have an image for this tile
                    temp_surface = pygame.Surface(self.rect.size)
                    temp_surface.fill('#59bfff')
                    self.sprite.states = temp_surface
                elif self.type == 'C': #1 Coin
                    image = ['missing.png']
                    self.sprite = Sprite(image, self.rect)

                    #Remove the below code when we have an image for this tile
                    temp_surface = pygame.Surface(self.rect.size)
                    temp_surface.fill('#f7c65c')
                    self.sprite.states = temp_surface
                elif self.type == '1': #1-Up
                    image = ['missing.png']
                    self.sprite = Sprite(image, self.rect)

                    #Remove the below code when we have an image for this tile
                    temp_surface = pygame.Surface(self.rect.size)
                    temp_surface.fill('#00c213')
                    self.sprite.states = temp_surface

#A basic left and right moving enemy that can be killed be jumping on its head
class Enemy(Tile):
    def __init__(self, type, size, x, y):
        super().__init__(type, size, x, y)
        self.speed = 4
        self.direction = -1

        self.bound_left = -float('inf')
        self.bound_right = float('inf')

        image = ['missing.png']
        self.sprite = Sprite(image, self.rect)
        #Remove the below code when we have an image for this
        temp_surface = pygame.Surface(self.rect.size)
        temp_surface.fill('#919191')
        self.sprite.states = temp_surface

    def set_collision(self, tile_arr):
        center = self.rect.centerx

        boundbox = self.rect.copy()
        boundbox.left -= 2500
        boundbox.width = 5000
        
        for tile in tile_arr:
            if boundbox.colliderect(tile.rect):
                temp_left = tile.rect.right - center
                temp_right = tile.rect.left - center
                self.bound_left = tile.rect.right if (tile.rect.right > self.bound_left and temp_left < 0) else self.bound_left
                self.bound_right = tile.rect.left if (tile.rect.left < self.bound_right and temp_right > 0) else self.bound_right


    def update(self, shift):
        super().update(shift)
        self.bound_left += shift.x
        self.bound_right += shift.x

    def move(self):
        self.rect.left += self.speed * self.direction

        if self.rect.right > self.bound_right:
            self.rect.right = self.bound_right
            self.direction *= -1
        elif self.rect.left < self.bound_left:
            self.rect.left = self.bound_left
            self.direction *= -1