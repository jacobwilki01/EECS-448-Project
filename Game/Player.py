import pygame
from Settings import *
from time import *

class Player:
    def __init__(self, window: Window, pos):
        self.window = window
        self.rect = pygame.Rect(pos, (50, 100))

        self.direction = pygame.math.Vector2(0,0)
        self.speed = 0
        self.max_Speed = 8
        self.acc = 0.2
        self.gravity = .8
        self.jump_Speed = -16

        self.collide_Floor = 0
        self.collide_Ceiling = 0
        self.collide_Right = 0
        self.collide_Left = 0

        self.pause_bg = pygame.Rect(0, 0, self.window.width, self.window.height)
        self.pause_button = pygame.Rect(0 , 0 , 200, 100)

    def jump(self):
        self.direction.y = self.jump_Speed

    def get_input(self):
        keys = pygame.key.get_pressed()

        self.direction.x = 0
        if keys[self.window.right_key]:
            self.direction.x += 1
        if keys[self.window.left_key]:
            self.direction.x += -1
            

        if keys[self.window.jump_key] and self.collide_Floor:
            self.jump()

        if keys[pygame.K_ESCAPE]:
            self.paused = True
            pause = self.pause()
            if type(pause) == tuple:
                if pause[0]:
                    return pause
            sleep(0.1)
    
    def get_up_input(self):
        keys = pygame.key.get_pressed()

        self.direction.y = 0
        if keys[self.window.right_key]:
            self.direction.y -= 5

    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def update(self):
        input = self.get_input()
        if type(input) == tuple:
            if input[0]:
                return input
        
        if abs(self.speed) < self.max_Speed or self.speed * self.direction.x < 0:
            self.speed += self.acc * self.direction.x
        if self.direction.x == 0:
            if abs(self.speed) < .5: self.speed = 0
            sign = -1 if self.speed > 0 else 1
            self.speed += self.acc * sign

        self.speed = round(self.speed, 1)

        self.rect.left += self.speed

    def pause(self):
        self.window.screen.fill((255,255,255))
        while self.paused:
            #draw background
            pygame.draw.rect(self.window.screen, '#9b9b9b', self.pause_bg)

            #draw title
            title_font = pygame.font.SysFont('Cambria', 100)
            title = title_font.render('Paused', True, (0,0,0))
            title_rect = title.get_rect()
            title_rect.center = (self.window.width / 2, self.window.height / 2 - 200)
            self.window.screen.blit(title, title_rect)

            #draw buttons
            button_text = pygame.font.SysFont('Cambria', 30)

            self.restart_button = self.pause_button.copy()
            self.restart_button.center = (self.window.width/5 , (self.window.height/4)*3)
            pygame.draw.rect(self.window.screen, '#d77467', self.restart_button)
            text = button_text.render('Resume', True, (0,0,0))
            self.window.screen.blit(text, (self.restart_button.x + 50, self.restart_button.y + 30))

            self.settings_button = self.pause_button.copy()
            self.settings_button.center = (self.window.width/2 , (self.window.height/4)*3)
            pygame.draw.rect(self.window.screen, '#d77467', self.settings_button)
            text = button_text.render('Settings', True, (0,0,0))
            self.window.screen.blit(text, (self.settings_button.x + 50, self.settings_button.y + 30))

            self.quit_button = self.pause_button.copy()
            self.quit_button.center = ((self.window.width/5)*4 , (self.window.height/4)*3)
            pygame.draw.rect(self.window.screen, '#d77467', self.quit_button)
            text = button_text.render('Quit', True, (0,0,0))
            self.window.screen.blit(text, (self.quit_button.x + 70, self.quit_button.y + 30))

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.restart_button.collidepoint(event.pos):
                        self.paused = False
                        self.window.screen.fill((0,0,0))
                        break
                    if self.settings_button.collidepoint(event.pos):
                        return (True, 'settings')
                    if self.quit_button.collidepoint(event.pos):
                        self.paused = False
                        return (True, 'quit')
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.paused = False
                        self.window.screen.fill((0,0,0))
                        break
