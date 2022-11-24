import pygame

class Window:
    def __init__(self):
        self.width = 800
        self.height = 600
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.frame_rate = 60
        self.game_state = 0

        self.current_res = 0

        self.jump_key = pygame.K_UP
        self.left_key = pygame.K_LEFT
        self.right_key = pygame.K_RIGHT

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
    
    def get_keys(self):
        return [self.jump_key, self.left_key, self.right_key]
    
    def set_keys(self, keys):
        self.jump_key = keys[0]
        self.left_key = keys[1]
        self.right_key = keys[2]

    def update_screen_res(self,res):
        self.screen = pygame.display.set_mode(res)
        #pygame.display.update() 
        self.width = res[0]
        self.height = res[1]
    
    def save_settings(self):
        file = open("saves/settings.txt", "w")
        file.write(str(self.width) + "\n")
        file.write(str(self.height) + "\n")
        file.write(str(self.current_res) + "\n")

        file.close()
    
    def save_keybinds(self):
        file = open("saves/keybinds.txt", "w")
        file.write(str(self.jump_key) + "\n")
        file.write(str(self.left_key) + "\n")
        file.write(str(self.right_key) + "\n")

        file.close()

'''
window = Window()
screen_Width = window.get_width()
screen_Height = window.get_height()
frame_Rate = window.get_frame_rate()
game_State = window.get_game_state()
screen = pygame.display.set_mode((screen_Width, screen_Height))
'''