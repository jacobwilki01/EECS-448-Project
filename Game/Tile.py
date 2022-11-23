import pygame

class Tile():
    def __init__(self, type, size, x, y, p=None):
        if type != 'B':
            self.rect = pygame.Rect(x, y, size, size)
        else:
            self.rect = pygame.Rect(x, y+8, size, size-8)
        self.type = type
        self.x = x
        self.y = y

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