import pygame, sys
import constants
from raindrop import Raindrop
from character import Player

pygame.init()

#Set the title for the window
pygame.display.set_caption("Mi Primer Juego")
#Create the window for the game
screen = pygame.display.set_mode((constants.WINDOW_WIDTH,constants.WINDOW_HEIGHT))

clock = pygame.time.Clock()

heroe = Player(50, 50)


# raindrops = []

#The Game Loop
while True:
    dt = clock.tick(constants.FPS)
    #Polling the events generated from the user
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


    screen.fill((200,200,200))
    heroe.update()
    heroe.draw(screen)
  
    pygame.display.flip()
    #Show the images in the screen and update the frame
    pygame.display.update()
    
