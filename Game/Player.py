import pygame
#from Settings import *

class Player:
    def __init__(self, surface, pos):
        self.surface = surface
        self.rect = pygame.Rect(pos, (50, 100))

        self.direction = pygame.math.Vector2(0,0)
        self.speed = 0
        self.max_Speed = 8
        self.acc = 0.2
        self.gravity = .8
        self.jump_Speed = -16

        self.collide_Floor = 0
        self.collide_Ceiling = 0
        self.collide_Right = 0
        self.collide_Left = 0

    def jump(self):
        self.direction.y = self.jump_Speed

    def get_input(self):
        keys = pygame.key.get_pressed()

        self.direction.x = 0
        if keys[pygame.K_RIGHT]:
            self.direction.x += 1
        if keys[pygame.K_LEFT]:
            self.direction.x += -1
            

        if keys[pygame.K_UP] and self.collide_Floor:
            self.jump()
            
    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def update(self):
        self.get_input()
        
        if abs(self.speed) < self.max_Speed or self.speed * self.direction.x < 0:
            self.speed += self.acc * self.direction.x
        if self.direction.x == 0:
            if abs(self.speed) < .5: self.speed = 0
            sign = -1 if self.speed > 0 else 1
            self.speed += self.acc * sign

        self.speed = round(self.speed, 1)

        self.rect.left += self.speed


        
        