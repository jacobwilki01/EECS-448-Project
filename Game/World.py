import pygame

class World:
    def __init__(self, levels):
        self.levels = levels
        self.current_Level = 0

    def run(self):
        if self.current_Level < len(self.levels):
            start = self.levels[self.current_Level].run()
            if type(start) == tuple:
                if start[1] == 'quit':
                    return (start[0], start[1])
                elif start[1] == 'settings':
                    return (start[0], start[1], self.current_Level)
            elif start:
                self.current_Level += 1
        else:
            return (True,'exception')
