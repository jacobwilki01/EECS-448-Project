import pygame
from Level import Level
from Settings import Window
from Stats import World_Stats

class World:
    def __init__(self, files, window: Window):
        self.window = window
        self.stats = World_Stats()
        self.levels = []
        self.backgrounds = ['background_day.png','background_sunset.png','background_night.png']

        for file in files:
            self.levels.append(self.gen_levels(file))

    def gen_levels(self,file):
        opened = open(file,'r')
        lines = []
        for line in opened:
            lines.append(line)
        
        opened.close()

        return Level(self.window, lines, (128,0), self.stats, self.backgrounds[len(self.levels) // 3])
        
    def run(self):
        if self.stats.level < len(self.levels):
            start = self.levels[self.stats.level].run()
            if type(start) == tuple:
                if start[1] == 'quit':
                    return (start[0], start[1])
                elif start[1] == 'settings':
                    return (start[0], start[1], self.stats.level)
                elif start[1] == 'dead':
                    self.stats.update_level(-self.stats.level)
                    return (start[0], start[1])
            elif start:
                self.stats.update_level(1)
        else:
            self.stats.update_level(-self.stats.level)
            return (True,'exception')
