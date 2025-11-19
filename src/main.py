import random
import pygame, sys
from pygame.locals import *
import constants
from raindrop import Raindrop
from character import Character

pygame.init()

#Set the title for the window
pygame.display.set_caption("Mi Primer Juego")
#Create the window for the game
screen = pygame.display.set_mode((constants.WINDOW_WIDTH,constants.WINDOW_HEIGHT))

clock = pygame.time.Clock()
heroe = Character("Ren")

raindrops = []

#The Game Loop
while True:
    dt =clock.tick(constants.FPS)
    #Polling the events generated from the user
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[K_RIGHT] or pressed_keys[K_d]:
        xpos += 1
    if pressed_keys[K_LEFT] or pressed_keys[K_a]:
        xpos -= 1
    if pressed_keys[K_UP] or pressed_keys[K_w]:
        ypos -= 1
    if pressed_keys[K_DOWN] or pressed_keys[K_s]:
        ypos += 1

    raindrops.append(Raindrop())


    screen.fill((200,200,200))
    # #Draw some shapes to the screen
    # pygame.draw.circle(screen,(0,180,200), (xpos,ypos), 10, 2) #(target_screen, circle_color, circle_position, size, border)
    # pygame.draw.rect(screen,(100,40,85),(150,100,100, 15), 1) #(target_screen, rectangle_color, (rectangle_position, width, height), border)
    i = 0
    while i < len(raindrops):
        raindrops[i].move()
        raindrops[i].draw(screen)
        if raindrops[i].is_off_screen():
            del raindrops[i]
            i -= 1
        i += 1
        print(len(raindrops))

    heroe.draw(screen)
  
    #Show the images in the screen and update the frame
    pygame.display.update()
    
