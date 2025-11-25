import pygame, sys, item_constants, os
from constants import WINDOW_HEIGHT, WINDOW_WIDTH, FPS
from inventory_ui import InventoryUI
from character import Player
from plataformas import Platform
from sprite_sheet import SpriteSheet


pygame.init()

#Set the title for the window
pygame.display.set_caption("Mi Primer Juego")
#Create the window for the game
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

item_constants.ITEM_SPRITESHEET = SpriteSheet(item_constants.PATH_ITEMS, item_constants.SPRITE_COLS, item_constants.SPRITE_ROWS)
clock = pygame.time.Clock()


platforms = pygame.sprite.Group()
#Limitando el movimiento al tamaño de la ventana
platforms.add(Platform(0, WINDOW_HEIGHT - 40, WINDOW_WIDTH, 1)) #suelo
platforms.add(Platform(0, 0, WINDOW_WIDTH, 1)) #techo
platforms.add(Platform(0, 0, 1, WINDOW_HEIGHT)) #lado izquierdo
platforms.add(Platform(WINDOW_WIDTH - 1, 0, 1, WINDOW_HEIGHT)) #lado derecho

#Añadiendo algunas plataformas dentro de la ventana
platforms.add(Platform(200, 400, 150, 20))
platforms.add(Platform(500, 360, 180, 20))

heroe = Player(50, 50, platforms)
inventory_ui = InventoryUI(heroe.inventory)
bg = pygame.image.load("src/assets/icons/Background.png").convert_alpha()
bg = pygame.transform.scale(bg, (640, 480))

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PATH_ITEMS = os.path.join(BASE_DIR, "assets", "icons", "apple.png")
apple = pygame.image.load(PATH_ITEMS).convert_alpha()


#The Game Loop
while True:
    dt = clock.tick(FPS)
    #Polling the events generated from the user
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_TAB:
                inventory_ui.toggle()

        heroe.handle_event(event) #Para que el Player pueda procesar algunos eventos

    heroe.update()

    screen.fill((200,200,200))
    screen.blit(bg, (0, 0))
    screen.blit(apple, (10, 10))
    #Draw platforms for debug
    platforms.draw(screen)
    heroe.draw(screen)
    inventory_ui.draw(screen)
    pygame.display.flip()
    #Show the images in the screen and update the frame
    pygame.display.update()
    
