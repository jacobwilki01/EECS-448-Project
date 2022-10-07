import pygame
from Settings import *

class Player:
    def __init__(self, surface, pos):
        self.surface = surface
        self.rect = pygame.Rect(pos, (50, 100))

        self.direction = pygame.math.Vector2(0,0)
        self.speed = 8
        self.velocity = pygame.math.Vector2(0,0)
        self.correction_Vec = pygame.math.Vector2(0,0)
        self.gravity = 0.1
        self.gravity_Speed = 0
        self.jump_Speed = 16

        self.collide_Floor = 0
        self.collide_Ceiling = 0
        self.collide_Right = 0
        self.collide_Left = 0

    def set_Movement(self):
        self.direction *= 0

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and (not self.collide_Left):
            self.direction.x += -1
        if keys[pygame.K_RIGHT] and (not self.collide_Right):
            self.direction.x += 1
        if keys[pygame.K_UP] and self.collide_Floor:
            self.direction.y += -1
        
        if self.direction.y <= -1:
            self.velocity.y += -(self.jump_Speed)
            self.direction.y += 1

        self.velocity.x = self.direction.x * self.speed
        self.velocity.y += self.gravity_Speed

        if (not self.collide_Floor):
            self.gravity_Speed += self.gravity
        else:
            self.gravity_Speed = 0
            #self.correction.y = (screen_Hieght - 100) - self.rect.bottom
            if self.velocity.y > 0:
                self.velocity.y = 0

    def correction(self):
        self.rect.topleft += self.correction_Vec

    def update(self):      
        self.set_Movement()

        self.rect.topleft += self.velocity

        
        