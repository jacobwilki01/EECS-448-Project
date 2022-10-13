import pygame

class World:
    def __init__(self, levels):
        self.levels = levels
        self.current_Level = 0

    def run(self):
        if(self.current_Level == 0):
            if(self.levels[0].run()): self.current_Level += 1
        elif(self.current_Level == 1):
            if(self.levels[1].run()): pass    