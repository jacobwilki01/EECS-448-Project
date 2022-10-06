import pygame

class Player:
    def __init__(self, surface, pos):
        self.surface = surface
        self.rect = pygame.Rect(pos, (50, 100))

        self.direction = pygame.math.Vector2(0,0)
        self.speed = 8
        self.velocity = pygame.math.Vector2(0,0)
        self.gravity = 0.8
        self.jump_Speed = -16

        self.collide_Floor = 0
        self.collide_Ceiling = 0
        self.collide_Right = 0
        self.collide_Left = 0

    def update(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT and (not self.collide_Left):
                    self.direction.x = -1
                if event.key == pygame.K_RIGHT and not self.collide_Right:
                    self.direction.x = 1
                if event.key == pygame.K_UP and self.collide_Floor:
                    self.direction.y = -1
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    self.direction.x = 0
                if event.key == pygame.K_UP:
                    self.direction.y = 0

        self.velocity = self.direction * self.speed
        if (not self.collide_Floor):
            self.velocity += pygame.math.Vector2(0,1) * self.gravity

        self.rect.topleft += self.velocity