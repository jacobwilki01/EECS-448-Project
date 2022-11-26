import pygame

class Sprite():
    #Provide a list of images and a rect and the image will scale to the rect
    #note the list of images should contain the file name of the image in graphics
    def __init__(self, image_names : list, rect: pygame.Rect):
        self.rect = rect
        self.states = None

        if len(image_names) == 1:
            image = pygame.image.load('graphics/' + image_names[0]).convert()
            image = pygame.transform.scale(image, (rect.width, rect.height))
            self.states = image
        else: 
            self.states = dict()
            for name in image_names:
                image = pygame.image.load('graphics/' + name).convert()
                image = pygame.transform.scale(image, (rect.width, rect.height))
                self.states[name] = image      

    #Draws the sprite according to the given state
    #Note: A state is only needed if more than 1 states are possible
    def draw(self, screen, state=None):
        if type(self.states) == dict:
            screen.blit(self.states[state], self.rect.topleft)
        else:
            screen.blit(self.states, self.rect.topleft)