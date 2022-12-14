from turtle import clear
import pygame
from Settings import *
from Sprite import Sprite

class Menu:
    def __init__(self, window: Window):
        self.window = window
        self.backround_Rect = pygame.Rect(0, 0, window.width, window.height)
        self.button_Rect = pygame.Rect(0 , 0 , 200, 100)
        self.button_Rect_small = pygame.Rect(0, 0, 100, 32.5)

    def run(self, events, load_error):
        #Draw background
        background = Sprite(['menu_background.png'], self.backround_Rect)
        background.draw(self.window.screen)

        #Draw Title
        rect = pygame.Rect(0, 0, 500, 280)
        rect.center = (self.window.width/2, self.window.height/2 - 200)
        title = Sprite(['Alpha_Speed.png'], rect)
        title.draw(self.window.screen)

        #Draw New
        rect2 = pygame.Rect(0, 0, 200, 100)
        rect2.center = (self.window.width/4 - 50, (self.window.height/4)*3)
        new = Sprite(['new_game.png'], rect2)
        new.draw(self.window.screen)

        #Draw Load
        rect3 = pygame.Rect(0, 0, 200, 100)
        rect3.center = (self.window.width/2 , (self.window.height/4)*3)
        load = Sprite(['load_game.png'], rect3)
        load.draw(self.window.screen)

        #Draw Quit
        rect4 = pygame.Rect(0, 0, 200, 100)
        rect4.center = ((self.window.width/4)*3 + 50,(self.window.height/4)*3)
        quit = Sprite(['quit.png'], rect4)
        quit.draw(self.window.screen)

        #Draw Settings
        rect5 = pygame.Rect(0, 0, 100, 32.5)
        rect5.center = (rect3.center[0], rect3.center[1] + 90)
        settings = Sprite(['settings_texture.png'], rect5)
        settings.draw(self.window.screen)

        #Draw Load Error Text
        if load_error:
            error_text = pygame.font.SysFont('Cambria', 20)
            load_error = error_text.render('No save file found', True, '#000000')
            self.window.screen.blit(load_error, (rect3.x + 25, rect3.y + 70))

        #Check for button click
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if rect2.collidepoint(event.pos):
                    return 1
                elif rect3.collidepoint(event.pos):
                    return 2
                elif rect4.collidepoint(event.pos):
                    return 3
                elif rect5.collidepoint(event.pos):
                    return 4
                

