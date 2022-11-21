import pygame

class Window:
    @staticmethod
    def __init__(self):
        self.width = 800
        self.height = 600
        self.frame_rate = 60
        self.game_state = 0
    def get_width(self):
        return self.width
    def get_height(self):
        return self.height
    def get_frame_rate(self):
        return self.frame_rate
    def get_game_state(self):
        return self.game_state
    def set_game_state(self, state):
        self.game_state = state
    def update_screen_res(self,res,scr,width,height):
        scr = pygame.display.set_mode(res)
        pygame.display.update()
        width = res[0]
        height = res[1]
        return scr


window = Window()
screen_Width = window.get_width()
screen_Height = window.get_height()
frame_Rate = window.get_frame_rate()
game_State = window.get_game_state()
screen = pygame.display.set_mode((screen_Width, screen_Height))