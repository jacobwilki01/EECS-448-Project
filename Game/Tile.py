import pygame

class Tile():
    def __init__(self, size, x, y):
        self.rect = pygame.Rect(x, y, size, size)

    def update(self, shift):
        self.rect.topleft += shift