class Settings(Menu):
    def __init__(self, window: Window, current_res):
        super().__init__(window)
        self.button_Rect = pygame.Rect(0, 0, 110, 25)
        self.cursor = pygame.Rect(0, 0, 5, 15)
        self.line = pygame.Rect(0, 0, 300, 2)

        self.update = [False, current_res]

    def run(self,events):
        #Draw background
        background = Sprite(['menu_background.png'], self.backround_Rect)
        background.draw(self.window.screen)

        #Draw Title
        title_Font = pygame.font.SysFont('Cambria', 50)
        title_Text = title_Font.render('Settings', True, '#000000')
        title_Rect = title_Text.get_rect()
        title_Rect.center = (self.window.width/2, self.window.height/2 - 250)
        self.window.screen.blit(title_Text, title_Rect)

        #Draw Screen Resolution Info
        screenRes_text = pygame.font.SysFont('Cambria', 25)
        img = screenRes_text.render('Screen Resolution:', True, '#000000')
        self.window.screen.blit(img, (self.window.width/2 - 190, self.window.height/2 - 150))

        #Draw Screen Resolution Menu
        resolution_sizes = [(800,600),(1024,768),(1280,720),(1920,1080)]
        self.window.current_res = self.update[1]

        self.screenRes_rect = self.button_Rect.copy()
        #self.screenRes_rect.width += 10*current_res
        self.screenRes_rect.center = (self.window.width/2 + 100, self.window.height/2 - 135)
        pygame.draw.rect(self.window.screen, '#d77467', self.screenRes_rect)

        screenRes_text = pygame.font.SysFont('Cambria', 20)
        res_img = screenRes_text.render(f'{self.window.width}x{self.window.height}', True, '#000000')

        text_center = ((len(str(self.window.width)) + len(str(self.window.height))) - 6) * 3.5

        self.window.screen.blit(res_img, (self.screenRes_rect.x + 15 - text_center, self.screenRes_rect.y + 2))
        
        #Screen Resolution Arrows
        right_arrow = pygame.image.load('graphics/menu_arrow.png')
        right_arrow.convert()

        right_rect = right_arrow.get_rect()
        right_rect.center = (self.window.width/2 + 169, self.window.height/2 - 135)
        pygame.draw.rect(self.window.screen, '#000000', right_rect)
        self.window.screen.blit(right_arrow, right_rect)

        left_arrow = pygame.image.load('graphics/menu_arrow_left.png')
        left_arrow.convert()

        left_rect = left_arrow.get_rect()
        left_rect.center = (self.window.width/2 + 30, self.window.height/2 - 135)
        pygame.draw.rect(self.window.screen, '#000000', left_rect)
        self.window.screen.blit(left_arrow, left_rect)

        #Draw Jump Button Key Button
        jump_button_text = pygame.font.SysFont('Cambria', 25)
        jump_button_img = jump_button_text.render('Jump Key:', True, '#000000')
        self.window.screen.blit(jump_button_img, (self.window.width/2 - 190, self.window.height/2 - 100))

        self.jump_button_rect = self.button_Rect.copy()
        self.jump_button_rect.center = (self.window.width/2 - 20, self.window.height/2 - 85)
        pygame.draw.rect(self.window.screen, '#d77467', self.jump_button_rect)
        if self.window.get_keys()[0] == pygame.K_UP:
            pygame.draw.rect(self.window.screen, '#c73c2a', self.jump_button_rect, 2)

        up_text = pygame.font.SysFont('Cambria', 20)
        up_img = up_text.render('Up Arrow', True, '#000000')
        self.window.screen.blit(up_img, (self.jump_button_rect.x + 12, self.jump_button_rect.y + 1))

        self.jump_button_rect_2 = self.button_Rect.copy()
        self.jump_button_rect_2.center = (self.window.width/2 + 100, self.window.height/2 - 85)
        pygame.draw.rect(self.window.screen, '#d77467', self.jump_button_rect_2)
        if self.window.get_keys()[0] == pygame.K_w:
            pygame.draw.rect(self.window.screen, '#c73c2a', self.jump_button_rect_2, 2)

        up_text = pygame.font.SysFont('Cambria', 20)
        up_img = up_text.render('W', True, '#000000')
        self.window.screen.blit(up_img, (self.jump_button_rect_2.x + 45, self.jump_button_rect_2.y + 1))

        self.jump_button_rect_3 = self.button_Rect.copy()
        self.jump_button_rect_3.center = (self.window.width/2 + 220, self.window.height/2 - 85)
        pygame.draw.rect(self.window.screen, '#d77467', self.jump_button_rect_3)
        if self.window.get_keys()[0] == pygame.K_SPACE:
            pygame.draw.rect(self.window.screen, '#c73c2a', self.jump_button_rect_3, 2)
        
        up_text = pygame.font.SysFont('Cambria', 20)
        up_img = up_text.render('Space', True, '#000000')
        self.window.screen.blit(up_img, (self.jump_button_rect_3.x + 30, self.jump_button_rect_3.y + 1))

        #Draw Left Button Key Button
        left_button_text = pygame.font.SysFont('Cambria', 25)
        left_button_img = left_button_text.render('Left Key:', True, '#000000')
        self.window.screen.blit(left_button_img, (self.window.width/2 - 190, self.window.height/2 - 50))

        self.left_button_rect = self.button_Rect.copy()
        self.left_button_rect.center = (self.window.width/2 + 160, self.window.height/2 - 35)
        pygame.draw.rect(self.window.screen, '#d77467', self.left_button_rect)
        if self.window.get_keys()[1] == pygame.K_LEFT:
            pygame.draw.rect(self.window.screen, '#c73c2a', self.left_button_rect, 2)

        left_text = pygame.font.SysFont('Cambria', 20)
        left_img = left_text.render('Left Arrow', True, '#000000')
        self.window.screen.blit(left_img, (self.left_button_rect.x + 8, self.left_button_rect.y + 1))

        self.left_button_rect_2 = self.button_Rect.copy()
        self.left_button_rect_2.center = (self.window.width/2 + 40, self.window.height/2 - 35)
        pygame.draw.rect(self.window.screen, '#d77467', self.left_button_rect_2)
        if self.window.get_keys()[1] == pygame.K_a:
            pygame.draw.rect(self.window.screen, '#c73c2a', self.left_button_rect_2, 2)

        left_text = pygame.font.SysFont('Cambria', 20)
        left_img = left_text.render('A', True, '#000000')
        self.window.screen.blit(left_img, (self.left_button_rect_2.x + 48, self.left_button_rect_2.y + 1))

        #Draw Right Button Key Button
        right_button_text = pygame.font.SysFont('Cambria', 25)
        right_button_img = right_button_text.render('Right Key:', True, '#000000')
        self.window.screen.blit(right_button_img, (self.window.width/2 - 190, self.window.height/2))

        self.right_button_rect = self.button_Rect.copy()
        self.right_button_rect.center = (self.window.width/2 + 160, self.window.height/2 + 15)
        pygame.draw.rect(self.window.screen, '#d77467', self.right_button_rect)
        if self.window.get_keys()[2] == pygame.K_RIGHT:
            pygame.draw.rect(self.window.screen, '#c73c2a', self.right_button_rect, 2)

        right_text = pygame.font.SysFont('Cambria', 20)
        right_img = right_text.render('Right Arrow', True, '#000000')
        self.window.screen.blit(right_img, (self.right_button_rect.x + 2, self.right_button_rect.y + 1))
        
        self.right_button_rect_2 = self.button_Rect.copy()
        self.right_button_rect_2.center = (self.window.width/2 + 40, self.window.height/2 + 15)
        pygame.draw.rect(self.window.screen, '#d77467', self.right_button_rect_2)
        if self.window.get_keys()[2] == pygame.K_d:
            pygame.draw.rect(self.window.screen, '#c73c2a', self.right_button_rect_2, 2)

        right_text = pygame.font.SysFont('Cambria', 20)
        right_img = right_text.render('D', True, '#000000')
        self.window.screen.blit(right_img, (self.right_button_rect_2.x + 48, self.right_button_rect_2.y + 1))

        #exit rectangle
        exit_rect = self.button_Rect.copy()
        exit_rect.center = (self.window.width/2, self.window.height - 50)
        pygame.draw.rect(self.window.screen, '#d77467', exit_rect)

        exit_text = pygame.font.SysFont('Cambria', 20)
        exit_img = exit_text.render('Exit', True, '#000000')
        self.window.screen.blit(exit_img, (exit_rect.x + 38, exit_rect.y + 1))


        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                #Below is some fun boolean math to prevent the need for multiple if statements
                #Ask Ian for clarification if needed
                right_collide = right_rect.collidepoint(event.pos)
                left_collide = -(left_rect.collidepoint(event.pos))
                collide = right_collide + left_collide
                if collide:
                    if self.window.current_res == (3*collide + 3)/2:
                        self.window.current_res = int((-3*collide + 3)/2)
                    else:
                        self.window.current_res += collide
                    self.window.update_screen_res(resolution_sizes[self.window.current_res])
                    self.update = [True, self.window.current_res]
                
                if self.jump_button_rect.collidepoint(event.pos):
                    self.window.set_keys([pygame.K_UP,self.window.get_keys()[1],self.window.get_keys()[2]])
                elif self.jump_button_rect_2.collidepoint(event.pos):
                    self.window.set_keys([pygame.K_w,self.window.get_keys()[1],self.window.get_keys()[2]])
                elif self.jump_button_rect_3.collidepoint(event.pos):
                    self.window.set_keys([pygame.K_SPACE,self.window.get_keys()[1],self.window.get_keys()[2]])
                elif self.left_button_rect.collidepoint(event.pos):
                    self.window.set_keys([self.window.get_keys()[0],pygame.K_LEFT,self.window.get_keys()[2]])
                elif self.left_button_rect_2.collidepoint(event.pos):
                    self.window.set_keys([self.window.get_keys()[0],pygame.K_a,self.window.get_keys()[2]])
                elif self.right_button_rect.collidepoint(event.pos):
                    self.window.set_keys([self.window.get_keys()[0],self.window.get_keys()[1],pygame.K_RIGHT])
                elif self.right_button_rect_2.collidepoint(event.pos):
                    self.window.set_keys([self.window.get_keys()[0],self.window.get_keys()[1],pygame.K_d])
                elif exit_rect.collidepoint(event.pos):
                    return 1
