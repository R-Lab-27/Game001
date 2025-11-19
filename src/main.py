import pygame, sys
from pygame.locals import *
import constans

pygame.init()

#Create the window for the game
screen = pygame.display.set_mode((constans.WINDOW_WIDTH,constans.WINDOW_HEIGHT))

#The Game Loop
while True:
    #Polling the events generated from the user
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill((200,200,200))
    #Draw some shapes to the screen
    pygame.draw.circle(screen,(0,180,200), (150,150), 10, 2) #(target_screen, circle_color, circle_position, size, border)
    #Show the images in the screen and update the frame
    pygame.display.update()
