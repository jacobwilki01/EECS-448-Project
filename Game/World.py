import pygame
from Level import Level

class World:
    def __init__(self, files, screen):
        self.screen = screen
        self.levels = []
        for file in files:
            self.levels.append(self.gen_levels(file))
        self.current_Level = 0

    def gen_levels(self,file):
        opened = open(file,'r')
        lines = []
        for line in opened:
            lines.append(line)
        
        return Level(self.screen,lines,(128,0))
        
    def run(self):
        if self.current_Level < len(self.levels):
            start = self.levels[self.current_Level].run()
            if type(start) == tuple:
                if start[1] == 'quit':
                    return (start[0], start[1])
                elif start[1] == 'settings':
                    return (start[0], start[1], self.current_Level)
                elif start[1] == 'dead':
                    self.current_Level = 0
                    return (start[0], start[1])
            elif start:
                self.current_Level += 1
        else:
            self.current_Level = 0
            return (True,'exception')
