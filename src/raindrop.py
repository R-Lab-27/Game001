import pygame, random

class Raindrop():
    def __init__(self, width = 640):
        self.x = random.randint(0, width)
        self.y = -5

    def move(self):
        self.y += 7

    def draw(self, screen):
        pygame.draw.line(screen, (0,0,0), (self.x, self.y), (self.x, self.y + 5), 1)