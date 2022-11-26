import pygame

class Sprite():
    #Provide a list of images and a rect and the image will scale to the rect
    #note the list of images should contain the file name of the image in graphics
    def __init__(self, image_names : list, rect: pygame.Rect):
        self.rect = rect
        self.states = dict()

        for name in image_names:
            image = pygame.image.load('graphics/' + name).convert()
            image = pygame.transform.scale(image, (rect.width, rect.height))
            self.states[name] = image

    #provide just an image and an x, y positon and the image will be placed within
    #a same size rect at the x, y position
    '''
    def __init__(self, image, x, y):
        image = pygame.image.load(image).convert()
        self.rect = image.get_rect()
        self.rect.topleft = (x, y)
    '''
        

    def draw(self, screen, state):
        screen.blit(self.states[state], self.rect.topleft)