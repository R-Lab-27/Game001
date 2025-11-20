import pygame, sys
import constants
from raindrop import Raindrop
from character import Player
from plataformas import Platform

pygame.init()

#Set the title for the window
pygame.display.set_caption("Mi Primer Juego")
#Create the window for the game
screen = pygame.display.set_mode((constants.WINDOW_WIDTH,constants.WINDOW_HEIGHT))

clock = pygame.time.Clock()

platforms = pygame.sprite.Group()
#Limitando el movimiento al tamaño de la ventana
platforms.add(Platform(0, 480, 680, 1)) #suelo
platforms.add(Platform(0, 0, 480, 1)) #techo
platforms.add(Platform(0, 0, 1, 480)) #lado izquierdo
platforms.add(Platform(679, 0, 1, 480)) #lado derecho

#Añadiendo algunas plataformas dentro de la ventana
platforms.add(Platform(200, 440, 150, 20))
platforms.add(Platform(500, 390, 180, 20))

heroe = Player(50, 50, platforms)


# raindrops = []

#The Game Loop
while True:
    dt = clock.tick(constants.FPS)
    #Polling the events generated from the user
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    heroe.update()

    screen.fill((200,200,200))
    platforms.draw(screen)
    heroe.draw(screen)
    pygame.display.flip()
    #Show the images in the screen and update the frame
    pygame.display.update()
    
