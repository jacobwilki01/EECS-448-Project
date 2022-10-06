import pygame
from sys import exit
from Settings import screen_Width, screen_Hieght, frame_Rate
pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([screen_Width, screen_Hieght])
pygame.display.set_caption("Menu")
clock = pygame.time.Clock()

Background_surface = pygame.image.load("graphics/Background.png")
#fill method give the surface a color


# Run until the user asks to quit
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            exit()
            # "Exit" closes the window without any errors
    
    
    screen.blit(Background_surface,(0,0))

    pygame.display.update()
    clock.tick(frame_Rate)


