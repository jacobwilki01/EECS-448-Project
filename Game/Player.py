import pygame
from Settings import *
from Sprite import *
from time import *

class Player:
    def __init__(self, window: Window, pos):
        self.window = window

        self.rect = pygame.Rect(pos, (50, 50))
        image_names = [ 'player_left.png', 'player_idle.png', 'player_right.png' ]
        self.sprite = Sprite(image_names, self.rect)

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

    def draw(self, screen):
        if self.direction.x < 0:
            self.sprite.draw(screen, 'player_left.png')
        elif self.direction.x > 0:
            self.sprite.draw(screen, 'player_right.png')
        else:
            self.sprite.draw(screen, 'player_idle.png')

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
        if keys[self.window.right_key] or keys[self.window.left_key]:
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
        if self.direction.x == 0 or self.speed * self.direction.x < 0:
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
            rect = pygame.Rect(0, 0, 400, 200)
            rect.center = self.window.width/2, self.window.height/2 - 200
            paused = Sprite(['paused.png'], rect)
            paused.draw(self.window.screen)

            #draw resume button
            rect2 = pygame.Rect(0, 0, 200, 100)
            rect2.center = (self.window.width/5 , (self.window.height/4)*3)
            resume = Sprite(['resume.png'], rect2)
            resume.draw(self.window.screen)

            #draw settings button
            rect3 = pygame.Rect(0, 0, 200, 100)
            rect3.center = (self.window.width/2 , (self.window.height/4)*3)
            settings = Sprite(['settings_texture.png'], rect3)
            settings.draw(self.window.screen)

            #draw quit button
            rect4 = pygame.Rect(0, 0, 200, 100)
            rect4.center = ((self.window.width/5)*4 , (self.window.height/4)*3)
            quit = Sprite(['quit.png'], rect4)
            quit.draw(self.window.screen)

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if rect2.collidepoint(event.pos):
                        self.paused = False
                        self.window.screen.fill((0,0,0))
                        break
                    if rect3.collidepoint(event.pos):
                        return (True, 'settings')
                    if rect4.collidepoint(event.pos):
                        self.paused = False
                        return (True, 'quit')
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.paused = False
                        self.window.screen.fill((0,0,0))
                        break
