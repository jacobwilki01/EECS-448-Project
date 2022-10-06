import pygame

class Player:
    def __init__(self, surface, pos):
        self.surface = surface
        self.rect = pygame.Rect(pos, (50, 100))

        self.direction = pygame.math.Vector2(0,0)
        self.speed = 8
        self.velocity = pygame.math.Vector2(0,0)
        self.gravity = 0.08
        self.gravity_Speed = 0
        self.jump_Speed = 16

        self.collide_Floor = 0
        self.collide_Ceiling = 0
        self.collide_Right = 0
        self.collide_Left = 0

    def update(self):
        self.direction *= 0

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and (not self.collide_Left):
            self.direction.x += -1
        if keys[pygame.K_RIGHT] and (not self.collide_Right):
            self.direction.x += 1
        if keys[pygame.K_UP] and self.collide_Floor:
            self.direction.y += -1
        

        self.velocity.x = self.direction.x * self.speed
        self.velocity.y = self.direction.y * self.jump_Speed
        if (not self.collide_Floor):
            self.direction.y -= self.gravity
        elif self.direction.y < 0:
            self.direction.y = 0
            
        self.rect.topleft += self.velocity