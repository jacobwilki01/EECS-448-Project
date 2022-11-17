import pygame

class Window:
    def __init__(self):
        self.width = 800
        self.height = 600
        self.frame_rate = 60
    def get_width(self):
        return self.width
    def get_height(self):
        return self.height
    def get_frame_rate(self):
        return self.frame_rate
    def update_screen_res(self,res):
        pygame.display.set_mode(res)
        pygame.display.update()
        self.width = res[0]
        self.height = res[1]


window = Window()
screen_Width = window.get_width()
screen_Height = window.get_height()
frame_Rate = window.get_frame_rate()