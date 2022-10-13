import pygame

class Tile():
    def __init__(self, type, size, x, y):
        self.rect = pygame.Rect(x, y, size, size)
        self.type = type

    def update(self, shift):
        self.rect.topleft += shift