import pygame

class Tile():
    def __init__(self, type, size, x, y, a=None):
        self.rect = pygame.Rect(x, y, size, size)
        self.type = type
        self.x = x
        self.y = y

        if self.type == 'A':
            self.make_teleporter()
        elif self.type == 'B' and a != None:
            a.goal = self

    def update(self, shift):
        self.rect.topleft += shift
    
    def make_teleporter(self):
        self.goal = None
    
    def __str__(self):
        return f"({self.x}, {self.y})"