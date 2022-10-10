import pygame
from Settings import *

class Player:
    def __init__(self, surface, pos):
        self.surface = surface
        self.rect = pygame.Rect(pos, (50, 100))

        self.direction = pygame.math.Vector2(0,0)
        self.velocity = pygame.math.Vector2(0,0)
        #self.correction_Vec = pygame.math.Vector2(0,0)
        self.max_Speed = 8
        self.acceleration = 8
        self.gravity = .8
        self.gravity_Speed = 0
        self.jump_Speed = 16

        self.collide_Floor = 0
        self.collide_Ceiling = 0
        self.collide_Right = 0
        self.collide_Left = 0

    def correction(self, vector):
        self.rect.topleft += vector

    def set_Direction(self):
        self.direction *= 0

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.direction.x += -1
        if keys[pygame.K_RIGHT]:
            self.direction.x += 1
        if keys[pygame.K_UP]:
            self.direction.y += -1


    def set_Velocity(self):
        '''
        if self.direction.x == 0:
            self.velocity.x -= self.velocity.x
        elif abs(self.velocity.x) < self.max_Speed:
            self.velocity.x += self.acceleration * self.direction.x
'''
        self.velocity.x = self.direction.x * self.max_Speed
        if self.direction.y <= -1 and self.collide_Floor:
            self.velocity.y += -(self.jump_Speed)
        
        if (not self.collide_Floor):
            self.velocity.y += self.gravity
            
    

    def update(self):      
        self.set_Direction()
        self.set_Velocity()

    def move(self):
        self.rect.topleft += self.velocity

        
        