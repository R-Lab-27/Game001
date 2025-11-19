import pygame

class Character():
    def __init__(self, name = ""):
        self.name = name
        self.x = 50
        self.y = 50
        self.sprite = pygame.image.load("/home/r/Training/Proyectos/Game001/src/assets/adventurer-1.3-Sheet.png").convert

    def draw(self, screen):
        screen.blit(self.sprite, (self.x, self.y))