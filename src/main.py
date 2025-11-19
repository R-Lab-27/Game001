import pygame, sys
from pygame.locals import *
import constans

pygame.init()

#Set the title for the window
pygame.display.set_caption("Mi Primer Juego")
#Create the window for the game
screen = pygame.display.set_mode((constans.WINDOW_WIDTH,constans.WINDOW_HEIGHT))

clock = pygame.time.Clock()

xpos = 50

#The Game Loop
while True:
    clock.tick(constans.FPS)
    #Polling the events generated from the user
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[K_RIGHT]:
        xpos += 1
    if pressed_keys[K_LEFT]:
        xpos -= 1


    screen.fill((200,200,200))
    #Draw some shapes to the screen
    pygame.draw.circle(screen,(0,180,200), (xpos,150), 10, 2) #(target_screen, circle_color, circle_position, size, border)
    pygame.draw.rect(screen,(100,40,85),(150,100,100, 15), 1) #(target_screen, rectangle_color, (rectangle_position, width, height), border)
    #Show the images in the screen and update the frame
    pygame.display.update()
    
